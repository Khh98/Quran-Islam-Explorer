"""Quran data: bundled surah list, cached API calls and verse rendering helpers."""
import html
import json
import re
from pathlib import Path

import requests
import streamlit as st

ROOT = Path(__file__).resolve().parent
API = "https://api.alquran.cloud/v1"
AUDIO_CDN = "https://cdn.islamic.network/quran/audio"

_AR_DIGITS = str.maketrans("0123456789", "٠١٢٣٤٥٦٧٨٩")
_DIACRITICS = re.compile(r"[ؐ-ًؚ-ٰٟۖ-ۭ]")
BASMALA = "بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ"


def num(n, lang: str) -> str:
    """Show numbers with Arabic-Indic digits in the Arabic interface."""
    return str(n).translate(_AR_DIGITS) if lang == "ar" else str(n)


# ---------------------------------------------------------------------------
# Bundled data (no network needed)
# ---------------------------------------------------------------------------
@st.cache_data
def load_surahs() -> list[dict]:
    return json.loads((ROOT / "data" / "surahs.json").read_text(encoding="utf-8"))


@st.cache_data
def load_verses() -> dict:
    return json.loads((ROOT / "data" / "verses.json").read_text(encoding="utf-8"))


def surah(n: int) -> dict:
    return load_surahs()[n - 1]


def surah_label(n: int, lang: str) -> str:
    s = surah(n)
    if lang == "ar":
        return f"{num(n, 'ar')}. {s['ar']} · {s['en']}"
    return f"{n}. {s['en']} · {s['ar']}"


def ayah_audio_url(global_num: int, reciter: dict) -> str:
    return f"{AUDIO_CDN}/{reciter['kbps']}/{reciter['id']}/{global_num}.mp3"


# ---------------------------------------------------------------------------
# Live data (cached)
# ---------------------------------------------------------------------------
def _strip_basmala(text: str) -> str:
    if _DIACRITICS.sub("", text).startswith("بسم"):
        return " ".join(text.split(" ")[4:])
    return text


@st.cache_data(ttl=7 * 24 * 3600, show_spinner=False, max_entries=120)
def fetch_surah_text(n: int) -> list[dict]:
    """Full surah: Uthmani text, plain text (for the AI prompt), Sahih International, Tafsir al-Muyassar."""
    editions = "quran-uthmani,quran-simple-clean,en.sahih,ar.muyassar"
    r = requests.get(f"{API}/surah/{n}/editions/{editions}", timeout=30)
    r.raise_for_status()
    uth, clean, en, tafsir = (e["ayahs"] for e in r.json()["data"])
    ayahs = []
    for u, c, e, t in zip(uth, clean, en, tafsir):
        a = {"a": u["numberInSurah"], "g": u["number"], "ar": u["text"], "clean": c["text"],
             "en": e["text"], "tafsir": t["text"]}
        if a["a"] == 1 and n not in (1, 9):
            a["ar"], a["clean"] = _strip_basmala(a["ar"]), _strip_basmala(a["clean"])
        ayahs.append(a)
    return ayahs


@st.cache_data(ttl=30 * 24 * 3600, show_spinner=False, max_entries=600)
def fetch_bytes(url: str) -> bytes:
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    return r.content


# ---------------------------------------------------------------------------
# HTML rendering
# ---------------------------------------------------------------------------
def ayah_marker(a: int) -> str:
    return f'<span class="ayah-num">﴿{num(a, "ar")}﴾</span>'


def verses_block(ayahs: list[dict], show_en: bool = False, show_tafsir: bool = False,
                 inline: bool = True) -> str:
    """Arabic verses (RTL, Quran font) with optional translation / tafsir under each verse."""
    if inline and not show_en and not show_tafsir:
        body = " ".join(f"{html.escape(x['ar'])} {ayah_marker(x['a'])}" for x in ayahs)
        return f'<div class="quran">{body}</div>'
    rows = []
    for x in ayahs:
        row = f'<div class="quran">{html.escape(x["ar"])} {ayah_marker(x["a"])}</div>'
        if show_en and x.get("en"):
            row += f'<div class="translation" dir="ltr"><span class="t-num">{x["a"]}.</span> {html.escape(x["en"])}</div>'
        if show_tafsir and x.get("tafsir"):
            row += f'<div class="tafsir" dir="rtl">{html.escape(x["tafsir"])}</div>'
        rows.append(f'<div class="ayah-row">{row}</div>')
    return "".join(rows)


def reference(s: int, a1: int, a2: int, lang: str) -> str:
    meta = surah(s)
    if lang == "ar":  # e.g. «الشعراء · الآيات ٦١–٦٢»
        span = f"الآية {num(a1, 'ar')}" if a1 == a2 else f"الآيات {num(a1, 'ar')}–{num(a2, 'ar')}"
        return f"{meta['ar']} · {span}"
    span = str(a1) if a1 == a2 else f"{a1}–{a2}"
    return f"{meta['en']} · {s}:{span}"
