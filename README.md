# Quran & Islam Explorer

A bilingual (English / العربية), mobile-friendly Streamlit app for listening to the Quran,
understanding its surahs, and learning from the stories of the Prophets.

## What's inside

| Page | What it does |
|---|---|
| **Home** | Welcome note, animation, and an *Ayah of the Day* (authentic text + recitation, changes daily). |
| **Listen** | Full-surah recitations by handpicked Qaris; surah and Qari names in Arabic and English; *read along* with the Uthmani text plus Sahih International (English) or Tafsir al-Muyassar (Arabic). |
| **Explain** | A ~3 minute audio lesson: AI selects the key verses from the real surah text, a real Qari recites them, and a narrator explains them in Arabic or English. One MP3 you can play or download, plus a written transcript. |
| **Prophets** | 16 prophets: story, a verse from the Quran (with recitation), practical life lessons, and a "listen to the story" button. |

Language and page are kept in the URL, so links like `…/?page=prophets&lang=ar` can be shared.

## Run locally

```bash
pip install -r requirements.txt
```

```bash
cp .streamlit/secrets.toml.example .streamlit/secrets.toml   # then paste your OpenAI key
```

```bash
streamlit run main_q.py
```

Only the **Explain** page needs the OpenAI key; everything else works without it.

## Deploy on Streamlit Community Cloud

1. Push this folder to GitHub (the `.gitignore` keeps `secrets.toml` out).
2. New app → pick the repo → **Main file path:** `main_q.py`.
3. **Advanced settings → Secrets:** paste
   ```toml
   OPENAI_API_KEY = "sk-proj-..."
   ```
   Optionally add `OPENAI_MODEL = "..."` to switch models without touching code.
4. Deploy. No `packages.txt` is needed: ffmpeg comes from the `imageio-ffmpeg` pip package.

## Project layout

```
main_q.py            UI: navigation, pages, layout
content.py           ALL text (EN + AR): UI strings, reciters, prophets' stories and lessons
quran.py             Surah data, cached API calls, verse rendering
lesson.py            AI lesson planning, narration (edge-tts) and audio mixing (ffmpeg)
style.css            Theme, mobile layout, Arabic/RTL styles
data/surahs.json     114 surahs (Arabic + English names, meaning, verse count)
data/verses.json     Verses used on Home and Prophets (Uthmani text + translation)
static/              Background images (desktop + lightweight mobile versions)
tools/build_data.py  Regenerates data/ and static/ (run if you add verses or change images)
```

## How the audio lesson stays accurate

- The AI receives the **actual text** of the surah and only chooses verse numbers and writes explanations.
- Verses shown are the authentic Uthmani text (Tanzil via AlQuran.cloud); verses heard are recited by a real Qari (cdn.islamic.network), never by a synthetic voice.
- Each passage links to **Tafsir al-Muyassar** for reference.
- Lessons are cached on disk per surah and language, so repeat visits are instant and cost nothing.

## Customising

- **Wording or translations:** edit `content.py`.
- **Add a Qari:** add an entry to `RECITERS` (full surahs from mp3quran.net) or `VERSE_RECITERS` (verse-by-verse from cdn.islamic.network) in `content.py`.
- **Add a prophet or Ayah of the Day:** add it to `content.py`, add the verse reference to `tools/build_data.py`, then run `python tools/build_data.py`.
- **Background images:** replace `tools/image_original.jpg` / `tools/background_original.jpg` and run the build script.
