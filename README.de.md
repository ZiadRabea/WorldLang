# WorldLang

<p align="center">
  <img src="images/world.png" alt="WorldLang-Logo" width="200">
</p>

<p align="center">
  <a href="README.md">English</a> |
  <a href="README.ar.md">العربية</a> |
  <a href="README.fr.md">Français</a> |
  <a href="README.es.md">Español</a> |
  <strong>Deutsch</strong> |
  <a href="README.zh.md">中文</a>
</p>

**Eine mehrsprachige Programmiersprache, mit der Sie Code in Ihrer Muttersprache schreiben und ausführen können.**

<p align="center">
  <a href="https://github.com/ZiadRabea/WorldLang/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/ZiadRabea/WorldLang" alt="GitHub-Lizenz">
  </a>
  <br>
  <a href="https://marketplace.visualstudio.com/items?itemName=worldlangteam.WorldEn">
    <img src="https://vsmarketplacebadges.dev/version-short/worldlangteam.WorldEn.svg" alt="VSCode-Erweiterung">
  </a>
  <br>
  <a href="https://www.researchgate.net/publication/377782413_A_Multilingual_Approach_with_Built-in_Code_Translation_and_Dynamic_Keyword_Importation">
    <img src="https://img.shields.io/badge/ResearchGate-preprint-brightgreen" alt="ResearchGate">
  </a>
</p>

**Ressourcen und Links:**

* 📖 **[Offizielle Dokumentation](https://ziadrabea.github.io/WorldDocs)**
  * 🚀 [Erste Schritte](https://ziadrabea.github.io/WorldDocs/installation.html)
  * 📚 [Sprachreferenz](https://ziadrabea.github.io/WorldDocs/features.html)
  * 🌍 [Unterstützte Sprachen](https://ziadrabea.github.io/WorldDocs/languages.html)
  * 🤝 [Beitragsanleitung](https://ziadrabea.github.io/WorldDocs/guide.html)
* 🌐 **[Offizielle Website](https://ziadrabea.github.io/worldlanguage)**
* 💬 **[Der Community beitreten](https://flow.daisyscript.com)**
* 🔬 **[Akademischer Preprint (ResearchGate)](https://www.researchgate.net/publication/377782413_A_Multilingual_Approach_with_Built-in_Code_Translation_and_Dynamic_Keyword_Importation)**
* 🧩 **[WorldLangEN VS-Code-Erweiterung](https://marketplace.visualstudio.com/items?itemName=worldlangteam.WorldEn)**
* 👤 **Betreuer:** Ziad Rabea ([LinkedIn](https://www.linkedin.com/in/ziadrabea/) | [E-Mail](mailto:zidr2005@gmail.com))

WorldLang ist ein Open-Source-Interpreter, der in Python geschrieben wurde und die Sprachbarriere in der Programmierung beseitigt. Anstatt sich englische Schlüsselwörter zu merken, schreiben Sie Code mit nativer Syntax – Arabisch, Französisch, Japanisch und 18 weitere Sprachen – und die Engine tokenisiert und führt ihn über eine benutzerdefinierte Lexer → Parser → Runtime-Pipeline aus.

> **Unterstützte Sprachen: 21** — Arabisch, Chinesisch, Niederländisch, Englisch, Französisch, Deutsch, Indonesisch, Italienisch, Japanisch, Kasachisch, Koreanisch, Persisch, Polnisch, Portugiesisch, Rumänisch, Russisch, Spanisch, Türkisch, Ukrainisch, Urdu, Vietnamesisch.

---

## Inhaltsverzeichnis

- [Funktionen](#funktionen)
- [Voraussetzungen](#voraussetzungen)
- [Installation](#installation)
- [Verwendung](#verwendung)
- [Code-Beispiel](#code-beispiel)
- [Eingebaute Bibliotheken](#eingebaute-bibliotheken)
- [Architektur](#architektur)
- [Sprach- & Bibliotheksverwaltung](#sprach--bibliotheksverwaltung)
- [Beitragen](#beitragen)
- [Lizenz](#lizenz)

---

## Funktionen

- **Programmierung in der Muttersprache** — schreiben Sie Code mit den Schlüsselwörtern Ihrer gewählten Sprache.
- **21 Sprachpakete** werden in `data/` als JSON-Schlüsselworttabellen mitgeliefert.
- **Dynamische Schlüsselwortzuordnung** — der Lexer ordnet native Schlüsselwörter zur Laufzeit generischen Token zu.
- **Vollwertiger Interpreter** — Variablen, Funktionen, Rekursion, Schleifen, Bedingungen, Listen, Dictionaries und Arithmetik.
- **Hardware & Robotik** — serielle Kommunikation für Mikrocontroller (z.B. Arduino).
- **Sprache** — Text-to-Speech und Spracherkennung.
- **Eingebaute Bibliotheken** — Bildverarbeitung, Diagramme, Zufallszahlen, Dateisystem und mehr.
- **Generative KI** — optionale Google-Gemini-Integration.
- **Bibliotheks- & Erweiterungsverwaltung** — laden Sie `.world`-Bibliotheken und Erweiterungen direkt aus dem Netz herunter.

---

## Voraussetzungen

- **Python 3.12+**
- **Windows, macOS oder Linux**

Benötigte Kernpakete (siehe [Installation](#installation)):

| Paket | Verwendungszweck |
|-------|-------------------|
| `requests` | Herunterladen von Sprachpaketen, Bibliotheken und Erweiterungen |
| `Pillow` | Bildverarbeitung (`_builtins/Image.py`) |
| `matplotlib` & `numpy` | Diagramme (`_builtins/Graph.py`) |
| `pyautogui` | Maus-/Tastatursteuerung (`_builtins/Controls.py`) |
| `pyserial` | Serielle/Hardware-Kommunikation (`_builtins/Serial.py`) |
| `pyttsx3` | Text-to-Speech (`_builtins/Speech.py`) |
| `SpeechRecognition` | Spracherkennung (`_builtins/Speech.py`) |
| `google-generativeai` | Generative KI (`_builtins/GenAI.py`) |
| `rich` | Markdown-Darstellung für KI-Ausgaben (`_builtins/GenAI.py`) |

> Nur `requests` ist für die Kernfunktionalität erforderlich. Die übrigen Pakete werden nur für die oben aufgeführten spezifischen optionalen eingebauten Bibliotheken benötigt.

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

Um die KI-Funktionen zu aktivieren, benötigen Sie zusätzlich:

```bash
pip install google-generativeai
```

---

## Verwendung

Der Interpreter wird als REPL (Read–Eval–Print Loop) ausgeliefert. Starten Sie ihn mit:

```bash
python bin/World.py
```

Es erscheint eine Eingabeaufforderung:

```
World >>
```

Geben Sie ein Programm ein und drücken Sie Sie Eingabe, um es auszuführen. Spezielle Befehle an der Eingabeaufforderung:

| Befehl | Aktion |
|--------|--------|
| `libman` | Bibliotheksmanager ausführen (`.world`-Bibliotheken herunterladen) |
| `langman` | Sprachmanager ausführen (Sprachpakete herunterladen/wechseln) |
| `extman` | Erweiterungsmanager ausführen (Erweiterungen herunterladen) |

`WorldLang` ist standardmäßig auf Arabisch eingestellt. Die arabischen Schlüsselwörter werden aus `bin/keywords.json` geladen. Wechseln oder fügen Sie Sprachen über den `langman`-Manager hinzu.

---

## Code-Beispiel

Ein rekursiver **Fakultätsrechner**, der vollständig mit nativen arabischen Schlüsselwörtern geschrieben ist:

```world
# حاسبة المضروب
متغير الرقم = عدد_صحيح(استقبل("أدخل رقماً"))

دالة مضروب(رقم)
    اذا رقم == 1 او رقم == 0 نفذ ارجاع 1
    ارجاع رقم * مضروب(رقم - 1)
نهاية

طباعة(مضروب(5))
```

So liest der Lexer den Code:

| Arabisches Schlüsselwort | Bedeutung |
|---------------------------|-----------|
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

## Eingebaute Bibliotheken

Der Interpreter stellt mehrere Python-gestützte Bibliotheken bereit, die als native WorldLang-Funktionen registriert sind:

| Bibliothek | Zweck | Unterstützungsmodule |
|-----------|-------|-----------------------|
| `String` | `split`, `uppercase`, `lowercase`, `contains`, `replace`, ... | `_builtins/String.py` |
| `Random` | Zufallszahlengenerierung | `_builtins/Random.py` |
| `os` | Dateisystem: `chdir`, `mkdir`, `list_dir`, `move`, `system`, ... | `_builtins/os.py` |
| `Image` | Bilder laden/speichern (Konvertierung zu/von RGB-Listen) | `_builtins/Image.py` |
| `Graph` | `plot`, `scatter`, `bar` Diagrammerstellung | `_builtins/Graph.py` |
| `Controls` | Maus-/Tastaturautomatisierung | `_builtins/Controls.py` |
| `Serial` | Hardware-/Arduino-serielle Kommunikation (`send`/`receive`) | `_builtins/Serial.py` |
| `Speech` | Text-to-Speech und Spracherkennung | `_builtins/Speech.py` |
| `GenAI` | Generative KI über Google Gemini | `_builtins/GenAI.py` |

---

## Architektur

WorldLang ist ein **Tree-Walking-Interpreter**. Der Quellcode durchläuft eine dreistufige Pipeline:

```
1. Lexer  ──→  Tokens (native keywords mapped to generic tokens)
2. Parser ──→  AST  (language-agnostic Abstract Syntax Tree)
3. Runtime ──→ Result (interpreter walks the AST, managing symbols & scope)
```

**Wichtige Komponenten in `bin/`:**

| Datei | Rolle |
|-------|-------|
| `World.py` | Einstiegspunkt — REPL-Shell |
| `Lexer.py` | Tokenizer; ordnet Schlüsselwörter aus der aktiven Sprachtabelle dynamisch zu |
| `Parser.py` | Grammatikregeln → AST-Erzeugung |
| `Interpreter.py` | Führt die AST aus und stellt die Standardbibliothek bereit |
| `Tokens.py` | Token-Typen; lädt Schlüsselworttabellen (`keywords.json`) |
| `Errors.py` | Fehlertypen (`IllegalChar`, `Syntax`, `Runtime`) |
| `RT_result.py` | Laufzeitergebnisse, Kontext und Symboltabellen |
| `datatypes/` | `Value`, `Number`, `String`, `List`, `Dict`, `Function` |
| `_builtins/` | Python-gestützte Standardbibliotheken |

Die Schlüsselworttabellen sind einfache JSON-Dateien unter `data/` (eine pro Sprache, z.B. `Arabic_KW.json`), die die Sprachunterstützung der Engine vollständig datengetrieben halten.

---

## Sprach- & Bibliotheksverwaltung

WorldLang kann zur Laufzeit Ressourcen aus dem Netz abrufen:

- **`langman`** — laden Sie Schlüsselworttabellen für zusätzliche Sprachen in `data/` herunter.
- **`libman`** — laden Sie `.world`-Bibliotheken herunter (z.B. `math.world`, `json_ar.world`).
- **`extman`** — laden Sie Erweiterungen in `extensions/` herunter (z.B. die Sprachcodierungs-Erweiterung `vcode.world`).

> Diese Funktionen erfordern eine Internetverbindung und Zugriff auf das vom Interpreter referenzierte Remote-Ressourcen-Repository.

---

## Beitragen

WorldLang ist Open-Source und gemeinschaftlich getrieben. Beiträge sind in vielen Formen willkommen:

- **Sprachbeiträge** — fügen Sie Lokalisierungstabellen hinzu oder verbessern Sie diese (`data/*_KW.json`).
- **Compiler-Entwickler** — verbessern Sie Lexer, Parser, Laufzeitumgebung und Standardbibliothek.
- **Hardware-Entwickler** — erweitern Sie Hardware- und Roboterintegrations.
- **Tester** — entdecken Sie Fehler und verbessern Sie die Zuverlässigkeit.
- **Jeder** — melden Sie Probleme, verbessern Sie die Dokumentation und teilen Sie Ideen.

Um beizutragen:

1. Gabeln Sie das Repository.
2. Klonen Sie Ihre Gabel und erstellen Sie einen Branch.
3. Nehmen Sie Ihre Änderungen vor und commitsen Sie sie.
4. Öffnen Sie einen Pull Request an den `main`-Branch.

---

## Lizenz

WorldLang wird unter der [MIT-Lizenz](LICENSE) veröffentlicht.
