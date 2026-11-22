"""
Surah audio lessons.

Flow:  real surah text (API)  ->  AI chooses key passages + writes a spoken explanation
       ->  a real Qari recites those verses  ->  edge-tts narrates the explanation
       ->  ffmpeg stitches everything into ONE mp3 (about 3 minutes).

The AI never writes Quran verses itself: the verse text shown is the authentic
Uthmani text and the verses you hear are recited by a real Qari.
"""
import asyncio
import json
import os
import re
import shutil
import subprocess
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import edge_tts
import requests
import streamlit as st

from quran import ayah_audio_url, fetch_surah_text, surah

DEFAULT_MODEL = "gpt-5.6-sol"


# ---------------------------------------------------------------------------
# Secrets / client
# ---------------------------------------------------------------------------
def get_secret(name: str, default=None):
    try:
        value = st.secrets.get(name)
    except Exception:  # no secrets.toml at all
        value = None
    return value or os.environ.get(name) or default


def has_api_key() -> bool:
    return bool(get_secret("OPENAI_API_KEY"))


@st.cache_resource(show_spinner=False)
def _client(api_key: str):
    from openai import OpenAI
    return OpenAI(api_key=api_key, timeout=120, max_retries=2)


# ---------------------------------------------------------------------------
# 1) AI lesson plan
# ---------------------------------------------------------------------------
_LANG_RULES = {
    "ar": ("Write everything in clear, simple Modern Standard Arabic (فصحى ميسّرة) for a general audience. "
           "Write «النبي صلى الله عليه وسلم» in full, never as a symbol. "
           "Start each explanation with the overall meaning of the recited verses, then the deeper insight."),
    "en": ("Write everything in clear, warm, simple English for a general audience, including new Muslims and "
           "non-Muslims. Use Arabic terms sparingly and explain them. Write 'the Prophet, peace be upon him' in full, "
           "never as a symbol. Start each explanation by conveying the meaning of the recited verses in your own "
           "words, because the listener may not understand Arabic."),
}
# Length calibration (measured): narration ~115 words/min in Arabic and ~150 in English;
# a Qari like Alafasy recites ~0.85 Quran words per second. Targets give a ~3-3.5 minute lesson.
_WORDS = {
    "ar": {"intro": "30-45", "expl": "30-50", "lesson": "8-14", "closing": "15-25", "total": "200-260"},
    "en": {"intro": "40-55", "expl": "40-60", "lesson": "10-16", "closing": "18-28", "total": "240-320"},
}
WHOLE_SURAH_MAX_WORDS = 45   # surahs up to this length are recited in full (Al-Kawthar ... Al-'Adiyat)
RECITATION_MAX_WORDS = 90    # hard safety cap (~100 s); the prompt itself asks for ~60 words (~70 s)


def _quran_words(ayahs: list[dict]) -> int:
    return sum(len(a["clean"].split()) for a in ayahs)


def _system_prompt(lang: str, ayahs: list[dict]) -> str:
    w = _WORDS[lang]
    if _quran_words(ayahs) <= WHOLE_SURAH_MAX_WORDS:
        passage_rule = (f"This surah is short: cover ALL {len(ayahs)} verses, in order, grouped into 1 to 3 passages "
                        "of consecutive verses.")
    else:
        passage_rule = ("Choose 3 or 4 passages that best capture the surah's message, each 1 or 2 consecutive verses "
                        "(3 only if they are very short). Prefer well-known, central verses that people memorise and "
                        "reflect on. Keep the recitation short: all chosen verses together should contain no more than "
                        "about 60 words of Quran text, so prefer short and medium verses (one central long verse such "
                        "as Ayat al-Kursi is fine on its own).")
    return f"""You are a warm, knowledgeable Quran teacher preparing a short AUDIO lesson (about 3 minutes in total) on one surah.
A professional Qari will recite the verses you choose, and a narrator voice will read everything you write.

ACCURACY (most important)
- Base every explanation on well-established classical tafsir: Ibn Kathir, al-Tabari, al-Sa'di and al-Tafsir al-Muyassar. Do not speculate or invent.
- Mention a hadith or an occasion of revelation only if it is well known and authentic; otherwise leave it out.
- No fatwas or rulings on disputed matters. Be gentle, respectful and hopeful.
- Never write out whole verses yourself; the Qari recites them. You may quote a key word or a short phrase to explain it.

SPOKEN STYLE
- {_LANG_RULES[lang]}
- Short, flowing sentences. No lists, bullet points, emojis, markdown, brackets, digits or verse numbers; write any number as words.

CHOOSING THE VERSES
- {passage_rule}
- Passages must follow the order of the surah and must not overlap.

OUTPUT: one JSON object with exactly these keys:
{{
  "theme": "the surah's central theme as a short title (max 8 words)",
  "intro": "{w['intro']} words: the meaning of the surah's name, whether it is Meccan or Medinan, its central message, and the context of revelation if well known",
  "passages": [
    {{"from": <first verse number>, "to": <last verse number>,
      "heading": "max 6 words",
      "lead_in": "one short spoken sentence (max 12 words) that introduces the recitation, e.g. 'Let us listen to the opening verses.'",
      "explanation": "{w['expl']} words: what these verses mean and how they connect to the surah's message"}}
  ],
  "lessons": ["exactly three practical lessons for daily life, {w['lesson']} words each"],
  "closing": "{w['closing']} words: a short closing reflection or dua"
}}
Total written words: about {w['total']}."""


def _user_prompt(n: int, lang: str, ayahs: list[dict]) -> str:
    s = surah(n)
    text = "\n".join(f"{a['a']}: {a['clean']}" for a in ayahs)
    language = "Arabic" if lang == "ar" else "English"
    return (f"Surah {n}: {s['en']} ({s['ar']}), \"{s['meaning']}\". {s['type']}. {s['ayahs']} verses.\n"
            f"Lesson language: {language}\n\nFull text (verse number: text):\n{text}\n\nReturn only the JSON object.")


def _parse_json(raw: str) -> dict:
    raw = (raw or "").strip()
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", raw, re.S)
        if not match:
            raise ValueError("AI response was not JSON")
        return json.loads(match.group(0))


def _clean(text) -> str:
    text = re.sub(r"[*_#`>\[\]]", "", str(text or ""))
    return re.sub(r"\s+", " ", text).strip()


def _fit_recitation(passages: list[dict], words: dict[int, int], budget: int) -> None:
    """Keep the recited verses within the time budget (safety net if the AI picked too many)."""
    def size(p):
        return sum(words[a] for a in range(p["from"], p["to"] + 1))
    # 1) a single verse longer than the whole budget (e.g. 2:282) goes first
    for p in sorted(passages, key=size, reverse=True):
        if len(passages) > 2 and p["from"] == p["to"] and size(p) > budget:
            passages.remove(p)
    # 2) shorten multi-verse passages, then 3) drop the longest single verses
    while sum(size(p) for p in passages) > budget:
        multi = [p for p in passages if p["to"] > p["from"]]
        if multi:
            max(multi, key=size)["to"] -= 1          # shorten the longest passage
        elif len(passages) > 2:
            passages.remove(max(passages, key=size))  # drop the longest single verse
        else:
            break


def _validate(plan: dict, ayahs: list[dict]) -> dict:
    n_ayahs = len(ayahs)
    whole = _quran_words(ayahs) <= WHOLE_SURAH_MAX_WORDS
    spans = []
    for p in plan.get("passages", []):
        try:
            spans.append((int(p["from"]), int(p.get("to", p["from"])), p))
        except (KeyError, TypeError, ValueError, AttributeError):
            continue  # malformed entry from the AI: skip it
    passages, last_to = [], 0
    for a, b, p in sorted(spans, key=lambda x: x[0]):
        a = max(a, last_to + 1)
        b = min(max(a, b), n_ayahs)
        if not whole:
            b = min(b, a + 2)  # at most 3 verses per passage
        if a > n_ayahs or not _clean(p.get("explanation")):
            continue
        passages.append({"from": a, "to": b, "heading": _clean(p.get("heading")),
                         "lead_in": _clean(p.get("lead_in")), "explanation": _clean(p.get("explanation"))})
        last_to = b
    passages = passages[:4]
    if not passages or not _clean(plan.get("intro")):
        raise ValueError("AI lesson plan was incomplete")
    if not whole:
        _fit_recitation(passages, {a["a"]: len(a["clean"].split()) for a in ayahs}, RECITATION_MAX_WORDS)
    lessons = [_clean(x) for x in plan.get("lessons", []) if _clean(x)][:4]
    return {"theme": _clean(plan.get("theme")), "intro": _clean(plan.get("intro")), "passages": passages,
            "lessons": lessons, "closing": _clean(plan.get("closing"))}


@st.cache_data(persist="disk", show_spinner=False)
def plan_lesson(n: int, lang: str, model: str) -> dict:
    """Cached on disk: each surah/language is generated once, then served instantly."""
    import openai

    ayahs = fetch_surah_text(n)
    client = _client(get_secret("OPENAI_API_KEY"))
    kwargs = dict(
        model=model,
        messages=[{"role": "system", "content": _system_prompt(lang, ayahs)},
                  {"role": "user", "content": _user_prompt(n, lang, ayahs)}],
        # Generous budget: reasoning models spend part of it thinking before they answer.
        max_completion_tokens=12000,
    )
    try:
        resp = client.chat.completions.create(response_format={"type": "json_object"}, **kwargs)
    except openai.BadRequestError:
        resp = client.chat.completions.create(**kwargs)  # model without JSON mode
    return _validate(_parse_json(resp.choices[0].message.content), ayahs)


# ---------------------------------------------------------------------------
# 2) Narration (edge-tts)
# ---------------------------------------------------------------------------
_ORDINALS = {"ar": ["أولاً", "ثانياً", "ثالثاً", "رابعاً"], "en": ["First", "Second", "Third", "Fourth"]}
_LESSONS_INTRO = {"ar": "ومن الدروس العملية التي نتعلّمها من هذه السورة.",
                  "en": "Here are some practical lessons we can take from this surah."}


def narration_texts(plan: dict, lang: str) -> list[str]:
    """One narration chunk before each recitation, plus the final chunk (explanation + lessons + closing)."""
    comma = "،" if lang == "ar" else ","
    P = plan["passages"]
    texts = [f"{plan['intro']} {P[0]['lead_in']}".strip()]
    for i, p in enumerate(P):
        t = p["explanation"]
        if i + 1 < len(P):
            t += " " + P[i + 1]["lead_in"]
        else:
            if plan["lessons"]:
                t += " " + _LESSONS_INTRO[lang] + " " + " ".join(
                    f"{_ORDINALS[lang][j]}{comma} {x}" for j, x in enumerate(plan["lessons"]))
            t += " " + plan["closing"]
        texts.append(t.strip())
    return texts


async def _tts_one(text: str, voice: str, sem: asyncio.Semaphore) -> bytes:
    error = None
    async with sem:
        for attempt in range(3):
            try:
                buf = bytearray()
                async for chunk in edge_tts.Communicate(text, voice).stream():
                    if chunk["type"] == "audio":
                        buf.extend(chunk["data"])
                if buf:
                    return bytes(buf)
            except Exception as e:  # network hiccup / throttling
                error = e
            await asyncio.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"Text-to-speech failed: {error}")


@st.cache_data(show_spinner=False, max_entries=120)
def tts_segments(texts: tuple[str, ...], voice: str) -> list[bytes]:
    async def run():
        sem = asyncio.Semaphore(3)
        return await asyncio.gather(*(_tts_one(t, voice, sem) for t in texts))
    return list(asyncio.run(run()))


# ---------------------------------------------------------------------------
# 3) Mixing (ffmpeg)
# ---------------------------------------------------------------------------
def _ffmpeg() -> str:
    exe = shutil.which("ffmpeg")
    if exe:
        return exe
    import imageio_ffmpeg  # pip-installed static ffmpeg (works on Windows and Streamlit Cloud)
    return imageio_ffmpeg.get_ffmpeg_exe()


def mix_mp3(parts: list[tuple[bytes, float]], normalize: bool = True) -> tuple[bytes, float]:
    """Join mp3 clips (each followed by `gap` seconds of silence) into one mono mp3. Returns (mp3, seconds)."""
    with tempfile.TemporaryDirectory() as tmp:
        cmd = [_ffmpeg(), "-hide_banner", "-loglevel", "error", "-y"]
        chains = []
        for i, (data, gap) in enumerate(parts):
            path = Path(tmp) / f"{i}.mp3"
            path.write_bytes(data)
            cmd += ["-i", str(path)]
            pad = f",apad=pad_dur={gap}" if gap else ""
            chains.append(f"[{i}:a]aresample=44100,aformat=sample_fmts=fltp:channel_layouts=mono{pad}[a{i}]")
        n = len(parts)
        tail = ",loudnorm=I=-16:TP=-1.5:LRA=11,aresample=44100" if normalize else ""
        chains.append("".join(f"[a{i}]" for i in range(n)) + f"concat=n={n}:v=0:a=1{tail}[out]")
        out = Path(tmp) / "lesson.mp3"
        cmd += ["-filter_complex", ";".join(chains), "-map", "[out]", "-ac", "1",
                "-c:a", "libmp3lame", "-b:a", "64k", str(out)]
        subprocess.run(cmd, check=True, capture_output=True, timeout=180)
        data = out.read_bytes()
    return data, len(data) * 8 / 64000  # constant 64 kbps -> duration


def _download_all(urls: list[str]) -> list[bytes]:
    def get(url):
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        return r.content
    with ThreadPoolExecutor(max_workers=6) as pool:
        return list(pool.map(get, urls))


@st.cache_data(show_spinner=False, max_entries=40)
def lesson_audio(n: int, lang: str, voice: str, reciter: dict, model: str) -> tuple[bytes, float]:
    """The final lesson mp3 (cached per surah / language / voice / Qari)."""
    plan = plan_lesson(n, lang, model)
    narration = tts_segments(tuple(narration_texts(plan, lang)), voice)
    ayahs = {a["a"]: a for a in fetch_surah_text(n)}

    # Recitation clips: Basmala before a passage that starts the surah (not for Al-Fatihah / At-Tawbah).
    groups = []
    for p in plan["passages"]:
        nums = [ayahs[a]["g"] for a in range(p["from"], p["to"] + 1)]
        if p["from"] == 1 and n not in (1, 9):
            nums = [1] + nums  # 1:1 is the Basmala
        groups.append(nums)
    flat = [g for grp in groups for g in grp]
    clips = iter(_download_all([ayah_audio_url(g, reciter) for g in flat]))

    parts = [(narration[0], 0.6)]
    for i, grp in enumerate(groups):
        for j in range(len(grp)):
            parts.append((next(clips), 0.7 if j == len(grp) - 1 else 0.25))
        parts.append((narration[i + 1], 0.6))
    return mix_mp3(parts)


@st.cache_data(show_spinner=False, max_entries=60)
def joined_ayah_audio(global_nums: tuple[int, ...], reciter: dict) -> bytes:
    """Several consecutive ayahs as one clip (used for Ayah of the Day ranges)."""
    clips = _download_all([ayah_audio_url(g, reciter) for g in global_nums])
    return mix_mp3([(c, 0.3) for c in clips], normalize=False)[0]
