"""
One-off build script: regenerates the bundled data files in ../data and the
optimised background images in ../static.

Run it from anywhere:   python tools/build_data.py

Why bundle?  The app no longer depends on an external API just to show the
surah list, and every Quran verse shown on the Home / Prophets pages comes
from the API (Uthmani script + Sahih International), never typed by hand.
"""
import json
import re
import time
from pathlib import Path

import requests
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
STATIC = ROOT / "static"
API = "https://api.alquran.cloud/v1"

# quran.com style transliterations (what the original app showed)
NAMES_EN = """Al-Fatihah|Al-Baqarah|Ali 'Imran|An-Nisa|Al-Ma'idah|Al-An'am|Al-A'raf|Al-Anfal|At-Tawbah|Yunus|Hud|Yusuf|Ar-Ra'd|Ibrahim|Al-Hijr|An-Nahl|Al-Isra|Al-Kahf|Maryam|Taha|Al-Anbiya|Al-Hajj|Al-Mu'minun|An-Nur|Al-Furqan|Ash-Shu'ara|An-Naml|Al-Qasas|Al-'Ankabut|Ar-Rum|Luqman|As-Sajdah|Al-Ahzab|Saba|Fatir|Ya-Sin|As-Saffat|Sad|Az-Zumar|Ghafir|Fussilat|Ash-Shura|Az-Zukhruf|Ad-Dukhan|Al-Jathiyah|Al-Ahqaf|Muhammad|Al-Fath|Al-Hujurat|Qaf|Adh-Dhariyat|At-Tur|An-Najm|Al-Qamar|Ar-Rahman|Al-Waqi'ah|Al-Hadid|Al-Mujadila|Al-Hashr|Al-Mumtahanah|As-Saf|Al-Jumu'ah|Al-Munafiqun|At-Taghabun|At-Talaq|At-Tahrim|Al-Mulk|Al-Qalam|Al-Haqqah|Al-Ma'arij|Nuh|Al-Jinn|Al-Muzzammil|Al-Muddaththir|Al-Qiyamah|Al-Insan|Al-Mursalat|An-Naba|An-Nazi'at|'Abasa|At-Takwir|Al-Infitar|Al-Mutaffifin|Al-Inshiqaq|Al-Buruj|At-Tariq|Al-A'la|Al-Ghashiyah|Al-Fajr|Al-Balad|Ash-Shams|Al-Layl|Ad-Duha|Ash-Sharh|At-Tin|Al-'Alaq|Al-Qadr|Al-Bayyinah|Az-Zalzalah|Al-'Adiyat|Al-Qari'ah|At-Takathur|Al-'Asr|Al-Humazah|Al-Fil|Quraysh|Al-Ma'un|Al-Kawthar|Al-Kafirun|An-Nasr|Al-Masad|Al-Ikhlas|Al-Falaq|An-Nas""".split("|")

MEANING_FIX = {
    3: "The Family of Imran", 10: "Jonah", 20: "Ta-Ha", 36: "Ya-Sin",
    37: "Those Ranged in Ranks", 38: "The Letter Sad", 50: "The Letter Qaf",
    55: "The Most Merciful", 60: "The Examined Woman", 97: "The Night of Decree",
    103: "Time",
}
ARABIC_FIX = {3: "آل عمران", 5: "المائدة", 34: "سبأ", 78: "النبأ"}

# Verses used on the Home page ("Ayah of the day") and the Prophets page.
AYAH_OF_DAY = [
    "2:45", "2:152", "2:153", "2:186", "2:201", "2:255", "2:286", "3:8", "3:139",
    "3:173", "12:87", "13:28", "14:7", "16:97", "18:10", "20:114", "25:63", "25:74",
    "28:24", "29:69", "39:53", "40:60", "41:34", "49:13", "50:16", "55:13", "64:11",
    "65:3", "93:5", "94:5-6", "112:1-4",
]
PROPHET_VERSES = [
    "7:23", "71:10-12", "11:52", "11:61", "21:69", "19:54", "12:90", "21:83",
    "11:85", "26:61-62", "34:13", "27:19", "21:87", "21:89-90", "19:30", "33:21",
]

DIAC = re.compile(r"[ؐ-ًؚ-ٰٟۖ-ۭ]")


def get(url):
    for attempt in range(4):
        try:
            r = requests.get(url, timeout=30)
            r.raise_for_status()
            return r.json()["data"]
        except Exception:
            if attempt == 3:
                raise
            time.sleep(2 * (attempt + 1))


def build_surahs():
    data = get(f"{API}/surah")
    out = []
    for s, en in zip(data, NAMES_EN):
        n = s["number"]
        ar = DIAC.sub("", s["name"].replace("سُورَةُ", "")).replace("ٱ", "ا").strip()
        out.append({
            "n": n,
            "ar": ARABIC_FIX.get(n, ar),
            "en": en,
            "meaning": MEANING_FIX.get(n, s["englishNameTranslation"]),
            "ayahs": s["numberOfAyahs"],
            "type": s["revelationType"],  # Meccan / Medinan
        })
    assert len(out) == 114
    (DATA / "surahs.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print("surahs.json:", len(out))


def expand(ref):
    s, a = ref.split(":")
    if "-" in a:
        a1, a2 = map(int, a.split("-"))
    else:
        a1 = a2 = int(a)
    return int(s), list(range(a1, a2 + 1))


def build_verses():
    out = {}
    for ref in dict.fromkeys(AYAH_OF_DAY + PROPHET_VERSES):
        s, ayahs = expand(ref)
        items = []
        for a in ayahs:
            ar, en = get(f"{API}/ayah/{s}:{a}/editions/quran-uthmani,en.sahih")
            items.append({"s": s, "a": a, "g": ar["number"], "ar": ar["text"], "en": en["text"]})
            time.sleep(0.15)
        # Strip the basmala the API prepends to ayah 1 (except Al-Fatihah).
        first = items[0]
        if first["a"] == 1 and s != 1 and DIAC.sub("", first["ar"]).startswith("بسم"):
            first["ar"] = " ".join(first["ar"].split(" ")[4:])
        out[ref] = items
        print(ref, "ok")
    (DATA / "verses.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print("verses.json:", len(out))


def build_images():
    # (source, output name, crop-focus x for portrait phones)
    for src, name in [("image_original.jpg", "bg_main"), ("background_original.jpg", "bg_prophets")]:
        im = Image.open(Path(__file__).parent / src).convert("RGB")
        for width, suffix, q in [(1920, "", 78), (960, "_mobile", 72)]:
            r = im.copy()
            r.thumbnail((width, width))
            r.save(STATIC / f"{name}{suffix}.jpg", "JPEG", quality=q, optimize=True, progressive=True)
            print(name + suffix, r.size, (STATIC / f"{name}{suffix}.jpg").stat().st_size // 1024, "KB")


if __name__ == "__main__":
    DATA.mkdir(exist_ok=True)
    STATIC.mkdir(exist_ok=True)
    build_surahs()
    build_verses()
    build_images()
