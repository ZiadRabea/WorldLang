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
  <a href="README.zh.md">中文</a> |
  <a href="README.ja.md">日本語</a>
</p>

**Eine mehrsprachige Programmiersprache, mit der Sie Code in Ihrer Muttersprache schreiben, ausführen, erkennen und übersetzen können.**

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
* 👤 **Maintainer:** Ziad Rabea ([LinkedIn](https://www.linkedin.com/in/ziadrabea/) | [E-Mail](mailto:zidr2005@gmail.com))

WorldLang ist ein Open-Source-Interpreter, der in Python geschrieben wurde und die Sprachbarriere in der Programmierung beseitigt. Anstatt sich englische Schlüsselwörter merken zu müssen, können Sie Code mit nativer Syntax schreiben — auf Arabisch, Französisch, Japanisch und in vielen weiteren Sprachen.

Die Engine verarbeitet und führt den Code über eine benutzerdefinierte **Lexer → Parser → Runtime**-Pipeline aus und unterstützt zusätzlich automatische Spracherkennung sowie die Übersetzung von WorldLang-Quellcode zwischen unterstützten Sprachen.

> **Unterstützte Sprachen: 31** — Arabisch, Aserbaidschanisch, Chinesisch, Deutsch, Englisch, Finnisch, Französisch, Griechisch, Hindi, Indonesisch, Irisch, Italienisch, Japanisch, Kasachisch, Koreanisch, Kurdisch, Lettisch, Malayisch, Niederländisch, Persisch, Polnisch, Portugiesisch, Rumänisch, Russisch, Spanisch, Schwedisch, Türkisch, Ukrainisch, Urdu, Usbekisch und Vietnamesisch.

---

## Inhaltsverzeichnis

- [Funktionen](#funktionen)
- [Voraussetzungen](#voraussetzungen)
- [Installation](#installation)
- [Verwendung](#verwendung)
- [Spracherkennung & Sprachauswahl](#spracherkennung--sprachauswahl)
- [Codeübersetzung](#codeübersetzung)
- [Code-Beispiel](#code-beispiel)
- [Eingebaute Bibliotheken](#eingebaute-bibliotheken)
- [Architektur](#architektur)
- [Sprach- & Bibliotheksverwaltung](#sprach--bibliotheksverwaltung)
- [Beitragen](#beitragen)
- [Lizenz](#lizenz)

---

## Funktionen

- **Programmierung in der Muttersprache** — schreiben Sie Code mit den Schlüsselwörtern Ihrer gewählten Sprache.
- **31 unterstützte Sprachpakete** mit dynamisch geladenen Schlüsselwortzuordnungen.
- **Hybride Sprachauswahl** — Sprache manuell auswählen oder WorldLang die Sprache automatisch erkennen lassen.
- **KI-basierte Spracherkennung** — erkennt die Sprache der Quellcodedatei automatisch, wenn keine Sprache manuell festgelegt wurde.
- **Sprachübergreifende Ausführung** — Dateien in unterschiedlichen unterstützten Sprachen können ausgeführt werden, ohne die Sprache vorher manuell umzuschalten.
- **Integrierte Codeübersetzung** — übersetzen Sie WorldLang-Quellcode zwischen unterstützten Sprachen.
- **Dynamische Schlüsselwortzuordnung** — der Lexer ordnet native Schlüsselwörter zur Laufzeit generischen Tokens zu.
- **Vollwertiger Interpreter** — Variablen, Funktionen, Rekursion, Schleifen, Bedingungen, Listen, Dictionaries und Arithmetik.
- **Hardware & Robotik** — serielle Kommunikation für Mikrocontroller wie Arduino.
- **Sprache** — Text-to-Speech und Spracherkennung.
- **Eingebaute Bibliotheken** — Bildverarbeitung, Diagramme, Zufallszahlen, Dateisystem und mehr.
- **Generative KI** — optionale Google-Gemini-Integration.
- **Bibliotheks- & Erweiterungsverwaltung** — `.world`-Bibliotheken und Erweiterungen direkt aus dem Netzwerk laden.

---

## Voraussetzungen

- **Python 3.12+**
- **Windows, macOS oder Linux**

Benötigte Pakete:

| Paket | Verwendungszweck |
|---------|-------------------|
| `requests` | Herunterladen von Sprachpaketen, Bibliotheken und Erweiterungen |
| `numpy` | KI-Spracherkennung und numerische Verarbeitung |
| `keras` | KI-basierte Spracherkennung |
| `nltk` | Vorverarbeitung für die Spracherkennung |
| `Pillow` | Bildverarbeitung (`_builtins/Image.py`) |
| `matplotlib` | Diagramme (`_builtins/Graph.py`) |
| `pyautogui` | Maus-/Tastatursteuerung (`_builtins/Controls.py`) |
| `pyserial` | Serielle/Hardware-Kommunikation (`_builtins/Serial.py`) |
| `pyttsx3` | Text-to-Speech (`_builtins/Speech.py`) |
| `SpeechRecognition` | Spracherkennung (`_builtins/Speech.py`) |
| `google-generativeai` | Generative KI (`_builtins/GenAI.py`) |
| `rich` | Markdown-Darstellung für KI-Ausgaben (`_builtins/GenAI.py`) |

> Nur `requests` ist für die grundlegende Interpreter-Funktionalität erforderlich. `Keras`, `NLTK` und `NumPy` werden für die KI-basierte automatische Spracherkennung benötigt. Die übrigen Pakete werden nur für die jeweiligen optionalen eingebauten Bibliotheken benötigt.

---

## Installation

```bash
# 1. Repository klonen
git clone https://github.com/ZiadRabea/WorldLang.git
cd WorldLang

# 2. (Empfohlen) Virtuelle Umgebung erstellen und aktivieren
python -m venv venv

# Windows:
venv\Scriptsctivate

# macOS / Linux:
source venv/bin/activate

# 3. Abhängigkeiten installieren
pip install requests numpy keras nltk Pillow matplotlib pyautogui pyserial pyttsx3 SpeechRecognition rich
```

Um die Google-Gemini-KI-Funktionen zu aktivieren:

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

```text
World >>
```

Geben Sie ein Programm ein und drücken Sie die Eingabetaste, um es auszuführen.

### Spezielle Befehle

| Befehl | Aktion |
|---|---|
| `libman` | Bibliotheksmanager ausführen und `.world`-Bibliotheken herunterladen |
| `langman` | Sprachmanager ausführen und Sprachpakete herunterladen/wechseln |
| `extman` | Erweiterungsmanager ausführen und Erweiterungen herunterladen |
| `setlang` | Programmiersprache manuell auswählen oder automatische Erkennung aktivieren |
| `world()` | Eine WorldLang-Quelldatei ausführen |
| `translate()` | WorldLang-Quellcode zwischen unterstützten Sprachen übersetzen |

---

## Spracherkennung & Sprachauswahl

WorldLang unterstützt ein **hybrides System zur Sprachwahl**.

Sie können die gewünschte Sprache explizit festlegen oder die Sprache nicht angeben und WorldLang automatisch die Sprache des Quellcodes erkennen lassen.

### Manuelle Sprachauswahl

Verwenden Sie:

```text
setlang
```

Beispiel:

```text
setlang -> ArabicKW
```

Damit wird die arabische Schlüsselworttabelle manuell als aktive Sprache festgelegt.

### Automatische Spracherkennung

Lassen Sie das Sprachargument leer:

```text
setlang -> ""
```

Dadurch wird die automatische Spracherkennung aktiviert.

Wenn die automatische Erkennung aktiviert ist, analysiert WorldLang den Quellcode und bestimmt die passende Sprache während der Lexing-/Tokenisierungsphase.

Dadurch können Dateien und importierte Module in verschiedenen unterstützten Sprachen **ohne vorheriges manuelles Umschalten der Sprache** ausgeführt werden.

### KI-Erkennungsmodule

Das automatische Spracherkennungssystem verwendet:

- `Keras`
- `NLTK`
- `NumPy`

Die automatische Erkennung ist optional, wenn eine Sprache manuell mit `setlang` ausgewählt wird.

---

## Codeübersetzung

WorldLang verfügt über einen integrierten **Übersetzer für Quellcode zwischen Sprachen**.

Anstatt Code lediglich durch einfache Textersetzung zu übersetzen, verarbeitet der Übersetzer den Quellcode über eine strukturierte Pipeline:

```text
Source
   ↓
Lexer
   ↓
Translator
   ↓
DeLexer
   ↓
Translated Source
```

Der Quellcode wird zunächst in sprachunabhängige Repräsentationen lexikalisiert. Der Translator ordnet diese Repräsentationen anschließend der Zielsprache zu, bevor der **DeLexer** wieder gültigen WorldLang-Quellcode erzeugt.

### Translate-Befehl

```text
translate(filename.world, source_language, target_language)
```

Beispiel:

```text
translate("factorial.world", "English", "Chinese")
```

WorldLang erzeugt automatisch eine übersetzte Quelldatei mit der Zielsprache.

Beispielsweise:

```text
factorial_Chinese.world
```

So kann ein WorldLang-Programm in einer Sprache geschrieben und anschließend in eine andere unterstützte Sprache übersetzt werden.

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

Dasselbe Programm kann auch auf Englisch geschrieben werden:

```worldlang
# Factorial Calculator
var number = int(input("Enter a number:"))

func factorial(number)
    if number == 1 or number == 0 do return 1
    return number * factorial(number - 1)
end

print(factorial(number))
```

Bei aktivierter automatischer Erkennung kann WorldLang bestimmen, welche unterstützte Sprache der Quellcode verwendet, ohne dass zuvor manuell eine Sprache ausgewählt werden muss.

---

## Eingebaute Bibliotheken

Der Interpreter stellt mehrere Python-gestützte Bibliotheken bereit, die als native WorldLang-Funktionen registriert sind:

| Bibliothek | Zweck | Unterstützungsmodul |
|---------|---------|----------------|
| `String` | `split`, `uppercase`, `lowercase`, `contains`, `replace`, ... | `_builtins/String.py` |
| `Random` | Zufallszahlengenerierung | `_builtins/Random.py` |
| `os` | Dateisystem: `chdir`, `mkdir`, `list_dir`, `move`, `system`, ... | `_builtins/os.py` |
| `Image` | Bilder laden/speichern und in/von RGB-Listen konvertieren | `_builtins/Image.py` |
| `Graph` | `plot`, `scatter`, `bar` zur Diagrammerstellung | `_builtins/Graph.py` |
| `Controls` | Maus-/Tastaturautomatisierung | `_builtins/Controls.py` |
| `Serial` | Serielle Hardware-/Arduino-Kommunikation (`send`/`receive`) | `_builtins/Serial.py` |
| `Speech` | Text-to-Speech und Spracherkennung | `_builtins/Speech.py` |
| `GenAI` | Generative KI über Google Gemini | `_builtins/GenAI.py` |

---

## Architektur

WorldLang ist ein **Tree-Walking-Interpreter** mit einer erweiterten multilingualen Verarbeitungsarchitektur.

### Ausführungspipeline

```text
Quellcode
    ↓
Sprachauswahl / KI-Erkennung
    ↓
Lexer
    ↓
Tokens
    ↓
Parser
    ↓
Abstract Syntax Tree
    ↓
Runtime
    ↓
Ergebnis
```

Die Erkennungsschicht bestimmt vor der Tokenisierung die passende Schlüsselworttabelle, wenn keine Sprache manuell festgelegt wurde.

### Übersetzungspipeline

```text
Source
   ↓
Lexer
   ↓
Sprachunabhängige Repräsentation
   ↓
Translator
   ↓
DeLexer
   ↓
Translated Source
```

Diese Architektur ermöglicht es WorldLang, mehrsprachigen Quellcode auszuführen und zu übersetzen, während die zugrunde liegende Interpreter-Pipeline sprachunabhängig bleibt.

### Wichtige Komponenten

| Datei / Komponente | Rolle |
|---|---|
| `World.py` | Einstiegspunkt und REPL-Shell |
| `Lexer.py` | Tokenizer; ordnet Schlüsselwörter aus der erkannten oder ausgewählten Sprache dynamisch zu |
| `Parser.py` | Grammatikregeln → AST-Erzeugung |
| `Interpreter.py` | Führt die AST aus und stellt die Standardbibliothek bereit |
| `Tokens.py` | Token-Typen und Schlüsselwortverwaltung |
| `Translator.py` | Übersetzt tokenisierte Repräsentationen zwischen unterstützten Sprachen |
| `DeLexer.py` | Erzeugt Quellcode mit den Schlüsselwörtern der Zielsprache |
| `Errors.py` | Fehlertypen (`IllegalChar`, `Syntax`, `Runtime`) |
| `RT_result.py` | Laufzeitergebnisse, Kontext und Symboltabellen |
| `datatypes/` | `Value`, `Number`, `String`, `List`, `Dict`, `Function` |
| `_builtins/` | Python-gestützte Standardbibliotheken |
| `data/` | Sprachschlüsselworttabellen und mehrsprachige Sprachressourcen |

Die Schlüsselworttabellen sind datengetriebene JSON-Dateien, sodass zusätzliche Sprachen hinzugefügt werden können, ohne die zentrale Interpreter-Grammatik neu schreiben zu müssen.

---

## Sprach- & Bibliotheksverwaltung

WorldLang kann zur Laufzeit Ressourcen aus dem Netzwerk abrufen:

- **`langman`** — Schlüsselworttabellen für zusätzliche Sprachen nach `data/` herunterladen.
- **`libman`** — `.world`-Bibliotheken herunterladen.
- **`extman`** — Erweiterungen nach `extensions/` herunterladen.
- **`setlang`** — eine Sprache manuell festlegen oder die KI-basierte automatische Spracherkennung aktivieren.
- **`world()`** — WorldLang-Quelldateien ausführen.
- **`translate()`** — WorldLang-Quellcode zwischen unterstützten Sprachen übersetzen.

> Sprachenerkennung und Übersetzung nutzen die mehrsprachige Schlüsselwortarchitektur, sodass verschiedene Sprachpakete dieselbe zugrunde liegende Interpreterstruktur verwenden können.

---

## Beitragen

WorldLang ist Open-Source und gemeinschaftlich getrieben. Beiträge sind in vielen Formen willkommen:

- **Sprachbeiträge** — Lokalisierungs- und Schlüsselworttabellen hinzufügen oder verbessern.
- **Interpreter-Entwickler** — Lexer, Parser, Translator, DeLexer, Runtime und Standardbibliothek verbessern.
- **KI-Entwickler** — Modelle und Vorverarbeitung für die automatische Spracherkennung verbessern.
- **Hardware-Entwickler** — Hardware- und Roboterintegrationen erweitern.
- **Tester** — Fehler entdecken und die Zuverlässigkeit verbessern.
- **Jeder** — Probleme melden, Dokumentation verbessern und Ideen teilen.

Um beizutragen:

1. Forken Sie das Repository.
2. Klonen Sie Ihren Fork und erstellen Sie einen Branch.
3. Nehmen Sie Ihre Änderungen vor und committen Sie diese.
4. Öffnen Sie einen Pull Request gegen den `main`-Branch.

---

## Lizenz

WorldLang wird unter der [MIT-Lizenz](LICENSE) veröffentlicht.
