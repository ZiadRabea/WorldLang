# WorldLang

<p align="center">
  <img src="images/world.png" alt="WorldLang Logo" width="200">
</p>

<p align="center">
  <strong>English</strong> |
  <a href="README.ar.md">العربية</a> |
  <a href="README.fr.md">Français</a> |
  <a href="README.es.md">Español</a> |
  <a href="README.de.md">Deutsch</a> |
  <a href="README.zh.md">中文</a>
</p>

**A multilingual programming language that lets you write and run code in your native language.**

<p align="center">
  <a href="https://github.com/ZiadRabea/WorldLang/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/ZiadRabea/WorldLang" alt="GitHub License">
  </a>
  <br>
  <a href="https://marketplace.visualstudio.com/items?itemName=worldlangteam.WorldEn">
    <img src="https://vsmarketplacebadges.dev/version-short/worldlangteam.WorldEn.svg" alt="VSCode Extension">
  </a>
  <br>
  <a href="https://www.researchgate.net/publication/377782413_A_Multilingual_Approach_with_Built-in_Code_Translation_and_Dynamic_Keyword_Importation">
    <img src="https://img.shields.io/badge/ResearchGate-preprint-brightgreen" alt="ResearchGate">
  </a>
</p>

**Resources & Links:**

* 📖 **[Official Documentation](https://ziadrabea.github.io/WorldDocs)**
  * 🚀 [Getting Started](https://ziadrabea.github.io/WorldDocs/installation.html)
  * 📚 [Language Reference](https://ziadrabea.github.io/WorldDocs/features.html)
  * 🌍 [Supported Languages](https://ziadrabea.github.io/WorldDocs/languages.html)
  * 🤝 [Contributing Guide](https://ziadrabea.github.io/WorldDocs/guide.html)
* 🌐 **[Official Website](https://ziadrabea.github.io/worldlanguage)**
* 💬 **[Join the Community](https://flow.daisyscript.com)**
* 🔬 **[Academic Pre-print (ResearchGate)](https://www.researchgate.net/publication/377782413_A_Multilingual_Approach_with_Built-in_Code_Translation_and_Dynamic_Keyword_Importation)**
* 🧩 **[WorldLangEN VS Code Extension](https://marketplace.visualstudio.com/items?itemName=worldlangteam.WorldEn)**
* 👤 **Maintainer:** Ziad Rabea ([LinkedIn](https://www.linkedin.com/in/ziadrabea/) | [Email](mailto:zidr2005@gmail.com))

WorldLang is an open-source interpreter built in Python that removes the language barrier in programming. Instead of memorizing English keywords, you write code using native syntax — Arabic, French, Japanese, and 18 more languages — and the engine tokenizes and executes it through a custom Lexer → Parser → Runtime pipeline.

> **Supported languages: 21** — Arabic, Chinese, Dutch, English, French, German, Indonesian, Italian, Japanese, Kazakh, Korean, Persian, Polish, Portuguese, Romanian, Russian, Spanish, Turkish, Ukrainian, Urdu, Vietnamese.

---

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Code Example](#code-example)
- [Built-in Libraries](#built-in-libraries)
- [Architecture](#architecture)
- [Language & Library Management](#language--library-management)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **Native-language programming** — write code using the keywords of your chosen language.
- **21 language packs** shipped in `data/` as JSON keyword tables.
- **Dynamic keyword mapping** — the lexer maps native keywords to generic tokens on the fly.
- **Full-featured interpreter** — variables, functions, recursion, loops, conditionals, lists, dicts, and arithmetic.
- **Hardware & robotics** — serial communication for microcontrollers (e.g. Arduino).
- **Speech** — text-to-speech and voice recognition.
- **Built-in libraries** — image processing, plotting, random, filesystem, and more.
- **Generative AI** — optional Google Gemini integration.
- **Library & extension management** — fetch `.world` libraries and extensions directly from the network.

---

## Requirements

- **Python 3.12+**
- **Windows, macOS, or Linux**

Core packages needed (see [Installation](#installation)):

| Package | Used for |
|---------|----------|
| `requests` | Downloading language packs, libraries, and extensions |
| `Pillow` | Image processing (`_builtins/Image.py`) |
| `matplotlib` & `numpy` | Plotting (`_builtins/Graph.py`) |
| `pyautogui` | Mouse/keyboard control (`_builtins/Controls.py`) |
| `pyserial` | Serial/hardware communication (`_builtins/Serial.py`) |
| `pyttsx3` | Text-to-speech (`_builtins/Speech.py`) |
| `SpeechRecognition` | Voice recognition (`_builtins/Speech.py`) |
| `google-generativeai` | Generative AI (`_builtins/GenAI.py`) |
| `rich` | Markdown rendering for AI output (`_builtins/GenAI.py`) |

> Only `requests` is required for core functionality. The remaining packages are needed only for the specific optional built-in libraries listed above.

---

## Installation

```bash
# 1. Clone the repository
git clone https://github.com/ZiadRabea/WorldLang.git
cd WorldLang

# 2. (Recommended) Create and activate a virtual environment
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS / Linux:
source venv/bin/activate

# 3. Install dependencies
pip install requests Pillow matplotlib numpy pyautogui pyserial pyttsx3 SpeechRecognition rich
```

To enable the AI features, you additionally need:

```bash
pip install google-generativeai
```

---

## Usage

The interpreter ships as a REPL (Read–Eval–Print Loop). To start it:

```bash
python bin/World.py
```

A prompt appears:

```
World >>
```

Type a program and press Enter to execute it. Special commands at the prompt:

| Command    | Action                                                        |
|------------|---------------------------------------------------------------|
| `libman`   | Run the library manager (download `.world` libraries)         |
| `langman`  | Run the language manager (download/switch language packs)     |
| `extman`   | Run the extension manager (download extensions)               |

`WorldLang` is Arabic-by-default. The Arabic keywords are loaded from `bin/keywords.json`. Switch or add languages via the `langman` manager.

---

## Code Example

A recursive **factorial calculator** written entirely with native Arabic keywords:

```world
# حاسبة المضروب
متغير الرقم = عدد_صحيح(استقبل("أدخل رقماً"))

دالة مضروب(رقم)
    اذا رقم == 1 او رقم == 0 نفذ ارجاع 1
    ارجاع رقم * مضروب(رقم - 1)
نهاية

طباعة(مضروب(5))
```

How the lexer reads it:

| Arabic keyword | Meaning |
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

## Built-in Libraries

The interpreter exposes several Python-backed libraries, registered as native WorldLang functions:

| Library | Purpose | Backing module |
|---------|---------|----------------|
| `String` | `split`, `uppercase`, `lowercase`, `contains`, `replace`, ... | `_builtins/String.py` |
| `Random` | Random number generation | `_builtins/Random.py` |
| `os` | Filesystem: `chdir`, `mkdir`, `list_dir`, `move`, `system`, ... | `_builtins/os.py` |
| `Image` | Load/save images (convert to/from RGB lists) | `_builtins/Image.py` |
| `Graph` | `plot`, `scatter`, `bar` charting | `_builtins/Graph.py` |
| `Controls` | Mouse/keyboard automation | `_builtins/Controls.py` |
| `Serial` | Hardware/Arduino serial communication (`send`/`receive`) | `_builtins/Serial.py` |
| `Speech` | Text-to-speech and voice recognition | `_builtins/Speech.py` |
| `GenAI` | Generative AI via Google Gemini | `_builtins/GenAI.py` |

---

## Architecture

WorldLang is a **tree-walking interpreter**. Source code passes through a three-stage pipeline:

```
1. Lexer  ──→  Tokens (native keywords mapped to generic tokens)
2. Parser ──→  AST  (language-agnostic Abstract Syntax Tree)
3. Runtime ──→ Result (interpreter walks the AST, managing symbols & scope)
```

**Key components in `bin/`:**

| File | Role |
|------|------|
| `World.py` | Entry point — REPL shell |
| `Lexer.py` | Tokenizer; dynamically maps keywords from the active language table |
| `Parser.py` | Grammar rules → AST generation |
| `Interpreter.py` | Executes the AST and provides the standard library |
| `Tokens.py` | Token types; loads keyword tables (`keywords.json`) |
| `Errors.py` | Error types (`IllegalChar`, `Syntax`, `Runtime`) |
| `RT_result.py` | Runtime results, context, and symbol tables |
| `datatypes/` | `Value`, `Number`, `String`, `List`, `Dict`, `Function` |
| `_builtins/` | Python-backed standard libraries |

The keyword tables are plain JSON files under `data/` (one per language, e.g. `Arabic_KW.json`), which keep the engine's language support fully data-driven.

---

## Language & Library Management

WorldLang can fetch resources from the network at runtime:

- **`langman`** — download keyword tables for additional languages into `data/`.
- **`libman`** — download `.world` libraries (e.g. `math.world`, `json_ar.world`).
- **`extman`** — download extensions into `extensions/` (e.g. the voice-coding extension `vcode.world`).

> These features require an internet connection and access to the remote resource repository referenced by the interpreter.

---

## Contributing

WorldLang is open-source and community-driven. Contributions are welcome in many forms:

- **Language contributors** — add or improve localization tables (`data/*_KW.json`).
- **Compiler developers** — improve the lexer, parser, runtime, and standard library.
- **Hardware developers** — expand hardware and robotics integrations.
- **Testers** — discover bugs and improve reliability.
- **Everyone** — report issues, improve documentation, and share ideas.

To contribute:

1. Fork the repository.
2. Clone your fork and create a branch.
3. Make your changes and commit them.
4. Open a Pull Request to the `main` branch.

---

## License

WorldLang is released under the [MIT License](LICENSE).
