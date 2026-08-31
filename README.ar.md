# WorldLang

<p align="center">
  <img src="images/world.png" alt="شعار WorldLang" width="200">
</p>

<p align="center">
  <a href="README.md">English</a> |
  <strong>العربية</strong> |
  <a href="README.fr.md">Français</a> |
  <a href="README.es.md">Español</a> |
  <a href="README.de.md">Deutsch</a> |
  <a href="README.zh.md">中文</a>
</p>

**لغة برمجة متعددة اللغات تتيح لك كتابة وتنفيذ الكود بلغتك الأم.**

<p align="center">
  <a href="https://github.com/ZiadRabea/WorldLang/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/ZiadRabea/WorldLang" alt="رخصة GitHub">
  </a>
  <br>
  <a href="https://marketplace.visualstudio.com/items?itemName=worldlangteam.WorldEn">
    <img src="https://vsmarketplacebadges.dev/version-short/worldlangteam.WorldEn.svg" alt="امتداد VSCode">
  </a>
  <br>
  <a href="https://www.researchgate.net/publication/377782413_A_Multilingual_Approach_with_Built-in_Code_Translation_and_Dynamic_Keyword_Importation">
    <img src="https://img.shields.io/badge/ResearchGate-preprint-brightgreen" alt="ResearchGate">
  </a>
</p>

**الموارد والروابط:**

* 📖 **[التوثيق الرسمي](https://ziadrabea.github.io/WorldDocs)**
  * 🚀 [البدء](https://ziadrabea.github.io/WorldDocs/installation.html)
  * 📚 [مرجع اللغة](https://ziadrabea.github.io/WorldDocs/features.html)
  * 🌍 [اللغات المدعومة](https://ziadrabea.github.io/WorldDocs/languages.html)
  * 🤝 [دليل المساهمة](https://ziadrabea.github.io/WorldDocs/guide.html)
* 🌐 **[الموقع الرسمي](https://ziadrabea.github.io/worldlanguage)**
* 💬 **[انضم إلى المجتمع](https://flow.daisyscript.com)**
* 🔬 **[ورقة بحثية (ResearchGate)](https://www.researchgate.net/publication/377782413_A_Multilingual_Approach_with_Built-in_Code_Translation_and_Dynamic_Keyword_Importation)**
* 🧩 **[امتداد WorldLangEN لـ VS Code](https://marketplace.visualstudio.com/items?itemName=worldlangteam.WorldEn)**
* 👤 **المشرف:** Ziad Rabea ([LinkedIn](https://www.linkedin.com/in/ziadrabea/) | [Email](mailto:zidr2005@gmail.com))

WorldLang هو مترجم مفتوح المصدر مبني بلغة Python يزيل حواجز اللغة في البرمجة. بدلاً من حفظ الكلمات المفتاحية الإنجليزية، تكتب الكود باستخدام بنية جملتك المحلية — العربية، الفرنسية، اليابانية، وأكثر من 18 لغة أخرى — ويقوم المحرك بعملية رمزية وتنفيذها عبر خط أنابيب مخصص: Lexer → Parser → Runtime.

> **اللغات المدعومة: 21** — العربية، الصينية، الهولندية، الإنجليزية، الفرنسية، الألمانية، الإندونيسية، الإيطالية، اليابانية، الكازاخية، الكورية، الفارسية، البولندية، البرتغالية، الرومانية، الروسية، الإسبانية، التركية، الأوكرانية، الأردوية، الفيتنامية.

---

## جدول المحتويات

- [الميزات](#الميزات)
- [المتطلبات](#المتطلبات)
- [التثبيت](#التثبيت)
- [الاستخدام](#الاستخدام)
- [مثال على الكود](#مثال-على-الكود)
- [المكتبات المدمجة](#المكتبات-المدمجة)
- [البنية](#البنية)
- [إدارة اللغة والمكتبات](#إدارة-اللغة-والمكتبات)
- [المساهمة](#المساهمة)
- [الرخصة](#الرخصة)

---

## الميزات

- **البرمجة بلغتك المحلية** — اكتب الكود باستخدام الكلمات المفتاحية للغة التي اخترتها.
- **21 حزمة لغة** مرفقة في `data/` كجداول كلمات مفتاحية بصيغة JSON.
- **مطابقة ديناميكية للم الكلمات المفتاحية** — يقوم الـ lexer بمطابقة الكلمات المفتاحية المحلية مع الرموز العامة أثناء التشغيل.
- **مترجم متكامل بالكامل** — المتغيرات، الدوال، التكرار الشروطي، الحلقات، الشروط، القوائم، القواميس، والحسابات الرياضية.
- **الأجهزة والروبوتات** — اتصال تسلسلي مع وحدات التحكم الدقيقة (مثل Arduino).
- **الصوت** — تحويل النص إلى كلام والتعرف على الصوت.
- **المكتبات المدمجة** — معالجة الصور، الرسوم البيانية، الأرقام العشوائية، نظام الملفات، والمزيد.
- **الذكاء الاصطناعي التوليدي** — تكامل اختياري مع Google Gemini.
- **إدارة المكتبات والامتدادات** — جلب مكتبات وامتدادات `.world` مباشرة من الإنترنت.

---

## المتطلبات

- **Python 3.12+**
- **Windows أو macOS أو Linux**

الحزم الأساسية المطلوبة (انظر [التثبيت](#التثبيت)):

| الحزمة | تُستخدم لـ |
|---------|----------|
| `requests` | تنزيل حزم اللغات والمكتبات والامتدادات |
| `Pillow` | معالجة الصور (`_builtins/Image.py`) |
| `matplotlib` و `numpy` | الرسوم البيانية (`_builtins/Graph.py`) |
| `pyautogui` | التحكم بالماوس/لوحة المفاتيح (`_builtins/Controls.py`) |
| `pyserial` | الاتصال التسلسلي/بالأجهزة (`_builtins/Serial.py`) |
| `pyttsx3` | تحويل النص إلى كلام (`_builtins/Speech.py`) |
| `SpeechRecognition` | التعرف على الصوت (`_builtins/Speech.py`) |
| `google-generativeai` | الذكاء الاصطناعي التوليدي (`_builtins/GenAI.py`) |
| `rich` | عرض Markdown لمخرجات الذكاء الاصطناعي (`_builtins/GenAI.py`) |

> `requests` فقط هو المطلوب للوظائف الأساسية. الحزم الأخرى مطلوبة فقط للمكتبات المدمجة الاختيارية المذكورة أعلاه.

---

## التثبيت

```bash
# 1. استنساخ المستودع
git clone https://github.com/ZiadRabea/WorldLang.git
cd WorldLang

# 2. (موصى به) إنشاء وتفعيل بيئة افتراضية
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS / Linux:
source venv/bin/activate

# 3. تثبيت التبعيات
pip install requests Pillow matplotlib numpy pyautogui pyserial pyttsx3 SpeechRecognition rich
```

لتفعيل ميزات الذكاء الاصطناعي، تحتاج أيضًا إلى:

```bash
pip install google-generativeai
```

---

## الاستخدام

يأتي المترجم كـ REPL (حلقة قراءة-تقييم-طباعة). لتشغيله:

```bash
python bin/World.py
```

يظهر موجه أوامر:

```
World >>
```

اكتب برنامجًا واضغط Enter لتنفيذه. الأوامر الخاصة عند الموجه:

| الأمر       | الإجراء                                                        |
|------------|---------------------------------------------------------------|
| `libman`   | تشغيل مدير المكتبات (تنزيل مكتبات `.world`)                  |
| `langman`  | تشغيل مدير اللغات (تنزيل/تبديل حزم اللغات)                  |
| `extman`   | تشغيل مدير الامتدادات (تنزيل الامتدادات)                     |

`WorldLang` عربي بشكل افتراضي. يتم تحميل الكلمات المفتاحية العربية من `bin/keywords.json`. قم بالتبديل أو إضافة لغات عبر المدير `langman`.

---

## مثال على كود

**حاسبة مضروب** تكرارية مكتوبة بالكامل باستخدام الكلمات المفتاحية العربية:

```world
# حاسبة المضروب
متغير الرقم = عدد_صحيح(استقبل("أدخل رقماً"))

دالة مضروب(رقم)
    اذا رقم == 1 او رقم == 0 نفذ ارجاع 1
    ارجاع رقم * مضروب(رقم - 1)
نهاية

طباعة(مضروب(5))
```

كيف يقرأها الـ lexer:

| الكلمة المفتاحية العربية | المعنى |
|----------------|---------|
| `متغير`       | `var` |
| `دالة`        | `func` |
| `اذا`         | `if` |
| `نفذ`         | `do` |
| `ارجاع`       | `return` |
| `نهاية`       | `end` |
| `طباعة`       | `print` |
| `عدد_صحيح`    | `int` |
| `استقبل`      | `input` |

---

## المكتبات المدمجة

يوفر المترجم عدة مكتبات مدعومة بـ Python، مسجلة كدوال WorldLang أصلية:

| المكتبة | الغرض | الوحدة الأساسية |
|---------|---------|----------------|
| `String` | `split`، `uppercase`، `lowercase`، `contains`، `replace`، ... | `_builtins/String.py` |
| `Random` | توليد أرقام عشوائية | `_builtins/Random.py` |
| `os` | نظام الملفات: `chdir`، `mkdir`، `list_dir`، `move`، `system`، ... | `_builtins/os.py` |
| `Image` | تحميل/حفظ الصور (تحويل إلى/من قوائم RGB) | `_builtins/Image.py` |
| `Graph` | الرسوم البيانية: `plot`، `scatter`، `bar` | `_builtins/Graph.py` |
| `Controls` | أتمتة الماوس/لوحة المفاتيح | `_builtins/Controls.py` |
| `Serial` | الاتصال التسلسلي بالأجهزة/Arduino (`send`/`receive`) | `_builtins/Serial.py` |
| `Speech` | تحويل النص إلى كلام والتعرف على الصوت | `_builtins/Speech.py` |
| `GenAI` | الذكاء الاصطناعي التوليدي عبر Google Gemini | `_builtins/GenAI.py` |

---

## البنية

WorldLang هو **مترجم شجري** (tree-walking interpreter). يمر الكود المصدري عبر خط أنابيب من ثلاث مراحل:

```
1. Lexer  ──→  Tokens (الكلمات المفتاحية المحلية مطابقة مع الرموز العامة)
2. Parser ──→  AST  (شجرة صياغة تجريدية مستقلة عن اللغة)
3. Runtime ──→ Result (يمشي المترجم على الـ AST، إدارة الرموز والنطاقات)
```

**المكونات الرئيسية في `bin/`:**

| الملف | الدور |
|------|------|
| `World.py` | نقطة الدخول — واجهة REPL |
| `Lexer.py` | محلل رمزي؛ يقوم بمطابقة الكلمات المفتاحية ديناميكيًا من جدول اللغة النشط |
| `Parser.py` | قواعد القواعد النحوية → إنشاء AST |
| `Interpreter.py` | ينفذ AST ويوفر المكتبة القياسية |
| `Tokens.py` | أنواع الرموز؛ يحمّل جداول الكلمات المفتاحية (`keywords.json`) |
| `Errors.py` | أنواع الأخطاء (`IllegalChar`، `Syntax`، `Runtime`) |
| `RT_result.py` | نتائج التشغيل، السياق، وجداول الرموز |
| `datatypes/` | `Value`، `Number`، `String`، `List`، `Dict`، `Function` |
| `_builtins/` | المكتبات القياسية المدعومة بـ Python |

جداول الكلمات المفتاحية هي ملفات JSON عادية تحت `data/` (واحد لكل لغة، مثل `Arabic_KW.json`)، مما يبقي دعم اللغة في المحرك مبنيًا بالكامل على البيانات.

---

## إدارة اللغة والمكتبات

يمكن لـ WorldLang جلب الموارد من الإنترنت أثناء التشغيل:

- **`langman`** — تنزيل جداول الكلمات المفتاحية للغات إضافية في `data/`.
- **`libman`** — تنزيل مكتبات `.world` (مثل `math.world`، `json_ar.world`).
- **`extman`** — تنزيل الامتدادات في `extensions/` (مثل امتداد البرمجة الصوتية `vcode.world`).

> تتطلب هذه الميزات اتصالًا بالإنترنت وصولًا إلى مستودع الموارد البعيد الذي يشير إليه المترجم.

---

## المساهمة

WorldLang مفتوح المصدر ومحرك من المجتمع. مرحب بالمساهمات بأشكال متعددة:

- **المساهمون اللغويون** — إضافة أو تحسين جداول التعريب (`data/*_KW.json`).
- **مطورو المترجمات** — تحسين الـ lexer والـ parser والـ runtime والمكتبة القياسية.
- **مطورو الأجهزة** — توسيع التكاملات مع الأجهزة والروبوتات.
- **المختبرون** — اكتشاف الأخطاء وتحسين الموثوقية.
- **الجميع** — الإبلاغ عن المشاكل، تحسين التوثيق، ومشاركة الأفكار.

للمساهمة:

1. استنسخ المستودع.
2. استنسخ الفرع الخاص بك وأنشئ فرعًا جديدًا.
3. أجرِ التغييرات وقم بالالتزام.
4. افتح طلب سحب إلى الفرع `main`.

---

## الرخصة

يُصدر WorldLang بموجب [رخصة MIT](LICENSE).
