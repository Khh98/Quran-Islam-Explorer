"""
Quran & Islam Explorer
Run locally:   streamlit run main_q.py
"""
import datetime as dt
import html
import logging
from pathlib import Path

import requests
import streamlit as st
from streamlit_lottie import st_lottie

import lesson
from content import (AYAH_OF_DAY, FEATURED_VIDEOS, LESSON_LANG_LABEL, PROPHETS, RECITERS, UI,
                     VERSE_RECITERS)
from quran import (BASMALA, ayah_audio_url, fetch_surah_text, load_verses, num, reference, surah,
                   surah_label, verses_block)

st.set_page_config(page_title="Quran & Islam Explorer", page_icon="🕌", layout="wide",
                   initial_sidebar_state="collapsed")

ROOT = Path(__file__).resolve().parent
log = logging.getLogger("quran_app")

PAGES = ["home", "listen", "explain", "prophets"]
NAV_ICONS = {"home": "🏠", "listen": "🎧", "explain": "📖", "prophets": "🌟"}
# Which image in /static each page uses, and where to focus it on portrait phones.
BACKGROUNDS = {"home": "bg_main", "listen": "bg_main", "explain": "bg_main", "prophets": "bg_prophets"}
MOBILE_FOCUS = {"bg_main": "36% center", "bg_prophets": "68% center"}
LOTTIE_URL = "https://lottie.host/713e9554-ee5f-41b8-a6ac-423cc61b12f6/FX5BAKwcuR.json"
SURAH_NUMBERS = list(range(1, 115))
RECITER_BY_ID = {r["id"]: r for r in RECITERS}
VERSE_RECITER_BY_ID = {r["id"]: r for r in VERSE_RECITERS}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def lang() -> str:
    return st.session_state.lang


def t(key: str, lng: str | None = None) -> str:
    return UI[lng or lang()][key]


def esc(text: str) -> str:
    return html.escape(text, quote=False)


def read_css() -> str:
    return (ROOT / "style.css").read_text(encoding="utf-8")


@st.cache_data(ttl=24 * 3600, show_spinner=False)
def load_lottie(url: str):
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        return r.json()
    except Exception:
        return None


def page_header(title: str, subtitle: str = ""):
    sub = f'<p class="page-sub">{esc(subtitle)}</p>' if subtitle else ""
    st.html(f'<div class="page-head"><h1 class="page-title">{esc(title)}</h1>{sub}</div>')


def bilingual_select(label: str, options: list, format_func, name: str):
    """A selectbox whose labels follow the language while keeping the chosen value.

    One widget per language (so the visible label always refreshes); the choice
    itself lives in st.session_state[name] and is carried across languages.
    """
    wkey = f"{name}__{lang()}"
    st.session_state[wkey] = st.session_state.get(name, options[0])

    def remember():
        st.session_state[name] = st.session_state[wkey]

    return st.selectbox(label, options, format_func=format_func, key=wkey, on_change=remember)


def verse_count(n: int, lng: str) -> str:
    if lng == "ar":  # Arabic plural rules: 3-10 take the plural form
        return f"{num(n, 'ar')} {'آيات' if 3 <= n % 100 <= 10 else 'آية'}"
    return f"{n} verses"


def reciter_label(r: dict) -> str:
    return f"{r['ar']} · {r['en']}" if lang() == "ar" else f"{r['en']} · {r['ar']}"


def prophet_name(p: dict, lng: str) -> str:
    name = p[lng]
    if "ﷺ" in name:
        return name
    if lng == "ar":
        return name + (" عليهما السلام" if " و" in name else " عليه السلام")
    return name + " (AS)"


def verse_audio(items: list[dict]):
    """Recitation (Mishary Alafasi) for one verse or a short range of verses."""
    reciter = VERSE_RECITERS[0]
    if len(items) == 1:
        st.audio(ayah_audio_url(items[0]["g"], reciter), format="audio/mpeg")
        return
    try:
        st.audio(lesson.joined_ayah_audio(tuple(x["g"] for x in items), reciter), format="audio/mpeg")
    except Exception:
        log.exception("joining ayah audio failed")
        st.audio(ayah_audio_url(items[0]["g"], reciter), format="audio/mpeg")


# ---------------------------------------------------------------------------
# State, styles and navigation
# ---------------------------------------------------------------------------
def init_state():
    qp = st.query_params
    if "lang" not in st.session_state:
        st.session_state.lang = qp.get("lang") if qp.get("lang") in ("en", "ar") else "en"
    if "nav" not in st.session_state:
        st.session_state.nav = qp.get("page") if qp.get("page") in PAGES else "home"
    if "lesson_lang" not in st.session_state:
        st.session_state.lesson_lang = st.session_state.lang
    st.session_state.setdefault("lesson_voice", "male")


def inject_styles(page: str):
    img = BACKGROUNDS[page]
    shade = "linear-gradient(180deg, rgba(6,8,14,.55) 0%, rgba(6,8,14,.30) 35%, rgba(6,8,14,.80) 100%)"
    css = read_css() + f"""
    .stApp {{ background-image: {shade}, url("app/static/{img}.jpg"); }}
    @media (max-width: 768px) {{
      .stApp {{ background-image: {shade}, url("app/static/{img}_mobile.jpg"); background-position: {MOBILE_FOCUS[img]}; }}
    }}"""
    if lang() == "ar":
        css += """
    [data-testid="stMainBlockContainer"] { direction: rtl; }
    [data-testid="stMainBlockContainer"] [data-testid="stMarkdownContainer"],
    [data-testid="stMainBlockContainer"] [data-testid="stWidgetLabel"] { text-align: right; }
    [role="listbox"] [role="option"] { direction: rtl; text-align: right; }"""
    st.html(f"<style>{css}</style>")


def top_bar():
    with st.container(key="topbar"):
        with st.container(horizontal=True, vertical_alignment="center", key="brandrow"):
            st.html(f'<div class="brand"><span class="brand-mark">۞</span><span>{esc(t("app_title"))}</span></div>',
                    width="stretch")
            st.segmented_control("Language", ["en", "ar"], key="lang", required=True,
                                 format_func=lambda x: "EN" if x == "en" else "عربي",
                                 label_visibility="collapsed")
        st.segmented_control("Navigation", PAGES, key="nav", required=True, width="stretch",
                             format_func=lambda p: f"{NAV_ICONS[p]} {t('nav_' + p)}",
                             label_visibility="collapsed")
    # Shareable links: ?page=prophets&lang=ar
    st.query_params.update({"page": st.session_state.nav, "lang": st.session_state.lang})


def footer():
    st.html(f'<div class="foot">{esc(t("footer"))}</div>')


# ---------------------------------------------------------------------------
# Page: Home
# ---------------------------------------------------------------------------
def page_home():
    col_text, col_anim = st.columns([3, 2], gap="large", vertical_alignment="center")
    with col_text:
        st.html(f"""
        <div class="qcard intro">
          <div class="eyebrow">بسم الله الرحمن الرحيم</div>
          <h1 class="intro-title">{esc(t("welcome"))}</h1>
          <p>{esc(t("intro_p1"))}</p>
          <p>{esc(t("intro_p2"))}</p>
          <p class="features-title">{esc(t("features_title"))}</p>
          <ul class="features">
            <li>{t("feature_1")}</li><li>{t("feature_2")}</li><li>{t("feature_3")}</li>
          </ul>
          <p class="intro-end">{esc(t("intro_end"))}</p>
        </div>""")
    with col_anim:
        animation = load_lottie(LOTTIE_URL)
        with st.container(key="lottie"):
            if animation:
                st_lottie(animation, height=360, key="animation")

    # Ayah of the day: same verse for everyone today, changes daily.
    ref = AYAH_OF_DAY[dt.date.today().toordinal() % len(AYAH_OF_DAY)]
    items = load_verses()[ref]
    s, a1, a2 = items[0]["s"], items[0]["a"], items[-1]["a"]
    translation = ""
    if lang() == "en":
        translation = '<p class="aod-en">' + esc(" ".join(x["en"] for x in items)) + "</p>"
    with st.container(key="card_aod"):
        st.html(f"""
          <div class="eyebrow">✦ {esc(t("ayah_of_day"))}</div>
          {verses_block([{"a": x["a"], "ar": x["ar"]} for x in items]).replace('class="quran"', 'class="quran center"')}
          {translation}
          <div class="ref center">{esc(reference(s, a1, a2, lang()))}</div>""")
        verse_audio(items)


# ---------------------------------------------------------------------------
# Page: Listen (full-surah recitation + read along)
# ---------------------------------------------------------------------------
def page_listen():
    page_header(t("listen_title"), t("listen_sub"))
    lg = lang()
    with st.container(key="card_player"):
        c1, c2 = st.columns(2)
        with c1:
            n = bilingual_select(t("select_surah"), SURAH_NUMBERS, lambda x: surah_label(x, lg), "listen_surah")
        with c2:
            rid = bilingual_select(t("select_reciter"), list(RECITER_BY_ID),
                                   lambda i: reciter_label(RECITER_BY_ID[i]), "listen_reciter")
        meta = surah(n)
        other_name = meta["meaning"] if lg == "en" else meta["en"]
        st.html(f"""<div class="chips">
            <span class="chip gold">{esc(meta['ar'])}</span>
            <span class="chip">{esc(other_name)}</span>
            <span class="chip">{esc(t(meta['type']))}</span>
            <span class="chip">{verse_count(meta['ayahs'], lg)}</span></div>""")
        st.audio(f"{RECITER_BY_ID[rid]['url']}{n:03d}.mp3", format="audio/mpeg")
        st.caption(t("audio_note"))

    reader = st.expander(t("read_along"), key="read_along", on_change="rerun")
    with reader:
        if reader.open:
            show_tafsir = st.toggle(t("show_tafsir"), key="read_tafsir") if lg == "ar" else False
            try:
                ayahs = fetch_surah_text(n)
            except Exception:
                st.warning(t("text_failed"))
            else:
                basmala = f'<div class="basmala">{BASMALA}</div>' if n not in (1, 9) else ""
                st.html(basmala + verses_block(ayahs, show_en=(lg == "en"), show_tafsir=show_tafsir))

    st.html(f'<h2 class="section-title">{esc(t("featured_title"))}</h2>')
    for i, v in enumerate(FEATURED_VIDEOS):
        name = f"{v['ar']} · {v['en']}" if lg == "ar" else v["en"]
        box = st.expander(name, icon="🎙️", key=f"video_{i}", on_change="rerun")
        with box:
            if box.open:
                st.html(f'<p class="muted">{esc(v["desc_" + lg])}</p>')
                st.video(v["youtube"])


# ---------------------------------------------------------------------------
# Page: Explain (AI audio lesson)
# ---------------------------------------------------------------------------
def page_explain():
    page_header(t("explain_title"), t("explain_sub"))
    lg = lang()
    with st.container(key="card_lesson_form"):
        n = bilingual_select(t("select_surah"), SURAH_NUMBERS, lambda x: surah_label(x, lg), "explain_surah")
        c1, c2, c3 = st.columns([1, 1, 1.4])
        with c1:
            lesson_lang = st.segmented_control(t("lesson_lang"), ["ar", "en"], key="lesson_lang", required=True,
                                               format_func=LESSON_LANG_LABEL.get, width="stretch")
        with c2:
            voice_key = st.segmented_control(t("voice"), ["male", "female"], key="lesson_voice", required=True,
                                             format_func=lambda v: t("voice_" + v), width="stretch")
        with c3:
            rid = bilingual_select(t("verse_reciter"), list(VERSE_RECITER_BY_ID),
                                   lambda i: reciter_label(VERSE_RECITER_BY_ID[i]), "lesson_reciter")
        go = st.button(t("generate"), type="primary", width="stretch", disabled=not lesson.has_api_key())
        if not lesson.has_api_key():
            st.info(t("no_key"))

    selection = (n, lesson_lang, voice_key, rid)
    if go:
        generate_lesson(*selection)
    current = st.session_state.get("lesson")
    if current and current["selection"] == selection:
        render_lesson(current)


def generate_lesson(n: int, lesson_lang: str, voice_key: str, rid: str):
    model = lesson.get_secret("OPENAI_MODEL", lesson.DEFAULT_MODEL)
    reciter = VERSE_RECITER_BY_ID[rid]
    stage = "text_failed"
    with st.status(t("step_text"), expanded=False) as status:
        try:
            fetch_surah_text(n)
            stage = "ai_error"
            status.update(label=t("step_plan"))
            plan = lesson.plan_lesson(n, lesson_lang, model, lesson.PROMPT_VERSION)
            stage = "tts_error"
            status.update(label=t("step_voice"))
            narration, fallback = lesson.narrate(tuple(lesson.narration_texts(plan, lesson_lang)),
                                                 lesson_lang, voice_key)
            stage = "audio_error"
            status.update(label=t("step_recite"))
            spans = tuple((p["from"], p["to"]) for p in plan["passages"])
            audio, seconds = lesson.mix_lesson(n, spans, reciter, tuple(narration))
        except Exception:
            log.exception("lesson generation failed at %s", stage)
            status.update(label=t("step_failed"), state="error")
            st.error(t(stage))
            return
        status.update(label=t("step_done"), state="complete")
    st.session_state.lesson = {"selection": (n, lesson_lang, voice_key, rid), "plan": plan,
                               "audio": audio, "seconds": seconds, "fallback": fallback}


def render_lesson(data: dict):
    n, ll, _, _ = data["selection"]
    plan, meta = data["plan"], surah(n)
    direction = "rtl" if ll == "ar" else "ltr"
    ayahs = {a["a"]: a for a in fetch_surah_text(n)}
    secs = int(round(data["seconds"]))
    minutes = f"{num(secs // 60, ll)}:{num(f'{secs % 60:02d}', ll)} {t('minutes', ll)}"
    title = f"{meta['ar']} · {meta['en']}" if ll == "ar" else f"{meta['en']} · {meta['ar']}"

    with st.container(key="card_lesson_audio"):
        st.html(f"""<div dir="{direction}" class="lesson-head">
              <div class="eyebrow">🎧 {esc(t("lesson_ready", ll))} · {minutes}</div>
              <h2 class="lesson-title">{esc(title)}</h2>
              <div class="lesson-theme">{esc(plan["theme"])}</div></div>""")
        st.audio(data["audio"], format="audio/mpeg")
        st.download_button(t("download", ll), data=data["audio"], mime="audio/mpeg",
                           file_name=f"{n:03d}-{meta['en'].replace(' ', '_')}-lesson-{ll}.mp3")
        if data.get("fallback"):
            st.caption("⚠️ " + t("voice_fallback", ll))

    parts = [f'<div class="qcard"><p class="explain" dir="{direction}">{esc(plan["intro"])}</p></div>',
             f'<h2 class="section-title" dir="{direction}">{esc(t("key_verses", ll))}</h2>']
    for p in plan["passages"]:
        chunk = [ayahs[a] for a in range(p["from"], p["to"] + 1)]
        tafsir = "".join(f'<p>{esc(x["tafsir"])} {num(x["a"], "ar")}</p>' for x in chunk)
        parts.append(f"""
        <div class="qcard passage">
          <div class="passage-head" dir="{direction}">
            <span class="passage-title">{esc(p["heading"])}</span>
            <span class="ref">{esc(reference(n, p["from"], p["to"], ll))}</span>
          </div>
          {verses_block(chunk, show_en=(ll == "en"))}
          <p class="explain" dir="{direction}">{esc(p["explanation"])}</p>
          <details class="tafsir-box" dir="rtl"><summary>{esc(t("tafsir_muyassar", ll))}</summary>{tafsir}</details>
        </div>""")
    if plan["lessons"]:
        items = "".join(f"<li>{esc(x)}</li>" for x in plan["lessons"])
        parts.append(f"""<div class="qcard" dir="{direction}"><div class="eyebrow">✦ {esc(t("lessons", ll))}</div>
                        <ul class="lessons-list">{items}</ul></div>""")
    if plan["closing"]:
        parts.append(f"""<div class="qcard" dir="{direction}"><div class="eyebrow">✦ {esc(t("closing", ll))}</div>
                        <p class="explain">{esc(plan["closing"])}</p></div>""")
    st.html("".join(parts))
    st.caption(t("disclaimer", ll))


# ---------------------------------------------------------------------------
# Page: Stories of the Prophets
# ---------------------------------------------------------------------------
def page_prophets():
    page_header(t("prophets_title"), t("prophets_sub"))
    lg = lang()
    verses = load_verses()
    for i, p in enumerate(PROPHETS):
        label = f"{prophet_name(p, lg)} · {p['title_' + lg]}"
        box = st.expander(label, icon=p["icon"], key=f"prophet_{i}", on_change="rerun")
        with box:
            if not box.open:
                continue
            items = verses[p["verse"]]
            s, a1, a2 = items[0]["s"], items[0]["a"], items[-1]["a"]
            badge = f'<span class="chip gold">⭐ {esc(t("ulul_azm"))}</span>' if p["ulul_azm"] else ""
            lessons_html = "".join(f"<li>{esc(x)}</li>" for x in p["lessons_" + lg])
            translation = ""
            if lg == "en":
                translation = '<p class="aod-en">' + esc(" ".join(x["en"] for x in items)) + "</p>"
            st.html(f"""
              <div class="prophet">
                {f'<div class="chips">{badge}</div>' if badge else ''}
                <div class="eyebrow">{esc(t("story"))}</div>
                <p class="story">{esc(p["story_" + lg])}</p>
                <div class="verse-box">
                  <div class="eyebrow">📖 {esc(t("from_quran"))}</div>
                  {verses_block([{"a": x["a"], "ar": x["ar"]} for x in items])}
                  {translation}
                  <div class="ref">{esc(reference(s, a1, a2, lg))}</div>
                </div>
              </div>""")
            verse_audio(items)
            st.html(f"""<div class="eyebrow">💡 {esc(t("life_lessons"))}</div>
                        <ul class="lessons-list">{lessons_html}</ul>""")
            if st.button(t("listen_story"), key=f"story_tts_{i}"):
                text = f"{prophet_name(p, lg)}. {p['story_' + lg]} " + " ".join(p["lessons_" + lg])
                try:
                    text = text.replace("ﷺ", "صلى الله عليه وسلم" if lg == "ar" else "peace be upon him")
                    audio = lesson.narrate((text,), lg, "male")[0][0]
                    st.audio(audio, format="audio/mpeg", autoplay=True)
                except Exception:
                    log.exception("story tts failed")
                    st.error(t("tts_error"))


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
init_state()
inject_styles(st.session_state.nav)
top_bar()
{"home": page_home, "listen": page_listen, "explain": page_explain, "prophets": page_prophets}[st.session_state.nav]()
footer()
