"""
All user-facing text lives here, in English and Arabic.
To change wording, edit this file only; the app logic doesn't need to change.
"""

# ---------------------------------------------------------------------------
# Interface strings
# ---------------------------------------------------------------------------
UI = {
    "en": {
        "app_title": "Quran & Islam Explorer",
        "nav_home": "Home",
        "nav_listen": "Listen",
        "nav_explain": "Explain",
        "nav_prophets": "Prophets",
        # Home
        "welcome": "Welcome to the Quran & Islam Explorer",
        "intro_p1": "I poured my heart into every line of code in this app. It's not just a blend of custom design and AI-powered features: it's also a journey of learning and faith for me as a Muslim.",
        "intro_p2": "With every update, I find myself deepening my understanding of the Quran and Islam.",
        "features_title": "What you'll find in this app",
        "feature_1": "🎧 <b>Curated recitations</b>: handpicked Qaris, with the full surah text to read along.",
        "feature_2": "🧠 <b>Surah audio lessons</b>: the key verses recited by a Qari and explained in Arabic or English in about 3 minutes.",
        "feature_3": "🌟 <b>Stories of the Prophets</b>: their journeys and the lessons we can live by today.",
        "intro_end": "Enough explaining, start exploring! JazakumAllahu Khairan.",
        "ayah_of_day": "Ayah of the Day",
        "start_listening": "Start listening",
        "lottie_failed": "Animation could not be loaded.",
        # Listen
        "listen_title": "Quran Recitation",
        "listen_sub": "Listen to the beautiful recitation of the Holy Quran by your favorite Qaris.",
        "select_surah": "Surah",
        "select_reciter": "Reciter",
        "verses": "verses",
        "Meccan": "Meccan",
        "Medinan": "Medinan",
        "read_along": "📖 Read along: full text and translation",
        "show_tafsir": "Show Tafsir al-Muyassar (Arabic)",
        "text_failed": "Couldn't load the surah text right now. Please try again in a moment.",
        "featured_title": "Peaceful recitations curated by me",
        "audio_note": "If the audio doesn't start, try another reciter: the recitation servers are sometimes busy.",
        # Explain
        "explain_title": "Understand a Surah",
        "explain_sub": "Choose a surah and get a short audio lesson: the app selects its key verses, a Qari recites them, and a narrator explains what they mean and how to live by them.",
        "lesson_lang": "Lesson language",
        "verse_reciter": "Qari for the verses",
        "voice": "Narrator voice",
        "voice_male": "Male",
        "voice_female": "Female",
        "generate": "🎙️ Create audio lesson",
        "step_text": "Reading the surah…",
        "step_plan": "Selecting the key verses and writing the explanation…",
        "step_voice": "Recording the narration…",
        "step_recite": "Preparing the recitation and mixing the lesson…",
        "step_done": "Your lesson is ready",
        "step_failed": "Something went wrong",
        "lesson_ready": "Audio lesson",
        "download": "⬇️ Download MP3",
        "minutes": "min",
        "key_verses": "Key verses",
        "lessons": "Lessons for our lives",
        "closing": "Closing reflection",
        "tafsir_muyassar": "Tafsir al-Muyassar",
        "no_key": "The AI lesson needs an OpenAI API key. Add `OPENAI_API_KEY` to your Streamlit secrets (see README).",
        "ai_error": "The AI service didn't respond properly. Please try again.",
        "tts_error": "The narration service is busy. Please try again in a minute.",
        "audio_error": "Couldn't download the recitation. Please try again or choose another Qari.",
        "disclaimer": "AI-generated explanation guided by classical tafsir. The verses are the authentic Uthmani text with real recitation. For deeper study, refer to trusted scholars and tafsir books such as Ibn Kathir and Al-Sa'di.",
        "lesson_cached_note": "Lessons are saved, so the next person who opens the same surah gets it instantly.",
        "voice_fallback": "The storyteller voice was unavailable, so this lesson uses the standard voice. Try again later.",
        # Prophets
        "prophets_title": "Stories of the Prophets",
        "prophets_sub": "Their journeys, a verse from the Quran, and practical lessons we can apply in our lives today. Tap a prophet to open his story.",
        "ulul_azm": "Ulul 'Azm: one of the five greatest messengers",
        "story": "Story",
        "life_lessons": "Lessons for our lives",
        "from_quran": "From the Quran",
        "listen_story": "🔊 Listen to the story",
        "pbuh": "peace be upon him",
        "footer": "Made with love for the Ummah · Quran text: Tanzil (Uthmani) via AlQuran.cloud · Translation: Sahih International",
    },
    "ar": {
        "app_title": "مستكشف القرآن والإسلام",
        "nav_home": "الرئيسية",
        "nav_listen": "التلاوة",
        "nav_explain": "الشرح",
        "nav_prophets": "الأنبياء",
        # Home
        "welcome": "مرحباً بك في مستكشف القرآن والإسلام",
        "intro_p1": "وضعتُ قلبي في كل سطر من هذا التطبيق. فهو ليس مجرد تصميم خاص وميزات مدعومة بالذكاء الاصطناعي، بل هو أيضاً رحلة تعلّم وإيمان بالنسبة لي كمسلم.",
        "intro_p2": "ومع كل تحديث أجد نفسي أتعمّق أكثر في فهم القرآن والإسلام.",
        "features_title": "ماذا ستجد في هذا التطبيق",
        "feature_1": "🎧 <b>تلاوات مختارة</b> لنخبة من القرّاء، مع نص السورة كاملاً للمتابعة أثناء الاستماع.",
        "feature_2": "🧠 <b>دروس صوتية في السور</b>: أهم الآيات بصوت قارئ، مع شرح ميسّر بالعربية أو الإنجليزية في نحو ثلاث دقائق.",
        "feature_3": "🌟 <b>قصص الأنبياء</b> والدروس التي نطبّقها في حياتنا اليوم.",
        "intro_end": "كفى شرحاً، ابدأ الاستكشاف! جزاكم الله خيراً.",
        "ayah_of_day": "آية اليوم",
        "start_listening": "ابدأ الاستماع",
        "lottie_failed": "تعذّر تحميل الرسوم المتحركة.",
        # Listen
        "listen_title": "تلاوة القرآن الكريم",
        "listen_sub": "استمع إلى تلاوات عذبة للقرآن الكريم بأصوات قرّائك المفضّلين.",
        "select_surah": "السورة",
        "select_reciter": "القارئ",
        "verses": "آية",
        "Meccan": "مكية",
        "Medinan": "مدنية",
        "read_along": "📖 تابع القراءة: نص السورة كاملاً",
        "show_tafsir": "عرض التفسير الميسّر",
        "text_failed": "تعذّر تحميل نص السورة الآن. حاول مرة أخرى بعد قليل.",
        "featured_title": "تلاوات هادئة اخترتها لكم",
        "audio_note": "إذا لم يبدأ الصوت، جرّب قارئاً آخر؛ فخوادم التلاوة تكون مزدحمة أحياناً.",
        # Explain
        "explain_title": "تدبّر سورة",
        "explain_sub": "اختر سورة واحصل على درس صوتي قصير: يختار التطبيق أهم آياتها، فيتلوها قارئ، ثم يشرح الراوي معانيها وكيف نعيش بها.",
        "lesson_lang": "لغة الدرس",
        "verse_reciter": "القارئ للآيات",
        "voice": "صوت الراوي",
        "voice_male": "رجل",
        "voice_female": "امرأة",
        "generate": "🎙️ أنشئ الدرس الصوتي",
        "step_text": "قراءة السورة…",
        "step_plan": "اختيار أهم الآيات وكتابة الشرح…",
        "step_voice": "تسجيل الشرح الصوتي…",
        "step_recite": "تجهيز التلاوة ودمج الدرس…",
        "step_done": "الدرس جاهز",
        "step_failed": "حدث خطأ",
        "lesson_ready": "الدرس الصوتي",
        "download": "⬇️ تحميل MP3",
        "minutes": "دقيقة",
        "key_verses": "أهم الآيات",
        "lessons": "دروس لحياتنا",
        "closing": "خاتمة",
        "tafsir_muyassar": "التفسير الميسّر",
        "no_key": "يحتاج الدرس إلى مفتاح OpenAI. أضف `OPENAI_API_KEY` إلى أسرار Streamlit (راجع ملف README).",
        "ai_error": "لم تستجب خدمة الذكاء الاصطناعي كما ينبغي. حاول مرة أخرى.",
        "tts_error": "خدمة الصوت مشغولة. حاول مرة أخرى بعد دقيقة.",
        "audio_error": "تعذّر تحميل التلاوة. حاول مرة أخرى أو اختر قارئاً آخر.",
        "disclaimer": "شرح مولّد بالذكاء الاصطناعي ومسترشد بكتب التفسير المعتمدة. نص الآيات بالرسم العثماني وبتلاوة حقيقية. وللتعمّق ارجع إلى العلماء الثقات وكتب التفسير مثل ابن كثير والسعدي.",
        "lesson_cached_note": "تُحفظ الدروس، فيحصل من يفتح السورة نفسها بعدك على الدرس فوراً.",
        "voice_fallback": "لم يتوفر صوت الراوي القصصي، فاستُخدم الصوت العادي في هذا الدرس. حاول مرة أخرى لاحقاً.",
        # Prophets
        "prophets_title": "قصص الأنبياء",
        "prophets_sub": "رحلاتهم، وآية من القرآن، ودروس عملية نطبّقها في حياتنا اليوم. اضغط على اسم النبي لتقرأ قصته.",
        "ulul_azm": "من أولي العزم من الرسل",
        "story": "القصة",
        "life_lessons": "دروس لحياتنا",
        "from_quran": "من القرآن الكريم",
        "listen_story": "🔊 استمع إلى القصة",
        "pbuh": "عليه السلام",
        "footer": "صُنع بحب للأمة · نص القرآن: تنزيل (الرسم العثماني) عبر AlQuran.cloud · الترجمة: Sahih International",
    },
}

LESSON_LANG_LABEL = {"ar": "العربية", "en": "English"}

# Storyteller narration (OpenAI speech model, uses your OPENAI_API_KEY).
# Other voices to try: ash, ballad, coral, echo, fable, nova, onyx, sage, shimmer, verse, alloy.
OPENAI_VOICES = {"male": "cedar", "female": "marin"}

# Free fallback voices (edge-tts), used only if the storyteller voice is unavailable.
VOICES = {
    "ar": {"male": "ar-SA-HamedNeural", "female": "ar-AE-FatimaNeural"},
    "en": {"male": "en-US-AndrewNeural", "female": "en-US-AvaNeural"},
}

# ---------------------------------------------------------------------------
# Reciters
# ---------------------------------------------------------------------------
# Full-surah recitations (mp3quran.net): your handpicked Qaris.
RECITERS = [
    {"id": "islam_sobhi", "en": "Islam Sobhi", "ar": "إسلام صبحي",
     "url": "https://server14.mp3quran.net/islam/Rewayat-Hafs-A-n-Assem/"},
    {"id": "raad_kurdi", "en": "Raad Kurdi", "ar": "رعد محمد الكردي",
     "url": "https://server6.mp3quran.net/kurdi/"},
    {"id": "hazza", "en": "Hazza Al Balushi", "ar": "هزاع البلوشي",
     "url": "https://server11.mp3quran.net/hazza/"},
    {"id": "alafasy", "en": "Mishary Alafasi", "ar": "مشاري راشد العفاسي",
     "url": "https://server8.mp3quran.net/afs/"},
    {"id": "maher", "en": "Maher Al Meaqli", "ar": "ماهر المعيقلي",
     "url": "https://server12.mp3quran.net/maher/"},
    {"id": "basit", "en": "Abdulbasit Abdulsamad", "ar": "عبد الباسط عبد الصمد",
     "url": "https://server7.mp3quran.net/basit/"},
]

# Verse-by-verse recitations (cdn.islamic.network) used inside the audio lessons.
VERSE_RECITERS = [
    {"id": "ar.alafasy", "kbps": 64, "en": "Mishary Alafasi", "ar": "مشاري راشد العفاسي"},
    {"id": "ar.mahermuaiqly", "kbps": 64, "en": "Maher Al Meaqli", "ar": "ماهر المعيقلي"},
    {"id": "ar.abdulbasitmurattal", "kbps": 64, "en": "Abdulbasit Abdulsamad", "ar": "عبد الباسط عبد الصمد"},
    {"id": "ar.husary", "kbps": 64, "en": "Mahmoud Khalil Al-Husary", "ar": "محمود خليل الحصري"},
    {"id": "ar.minshawi", "kbps": 128, "en": "Mohamed Siddiq El-Minshawi", "ar": "محمد صديق المنشاوي"},
    {"id": "ar.abdurrahmaansudais", "kbps": 64, "en": "Abdulrahman Al-Sudais", "ar": "عبد الرحمن السديس"},
]

FEATURED_VIDEOS = [
    {
        "en": "Abdullah Mosaad", "ar": "عبدالله مسعد",
        "youtube": "https://www.youtube.com/watch?v=inBCxCUW_vA",
        "desc_en": "Abdullah Mosaad is known for his deeply emotional and heart-touching Quran recitations. His voice brings serenity and peace to listeners worldwide.",
        "desc_ar": "يتميّز عبدالله مسعد بتلاواته المؤثّرة التي تلامس القلوب، ويبعث صوته السكينة والطمأنينة في نفوس المستمعين حول العالم.",
    },
    {
        "en": "Abdulrahman Almajed", "ar": "عبدالرحمن الماجد",
        "youtube": "https://www.youtube.com/watch?v=l3ZuhJOatRM",
        "desc_en": "Abdulrahman Almajed's recitation style is known for its clarity, precision, and soothing tone, making it a perfect choice for deep spiritual reflection.",
        "desc_ar": "تتميّز تلاوة عبدالرحمن الماجد بالوضوح والإتقان والنبرة الهادئة، مما يجعلها خياراً مثالياً للتدبّر والتأمّل.",
    },
]

# ---------------------------------------------------------------------------
# Stories of the Prophets (approximate chronological order)
# `verse` keys refer to data/verses.json (authentic text pulled from the API).
# ---------------------------------------------------------------------------
PROPHETS = [
    {
        "en": "Adam", "ar": "آدم", "icon": "🌱", "ulul_azm": False, "verse": "7:23",
        "title_en": "The Father of Humanity", "title_ar": "أبو البشر",
        "story_en": "Allah created Adam from clay, breathed life into him, taught him the names of all things, and commanded the angels to prostrate to him. Iblis refused out of arrogance. Adam and Hawwa lived in Paradise until Shaytan tempted them to eat from the forbidden tree. They did not argue or blame others: they turned to Allah in sincere repentance, and He forgave them and sent them to earth as its stewards.",
        "story_ar": "خلق الله آدم من طين، ونفخ فيه من روحه، وعلّمه الأسماء كلها، وأمر الملائكة بالسجود له فسجدوا إلا إبليس أبى واستكبر. سكن آدم وحواء الجنة حتى وسوس لهما الشيطان فأكلا من الشجرة. لم يجادلا ولم يلقيا اللوم على غيرهما، بل تابا إلى الله توبة صادقة، فتاب الله عليهما وأهبطهما إلى الأرض ليكونا خليفة فيها.",
        "lessons_en": [
            "Everyone makes mistakes; the best response is to admit them and return to Allah quickly.",
            "It was arrogance, not a single slip, that ruined Iblis. Stay humble.",
            "Knowledge is an honor from Allah, so keep learning.",
        ],
        "lessons_ar": [
            "كل إنسان يخطئ، وخير ما نفعله أن نعترف بالخطأ ونسارع بالتوبة.",
            "سقوط إبليس كان بسبب الكِبر، فلنحذر منه ولنبقَ متواضعين.",
            "العلم تكريم من الله للإنسان، فلنحرص على التعلّم دائماً.",
        ],
    },
    {
        "en": "Nuh", "ar": "نوح", "icon": "🚢", "ulul_azm": True, "verse": "71:10-12",
        "title_en": "The First Messenger to Mankind", "title_ar": "أول رسول إلى أهل الأرض",
        "story_en": "Nuh called his people to worship Allah alone for 950 years, by night and by day, in public and in private. Only a few believed, and the rest mocked him. Allah commanded him to build the Ark, and when the flood came, the believers were saved while those who rejected, including his own son, were drowned. The Ark came to rest on Mount Judi, and humanity began anew.",
        "story_ar": "دعا نوح قومه إلى عبادة الله وحده تسعمائة وخمسين عاماً، ليلاً ونهاراً، سراً وجهاراً، فلم يؤمن معه إلا قليل، وسخر منه الباقون. أمره الله ببناء السفينة، فلما جاء الطوفان نجّى الله المؤمنين وأغرق المكذّبين ومنهم ابنه، واستوت السفينة على الجودي لتبدأ البشرية صفحة جديدة.",
        "lessons_en": [
            "Keep doing good even when results are slow. Success lies in sincerity and effort.",
            "Salvation comes through faith and deeds, not family ties, and guidance is from Allah alone.",
            "Seeking forgiveness (istighfar) opens the doors of rain, provision and blessings.",
        ],
        "lessons_ar": [
            "استمر في الخير ولو تأخرت النتائج، فالعبرة بالإخلاص وبذل الجهد.",
            "النجاة بالإيمان والعمل لا بالنسب، والهداية بيد الله وحده.",
            "الاستغفار يفتح أبواب المطر والرزق والبركة.",
        ],
    },
    {
        "en": "Hud", "ar": "هود", "icon": "🌪️", "ulul_azm": False, "verse": "11:52",
        "title_en": "Messenger to the People of 'Ad", "title_ar": "رسول الله إلى عاد",
        "story_en": "The people of 'Ad were blessed with great strength, tall buildings and fertile lands, but they grew arrogant and asked, \"Who is mightier than us?\" Hud called them to worship Allah, seek His forgiveness and be grateful. They mocked him and refused. A cloud appeared that they thought would bring rain, but it was a furious wind that raged for seven nights and eight days. Hud and the believers were saved.",
        "story_ar": "أنعم الله على قوم عاد بالقوة والمباني العالية والأرض الخصبة، لكنهم تكبّروا وقالوا: من أشد منا قوة؟ دعاهم هود إلى عبادة الله والاستغفار وشكر النعمة، فسخروا منه وأعرضوا. فرأوا سحاباً ظنّوه مطراً، فإذا هو ريح عاتية سلّطها الله عليهم سبع ليالٍ وثمانية أيام، ونجّى الله هوداً والذين آمنوا معه.",
        "lessons_en": [
            "Strength, money and status are blessings to be grateful for, not reasons for arrogance.",
            "Repentance adds strength to your strength. True power comes from obeying Allah.",
            "Rely on Allah when you stand for the truth, even if you stand alone.",
        ],
        "lessons_ar": [
            "القوة والمال والمكانة نِعَم تستوجب الشكر، لا أسباباً للتكبّر.",
            "التوبة تزيدك قوة إلى قوتك، فالقوة الحقيقية في طاعة الله.",
            "توكّل على الله حين تقف مع الحق ولو كنت وحدك.",
        ],
    },
    {
        "en": "Salih", "ar": "صالح", "icon": "🐪", "ulul_azm": False, "verse": "11:61",
        "title_en": "Messenger to the People of Thamud", "title_ar": "رسول الله إلى ثمود",
        "story_en": "Thamud carved beautiful homes out of the mountains. When Salih called them to Allah, they demanded a miracle, so Allah brought forth a she-camel from the rock as a sign, and commanded them to share the water with her and not harm her. Instead, they plotted and killed her. The whole nation, which approved of the crime, was seized by a mighty blast, while Salih and the believers were saved.",
        "story_ar": "نحتت ثمود من الجبال بيوتاً فارهة. فلما دعاهم صالح إلى الله طلبوا آية، فأخرج الله لهم ناقة من الصخر، وأمرهم أن يقتسموا الماء معها وألا يمسّوها بسوء. لكنهم تآمروا وعقروها، فأخذت الصيحة القوم جميعاً لأنهم رضوا بفعل من عقرها، ونجّى الله صالحاً والذين آمنوا معه.",
        "lessons_en": [
            "Respect Allah's signs and limits; miracles don't help a heart that refuses to listen.",
            "Approving of wrongdoing makes you a partner in it, so speak up against injustice.",
            "Allah is near and answers those who turn back to Him.",
        ],
        "lessons_ar": [
            "عظّم آيات الله وحدوده، فالمعجزات لا تنفع قلباً يرفض الحق.",
            "الرضا بالمنكر مشاركة فيه، فلا تسكت عن الظلم.",
            "إن الله قريب مجيب لمن رجع إليه.",
        ],
    },
    {
        "en": "Ibrahim", "ar": "إبراهيم", "icon": "🔥", "ulul_azm": True, "verse": "21:69",
        "title_en": "The Friend of Allah", "title_ar": "خليل الرحمن",
        "story_en": "Ibrahim grew up among idol worshippers and used reason to reach the truth: the stars, the moon and the sun all set, so none of them can be God. He broke his people's idols to show they could not even defend themselves, and he was thrown into a huge fire, but Allah made the fire cool and safe for him. By Allah's command he left his wife Hajar and baby Ismail in the barren valley of Makkah, later built the Kaaba with Ismail, and was tested with the command to sacrifice his son. He obeyed, and Allah ransomed Ismail with a great sacrifice.",
        "story_ar": "نشأ إبراهيم بين قوم يعبدون الأصنام، فاستعمل عقله ليصل إلى الحق: الكواكب والقمر والشمس كلها تأفل، فلا يمكن أن تكون آلهة. حطّم أصنام قومه ليبيّن أنها لا تدفع عن نفسها شيئاً، فألقوه في نار عظيمة، فجعلها الله برداً وسلاماً عليه. وترك زوجته هاجر وابنه الرضيع إسماعيل في وادي مكة القاحل بأمر الله، ثم بنى الكعبة مع إسماعيل، وابتُلي بالأمر بذبح ابنه فامتثل، ففداه الله بذبح عظيم.",
        "lessons_en": [
            "Use your mind to seek the truth. Faith and reason go together.",
            "Complete trust in Allah can turn the greatest danger into safety.",
            "Put Allah's command before what you love most, and He will give you better.",
            "Make dua for your children and future generations, as Ibrahim did.",
        ],
        "lessons_ar": [
            "استعمل عقلك في طلب الحق، فالإيمان والعقل لا يتعارضان.",
            "التوكّل الصادق على الله يحوّل أعظم الأخطار إلى أمان.",
            "قدّم أمر الله على أحب الأشياء إليك يعوّضك الله خيراً منها.",
            "ادعُ لأبنائك وذريتك كما كان إبراهيم يدعو لهم.",
        ],
    },
    {
        "en": "Ismail", "ar": "إسماعيل", "icon": "💧", "ulul_azm": False, "verse": "19:54",
        "title_en": "True to His Promise", "title_ar": "صادق الوعد",
        "story_en": "As a baby, Ismail was left with his mother Hajar in the valley of Makkah. When their water ran out, Hajar ran seven times between the hills of Safa and Marwa searching for help, until Allah caused the spring of Zamzam to gush forth. When Ismail grew up and his father told him about the dream of sacrifice, he urged his father to carry out Allah's command and promised to be patient. Later he helped his father raise the foundations of the Kaaba.",
        "story_ar": "تُرك إسماعيل رضيعاً مع أمه هاجر في وادي مكة، فلما نفد الماء سعت هاجر بين الصفا والمروة سبع مرات تبحث عن النجدة، حتى فجّر الله لهما ماء زمزم. ولما كبر إسماعيل وأخبره أبوه برؤيا الذبح، طلب من أبيه أن يمضي لأمر الله ووعده بالصبر. ثم شارك أباه في رفع قواعد الكعبة.",
        "lessons_en": [
            "Take action like Hajar and trust Allah with the result. Her effort became a rite of Hajj.",
            "Keep your promises. Allah praised Ismail for being true to his word.",
            "Honor your parents and support them in what pleases Allah.",
        ],
        "lessons_ar": [
            "خذ بالأسباب كما فعلت هاجر وتوكّل على الله في النتائج، فقد صار سعيها شعيرة من شعائر الحج.",
            "أوفِ بوعدك، فقد أثنى الله على إسماعيل بأنه كان صادق الوعد.",
            "برّ والديك وأعِنهما على طاعة الله.",
        ],
    },
    {
        "en": "Yusuf", "ar": "يوسف", "icon": "🌙", "ulul_azm": False, "verse": "12:90",
        "title_en": "The Best of Stories", "title_ar": "أحسن القصص",
        "story_en": "Jealous of their father's love for him, Yusuf's brothers threw him into a well. He was sold as a slave in Egypt, refused the advances of the minister's wife, saying \"I seek refuge in Allah\", and was unjustly imprisoned for years. In prison he called others to Allah and interpreted dreams, until the king made him the trusted guardian of Egypt's storehouses. When famine brought his brothers to him, he forgave them completely: \"No blame upon you today.\"",
        "story_ar": "حسد إخوةُ يوسف أخاهم على حب أبيهم له فألقوه في البئر، ثم بِيع عبداً في مصر، وراودته امرأة العزيز فاستعصم وقال: معاذ الله، فسُجن ظلماً بضع سنين. وفي السجن دعا إلى الله وفسّر الرؤى، حتى جعله الملك أميناً على خزائن مصر. ولما جاءه إخوته في سنوات القحط عفا عنهم عفواً كاملاً وقال: لا تثريب عليكم اليوم.",
        "lessons_en": [
            "Jealousy can tear families apart. Guard your heart, and treat children fairly.",
            "Integrity when no one is watching is true strength.",
            "Allah's plan unfolds over years: the well and the prison led to the palace.",
            "Forgive when you have the power to take revenge.",
        ],
        "lessons_ar": [
            "الحسد يفرّق الأسر، فطهّر قلبك واعدل بين أبنائك.",
            "العفة والأمانة حين لا يراك أحد هي القوة الحقيقية.",
            "تدبير الله يتجلّى مع الأيام: البئر والسجن كانا طريقاً إلى القصر.",
            "اعفُ عند المقدرة.",
        ],
    },
    {
        "en": "Ayyub", "ar": "أيوب", "icon": "🤲", "ulul_azm": False, "verse": "21:83",
        "title_en": "The Model of Patience", "title_ar": "رمز الصبر",
        "story_en": "Ayyub was a prophet blessed with wealth, children and good health. Allah tested him by taking all of it away and afflicting him with a long illness. Through years of hardship he never complained about Allah; he only called upon Him with humble words. Allah answered him, told him to strike the ground with his foot so that a cool spring would heal him, and restored his family to him along with as many more.",
        "story_ar": "كان أيوب نبياً أنعم الله عليه بالمال والولد والعافية، فابتلاه الله بفقدها جميعاً وبمرض طويل. وعلى مدى سنوات من البلاء لم يشكُ ربه، بل دعاه بأدب وتضرّع. فاستجاب الله له، وأمره أن يضرب الأرض برجله فنبعت عين باردة كان فيها شفاؤه، وردّ عليه أهله ومثلهم معهم.",
        "lessons_en": [
            "Tests are not a sign of Allah's anger. Even the best of people are tested.",
            "Complain to Allah, not about Allah.",
            "Patience is rewarded: after hardship comes relief.",
        ],
        "lessons_ar": [
            "البلاء ليس علامة على غضب الله، فأحب الخلق إليه يُبتلَون.",
            "اشكُ همّك إلى الله، ولا تشكُ الله إلى الناس.",
            "الصبر عاقبته الفرج، فإن مع العسر يسراً.",
        ],
    },
    {
        "en": "Shu'ayb", "ar": "شعيب", "icon": "⚖️", "ulul_azm": False, "verse": "11:85",
        "title_en": "Champion of Honest Trade", "title_ar": "خطيب الأنبياء",
        "story_en": "Shu'ayb was sent to the people of Madyan, who were known for cheating in weights and measures, short-changing people and blocking travellers' roads. He called them to worship Allah, to give full measure and to stop spreading corruption in the land. They mocked him and objected that his prayer should have nothing to do with how they made their money. When they persisted, a terrible earthquake seized them, while Shu'ayb and the believers were saved.",
        "story_ar": "أُرسل شعيب إلى أهل مدين، وكانوا يطفّفون المكيال والميزان ويبخسون الناس أشياءهم ويقطعون الطريق. فدعاهم إلى عبادة الله والوفاء بالكيل وترك الفساد في الأرض، فسخروا منه واستنكروا أن تتدخّل صلاته في طريقة كسبهم للمال. فلما أصرّوا أخذتهم الرجفة، ونجّى الله شعيباً والذين آمنوا معه.",
        "lessons_en": [
            "Honesty in business is part of faith. Never cheat in work, trade or exams.",
            "Faith is not only rituals; it shapes how we earn and spend money.",
            "A little halal income is better than a lot of haram.",
        ],
        "lessons_ar": [
            "الأمانة في البيع والعمل جزء من الإيمان، فلا تغشّ في تجارة أو عمل أو امتحان.",
            "الدين ليس عبادات فقط، بل يضبط طريقة كسبنا وإنفاقنا للمال.",
            "القليل الحلال خير من الكثير الحرام.",
        ],
    },
    {
        "en": "Musa", "ar": "موسى", "icon": "🌊", "ulul_azm": True, "verse": "26:61-62",
        "title_en": "The One Allah Spoke To", "title_ar": "كليم الله",
        "story_en": "Pharaoh was killing the newborn boys of the Children of Israel, so Allah inspired Musa's mother to place him in a basket on the Nile. He was raised in Pharaoh's own palace and returned to his mother to nurse. As a young man he fled to Madyan, where he helped two women water their flock and married one of them. On his way back, Allah spoke to him at Mount Tur and sent him with his brother Harun to Pharaoh. When Pharaoh's army trapped the believers at the sea, Musa declared with certainty that his Lord was with him, and Allah split the sea.",
        "story_ar": "كان فرعون يقتل مواليد بني إسرائيل من الذكور، فأوحى الله إلى أم موسى أن تلقيه في التابوت في اليمّ، فتربّى في قصر فرعون نفسه، وردّه الله إلى أمه لترضعه. ولما شبّ خرج إلى مدين، فسقى لامرأتين وتزوّج إحداهما. وفي طريق عودته كلّمه الله عند جبل الطور وأرسله مع أخيه هارون إلى فرعون. ولما أدرك جيشُ فرعون المؤمنين عند البحر، قال موسى بيقين إن ربه معه سيهديه، فانفلق البحر بإذن الله.",
        "lessons_en": [
            "When there seems to be no way out, Allah opens one. Trust Him completely.",
            "Speak truth to power with wisdom and gentle words, as Allah told Musa and Harun.",
            "Ask Allah for courage and good companions: Musa asked for his brother Harun as a helper.",
            "Stay humble when seeking knowledge, as Musa was with Al-Khidr.",
        ],
        "lessons_ar": [
            "حين تُغلق الأبواب كلها يفتح الله باباً، فثق به ثقة كاملة.",
            "قل الحق بحكمة وقول ليّن، كما أمر الله موسى وهارون مع فرعون.",
            "اسأل الله الشجاعة والصحبة الصالحة، فقد طلب موسى أخاه هارون وزيراً له.",
            "تواضع في طلب العلم كما فعل موسى مع الخضر.",
        ],
    },
    {
        "en": "Dawud", "ar": "داود", "icon": "🛡️", "ulul_azm": False, "verse": "34:13",
        "title_en": "The Grateful King", "title_ar": "الملك الشاكر",
        "story_en": "As a young soldier in Talut's army, Dawud defeated the giant Jalut (Goliath). Allah gave him kingship, wisdom and the Zabur (Psalms). The mountains and the birds glorified Allah with him, and Allah softened iron in his hands so he could make armor. Although he was a king, he ate from the work of his own hands, and he fasted every other day: the fast the Prophet ﷺ described as the most beloved to Allah.",
        "story_ar": "كان داود جندياً شاباً في جيش طالوت فقتل جالوت، فآتاه الله الملك والحكمة والزبور. وكانت الجبال والطير تسبّح معه، وألان الله له الحديد فكان يصنع الدروع. ومع أنه كان ملكاً كان يأكل من عمل يده، وكان يصوم يوماً ويفطر يوماً، وهو الصيام الذي وصفه النبي ﷺ بأنه أحب الصيام إلى الله.",
        "lessons_en": [
            "Courage comes from faith, not from size or numbers.",
            "Earn your living honestly, through your own effort.",
            "Gratitude is shown through actions, not just words.",
            "Judge fairly between people and don't follow your desires.",
        ],
        "lessons_ar": [
            "الشجاعة تنبع من الإيمان لا من الحجم أو العدد.",
            "اكسب رزقك بجهدك وعملك الحلال.",
            "الشكر يكون بالعمل لا بالكلام فقط.",
            "احكم بين الناس بالعدل ولا تتّبع الهوى.",
        ],
    },
    {
        "en": "Sulaiman", "ar": "سليمان", "icon": "🐜", "ulul_azm": False, "verse": "27:19",
        "title_en": "The Wise King", "title_ar": "النبي الملك",
        "story_en": "Sulaiman inherited prophethood and wisdom from his father Dawud, and Allah gave him a kingdom like no other: the wind, the jinn and the birds were made subject to him, and he understood the speech of birds and animals. When he heard an ant warn its colony not to be crushed by his army, he smiled and thanked Allah. The hoopoe brought him news of the Queen of Sheba, whose people worshipped the sun. Sulaiman verified the report and invited her to Islam, and she submitted to Allah. Whenever he saw a blessing, he said it was from his Lord's favor, to test whether he would be grateful.",
        "story_ar": "ورث سليمان النبوة والحكمة عن أبيه داود، وآتاه الله ملكاً لا ينبغي لأحد من بعده، فسخّر له الريح والجن والطير، وعلّمه منطق الطير. ولما سمع نملة تحذّر قومها من أن يحطمهم جيشه تبسّم ضاحكاً وشكر الله. وجاءه الهدهد بخبر ملكة سبأ وقومها الذين يسجدون للشمس، فتثبّت سليمان من الخبر ودعاها إلى الإسلام فأسلمت لله. وكان كلما رأى نعمة قال إنها من فضل ربه ليبلوه أيشكر أم يكفر.",
        "lessons_en": [
            "Power and wealth are tests of gratitude.",
            "Show mercy even to the smallest creatures.",
            "Verify news before acting on it or sharing it.",
        ],
        "lessons_ar": [
            "الملك والمال اختبار للشكر.",
            "ارحم حتى أصغر المخلوقات.",
            "تثبّت من الأخبار قبل أن تبني عليها أو تنشرها.",
        ],
    },
    {
        "en": "Yunus", "ar": "يونس", "icon": "🐋", "ulul_azm": False, "verse": "21:87",
        "title_en": "The Companion of the Whale", "title_ar": "ذو النون",
        "story_en": "Yunus called his people to Allah, but when they kept rejecting him, he left them in anger before Allah permitted him to. He boarded an overloaded ship; in the storm, lots were cast, and he was thrown into the sea, where a whale swallowed him. In the darkness of the night, the sea and the whale's belly, he called out: \"There is no god but You, glory be to You, I was among the wrongdoers.\" Allah saved him, and his people, a hundred thousand or more, believed.",
        "story_ar": "دعا يونس قومه إلى الله، فلما أصرّوا على التكذيب خرج مغاضباً قبل أن يأذن الله له، فركب سفينة مشحونة، فاضطربت فاقترعوا فوقعت القرعة عليه، فأُلقي في البحر فالتقمه الحوت. وفي ظلمات الليل والبحر وبطن الحوت نادى: لا إله إلا أنت سبحانك إني كنت من الظالمين. فنجّاه الله، وآمن قومه وكانوا مائة ألف أو يزيدون.",
        "lessons_en": [
            "Don't give up on people or abandon your responsibilities out of frustration.",
            "No darkness is too deep for dua. The Prophet ﷺ said that no Muslim calls with Yunus's words for anything except that Allah answers him (Tirmidhi).",
            "Admitting your mistake is the key to relief.",
        ],
        "lessons_ar": [
            "لا تيأس من الناس ولا تترك مسؤوليتك بسبب الإحباط.",
            "لا توجد ظلمة أعمق من أن يصلها الدعاء، وقد أخبر النبي ﷺ أنه ما دعا بدعوة ذي النون مسلم في شيء إلا استجاب الله له (رواه الترمذي).",
            "الاعتراف بالخطأ مفتاح الفرج.",
        ],
    },
    {
        "en": "Zakariya & Yahya", "ar": "زكريا ويحيى", "icon": "🕯️", "ulul_azm": False, "verse": "21:89-90",
        "title_en": "Never Stop Making Dua", "title_ar": "لا تيأس من الدعاء",
        "story_en": "Zakariya was an old man whose wife was barren. When he saw the provision Allah sent to Maryam, who was in his care, he called upon his Lord quietly, asking for a righteous heir. Allah gave him the glad tidings of Yahya, a name given to no one before him. Yahya was given wisdom while still a child; he was gentle, pure, devoted to Allah and dutiful to his parents.",
        "story_ar": "كان زكريا شيخاً كبيراً وامرأته عاقراً، فلما رأى رزق الله الذي يأتي مريم وهي في كفالته، نادى ربه نداءً خفياً يسأله ذرية طيبة. فبشّره الله بيحيى، ولم يجعل له من قبل سمياً. ونشأ يحيى وقد آتاه الله الحكم صبياً، فكان حنوناً طاهراً تقياً باراً بوالديه.",
        "lessons_en": [
            "Nothing is impossible for Allah, so never stop making dua.",
            "Call on Allah quietly and humbly; He hears the whisper of the heart.",
            "Seeing Allah's blessings on others should inspire hope, not envy.",
        ],
        "lessons_ar": [
            "لا شيء مستحيل على الله، فلا تتوقف عن الدعاء.",
            "ادعُ الله بخشوع وخفية، فهو يسمع همس القلوب.",
            "رؤية نِعَم الله على غيرك تبعث الأمل لا الحسد.",
        ],
    },
    {
        "en": "Isa", "ar": "عيسى", "icon": "✨", "ulul_azm": True, "verse": "19:30",
        "title_en": "Al-Masih, Son of Maryam", "title_ar": "المسيح ابن مريم",
        "story_en": "Allah chose Maryam above the women of the worlds, and she gave birth to Isa without a father, by Allah's word \"Be\". When her people accused her, the baby Isa spoke from the cradle, declaring that he was the servant of Allah, given the Scripture and made a prophet. By Allah's permission he healed the blind and the leper and brought the dead back to life, and he was given the Injil. His enemies plotted to kill him, but they neither killed him nor crucified him: Allah raised him up to Himself, and he will return before the Last Day.",
        "story_ar": "اصطفى الله مريم على نساء العالمين، فولدت عيسى من غير أب بكلمة الله: كن. ولما اتهمها قومها تكلّم عيسى في المهد، فأعلن أنه عبد الله آتاه الكتاب وجعله نبياً. وكان بإذن الله يبرئ الأكمه والأبرص ويحيي الموتى، وآتاه الله الإنجيل. وتآمر أعداؤه على قتله، وما قتلوه وما صلبوه، بل رفعه الله إليه، وسينزل قبل قيام الساعة.",
        "lessons_en": [
            "Allah's power is beyond cause and effect. Trust Him when things seem impossible.",
            "True greatness is servitude to Allah: Isa's first words were \"I am the servant of Allah.\"",
            "Honor your mother: Isa described himself as dutiful to his mother.",
            "Maryam teaches us chastity and complete trust in Allah during hardship.",
        ],
        "lessons_ar": [
            "قدرة الله فوق الأسباب، فثق به حين تبدو الأمور مستحيلة.",
            "العظمة الحقيقية في العبودية لله، فأول ما قاله عيسى: إني عبد الله.",
            "برّ أمك، فقد وصف عيسى نفسه بأنه برّ بوالدته.",
            "تعلّمنا مريم العفة والتوكّل التام على الله في الشدائد.",
        ],
    },
    {
        "en": "Muhammad ﷺ", "ar": "محمد ﷺ", "icon": "🕋", "ulul_azm": True, "verse": "33:21",
        "title_en": "The Seal of the Prophets", "title_ar": "خاتم النبيين",
        "story_en": "Born in Makkah in the Year of the Elephant and orphaned young, Muhammad ﷺ was known as Al-Sadiq Al-Amin: the Truthful, the Trustworthy. At forty, Jibril came to him in the Cave of Hira with the first revelation: \"Read!\" For thirteen years he called people to Allah in Makkah despite persecution, then migrated to Madinah, where he built a community of faith, brotherhood and justice. When he returned to Makkah victorious, he forgave those who had persecuted him. He conveyed the message in full and passed away in Madinah, leaving the Quran and his Sunnah as guidance for all humanity.",
        "story_ar": "وُلد محمد ﷺ في مكة عام الفيل، ونشأ يتيماً، وعُرف بين قومه بالصادق الأمين. وفي الأربعين من عمره نزل عليه جبريل في غار حراء بأول الوحي: اقرأ. ودعا إلى الله في مكة ثلاث عشرة سنة رغم الأذى، ثم هاجر إلى المدينة فبنى مجتمعاً قائماً على الإيمان والأخوّة والعدل. ولما دخل مكة فاتحاً عفا عمّن آذوه. وبلّغ الرسالة كاملة، وتوفي في المدينة تاركاً القرآن والسنة هدىً للبشرية جمعاء.",
        "lessons_en": [
            "Be known for honesty and trustworthiness. Character speaks before words.",
            "Show mercy and forgiveness, even to those who wronged you.",
            "The most beloved deeds to Allah are the consistent ones, even if small (Bukhari & Muslim).",
            "Follow his example in everything: worship, family life, work and dealing with people.",
        ],
        "lessons_ar": [
            "كن معروفاً بالصدق والأمانة، فالأخلاق تسبق الكلام.",
            "ارحم واعفُ حتى عمّن أساء إليك.",
            "أحب الأعمال إلى الله أدومها وإن قلّ (متفق عليه).",
            "اقتدِ به ﷺ في كل شيء: في العبادة والأسرة والعمل ومعاملة الناس.",
        ],
    },
]

AYAH_OF_DAY = [
    "2:45", "2:152", "2:153", "2:186", "2:201", "2:255", "2:286", "3:8", "3:139",
    "3:173", "12:87", "13:28", "14:7", "16:97", "18:10", "20:114", "25:63", "25:74",
    "28:24", "29:69", "39:53", "40:60", "41:34", "49:13", "50:16", "55:13", "64:11",
    "65:3", "93:5", "94:5-6", "112:1-4",
]
