# WorldLang

<p align="center">
  <img src="images/world.png" alt="Logo de WorldLang" width="200">
</p>

<p align="center">
  <a href="README.md">English</a> |
  <a href="README.ar.md">العربية</a> |
  <a href="README.fr.md">Français</a> |
  <strong>Español</strong> |
  <a href="README.de.md">Deutsch</a> |
  <a href="README.zh.md">中文</a>
</p>

**Un lenguaje de programación multilingüe que te permite escribir y ejecutar código en tu idioma nativo.**

<p align="center">
  <a href="https://github.com/ZiadRabea/WorldLang/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/ZiadRabea/WorldLang" alt="Licencia GitHub">
  </a>
  <br>
  <a href="https://marketplace.visualstudio.com/items?itemName=worldlangteam.WorldEn">
    <img src="https://vsmarketplacebadges.dev/version-short/worldlangteam.WorldEn.svg" alt="Extensión VSCode">
  </a>
  <br>
  <a href="https://www.researchgate.net/publication/377782413_A_Multilingual_Approach_with_Built-in_Code_Translation_and_Dynamic_Keyword_Importation">
    <img src="https://img.shields.io/badge/ResearchGate-preprint-brightgreen" alt="ResearchGate">
  </a>
</p>

**Recursos y enlaces:**

* 📖 **[Documentación oficial](https://ziadrabea.github.io/WorldDocs)**
  * 🚀 [Primeros pasos](https://ziadrabea.github.io/WorldDocs/installation.html)
  * 📚 [Referencia del lenguaje](https://ziadrabea.github.io/WorldDocs/features.html)
  * 🌍 [Idiomas compatibles](https://ziadrabea.github.io/WorldDocs/languages.html)
  * 🤝 [Guía de contribución](https://ziadrabea.github.io/WorldDocs/guide.html)
* 🌐 **[Sitio web oficial](https://ziadrabea.github.io/worldlanguage)**
* 💬 **[Únete a la comunidad](https://flow.daisyscript.com)**
* 🔬 **[Pre-publicación académica (ResearchGate)](https://www.researchgate.net/publication/377782413_A_Multilingual_Approach_with_Built-in_Code_Translation_and_Dynamic_Keyword_Importation)**
* 🧩 **[Extensión de VS Code WorldLangEN](https://marketplace.visualstudio.com/items?itemName=worldlangteam.WorldEn)**
* 👤 **Mantenedor:** Ziad Rabea ([LinkedIn](https://www.linkedin.com/in/ziadrabea/) | [Correo](mailto:zidr2005@gmail.com))

WorldLang es un intérprete de código abierto construido en Python que elimina la barrera del idioma en la programación. En lugar de memorizar palabras clave en inglés, escribes código usando sintaxis nativa — árabe, francés, japonés y 18 idiomas más — y el motor lo tokeniza y ejecuta a través de un pipeline personalizado de Lexer → Parser → Runtime.

> **Idiomas compatibles: 21** — Árabe, Chino, Neerlandés, Inglés, Francés, Alemán, Indonesio, Italiano, Japonés, Kazajo, Coreano, Persa, Polaco, Portugués, Rumano, Ruso, Español, Turco, Ucraniano, Urdu, Vietnamita.

---

## Tabla de Contenidos

- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Ejemplo de Código](#ejemplo-de-código)
- [Bibliotecas Integradas](#bibliotecas-integradas)
- [Arquitectura](#arquitectura)
- [Gestión de Idiomas y Bibliotecas](#gestión-de-idiomas-y-bibliotecas)
- [Contribuir](#contribuir)
- [Licencia](#licencia)

---

## Características

- **Programación en idioma nativo** — escribe código usando las palabras clave de tu idioma elegido.
- **21 paquetes de idiomas** incluidos en `data/` como tablas de palabras clave JSON.
- **Mapeo dinámico de palabras clave** — el lexer asigna las palabras clave nativas a tokens genéricos en tiempo de ejecución.
- **Intérprete con funciones completas** — variables, funciones, recursión, bucles, condicionales, listas, diccionarios y aritmética.
- **Hardware y robótica** — comunicación serial para microcontroladores (por ejemplo, Arduino).
- **Voz** — texto a voz y reconocimiento de voz.
- **Bibliotecas integradas** — procesamiento de imágenes, gráficos, aleatoriedad, sistema de archivos y más.
- **IA generativa** — integración opcional con Google Gemini.
- **Gestión de bibliotecas y extensiones** — obtén bibliotecas y extensiones `.world` directamente de la red.

---

## Requisitos

- **Python 3.12+**
- **Windows, macOS o Linux**

Paquetes principales necesarios (ver [Instalación](#instalación)):

| Paquete | Uso |
|---------|-----|
| `requests` | Descarga de paquetes de idiomas, bibliotecas y extensiones |
| `Pillow` | Procesamiento de imágenes (`_builtins/Image.py`) |
| `matplotlib` y `numpy` | Gráficos (`_builtins/Graph.py`) |
| `pyautogui` | Control de mouse/teclado (`_builtins/Controls.py`) |
| `pyserial` | Comunicación serial/hardware (`_builtins/Serial.py`) |
| `pyttsx3` | Texto a voz (`_builtins/Speech.py`) |
| `SpeechRecognition` | Reconocimiento de voz (`_builtins/Speech.py`) |
| `google-generativeai` | IA generativa (`_builtins/GenAI.py`) |
| `rich` | Renderizado de Markdown para salida de IA (`_builtins/GenAI.py`) |

> Solo `requests` es necesario para la funcionalidad principal. Los paquetes restantes solo se necesitan para las bibliotecas integradas opcionales específicas mencionadas arriba.

---

## Instalación

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

Para habilitar las funciones de IA, additionally necesitas:

```bash
pip install google-generativeai
```

---

## Uso

El intérprete se presenta como un REPL (Bucle de Lectura–Evaluación–Impresión). Para iniciarlo:

```bash
python bin/World.py
```

Aparece un indicador:

```
World >>
```

Escribe un programa y presiona Enter para ejecutarlo. Comandos especiales en el indicador:

| Comando    | Acción |
|------------|--------|
| `libman`   | Ejecutar el gestor de bibliotecas (descargar bibliotecas `.world`) |
| `langman`  | Ejecutar el gestor de idiomas (descargar/cambiar paquetes de idiomas) |
| `extman`   | Ejecutar el gestor de extensiones (descargar extensiones) |

`WorldLang` usa árabe por defecto. Las palabras clave en árabe se cargan desde `bin/keywords.json`. Cambia o añade idiomas mediante el gestor `langman`.

---

## Ejemplo de Código

Una **calculadora de factorial** recursiva escrita enteramente con palabras clave nativas en árabe:

```world
# حاسبة المضروب
متغير الرقم = عدد_صحيح(استقبل("أدخل رقماً"))

دالة مضروب(رقم)
    اذا رقم == 1 او رقم == 0 نفذ ارجاع 1
    ارجاع رقم * مضروب(رقم - 1)
نهاية

طباعة(مضروب(5))
```

Cómo el lexer lo lee:

| Palabra clave árabe | Significado |
|---------------------|-------------|
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

## Bibliotecas Integradas

El intérprete expone varias bibliotecas respaldadas por Python, registradas como funciones nativas de WorldLang:

| Biblioteca | Propósito | Módulo de respaldo |
|------------|-----------|---------------------|
| `String` | `split`, `uppercase`, `lowercase`, `contains`, `replace`, ... | `_builtins/String.py` |
| `Random` | Generación de números aleatorios | `_builtins/Random.py` |
| `os` | Sistema de archivos: `chdir`, `mkdir`, `list_dir`, `move`, `system`, ... | `_builtins/os.py` |
| `Image` | Cargar/guardar imágenes (convertir a/de listas RGB) | `_builtins/Image.py` |
| `Graph` | Gráficos `plot`, `scatter`, `bar` | `_builtins/Graph.py` |
| `Controls` | Automatización de mouse/teclado | `_builtins/Controls.py` |
| `Serial` | Comunicación serial hardware/Arduino (`send`/`receive`) | `_builtins/Serial.py` |
| `Speech` | Texto a voz y reconocimiento de voz | `_builtins/Speech.py` |
| `GenAI` | IA generativa a través de Google Gemini | `_builtins/GenAI.py` |

---

## Arquitectura

WorldLang es un **intérprete de recorrido de árbol**. El código fuente pasa a través de un pipeline de tres etapas:

```
1. Lexer  ──→  Tokens (palabras clave nativas mapeadas a tokens genéricos)
2. Parser ──→  AST  (Árbol de Sintaxis Abstracta independiente del idioma)
3. Runtime ──→ Result (el intérprete recorre el AST, gestionando símbolos y alcance)
```

**Componentes principales en `bin/`:**

| Archivo | Rol |
|---------|-----|
| `World.py` | Punto de entrada — REPL shell |
| `Lexer.py` | Tokenizador; asigna dinámicamente palabras clave desde la tabla del idioma activo |
| `Parser.py` | Reglas gramaticales → generación de AST |
| `Interpreter.py` | Ejecuta el AST y proporciona la biblioteca estándar |
| `Tokens.py` | Tipos de token; carga tablas de palabras clave (`keywords.json`) |
| `Errors.py` | Tipos de error (`IllegalChar`, `Syntax`, `Runtime`) |
| `RT_result.py` | Resultados de tiempo de ejecución, contexto y tablas de símbolos |
| `datatypes/` | `Value`, `Number`, `String`, `List`, `Dict`, `Function` |
| `_builtins/` | Bibliotecas estándar respaldadas por Python |

Las tablas de palabras clave son archivos JSON simples bajo `data/` (uno por idioma, por ejemplo `Arabic_KW.json`), que mantienen el soporte de idiomas del motor completamente basado en datos.

---

## Gestión de Idiomas y Bibliotecas

WorldLang puede obtener recursos de la red en tiempo de ejecución:

- **`langman`** — descargar tablas de palabras clave para idiomas adicionales en `data/`.
- **`libman`** — descargar bibliotecas `.world` (por ejemplo, `math.world`, `json_ar.world`).
- **`extman`** — descargar extensiones en `extensions/` (por ejemplo, la extensión de codificación por voz `vcode.world`).

> Estas funciones requieren una conexión a internet y acceso al repositorio de recursos remoto referenciado por el intérprete.

---

## Contribuir

WorldLang es de código abierto y está impulsado por la comunidad. Las contribuciones son bienvenidas en muchas formas:

- **Contribuidores de idiomas** — añadir o mejorar tablas de localización (`data/*_KW.json`).
- **Desarrolladores del compilador** — mejorar el lexer, parser, runtime y la biblioteca estándar.
- **Desarrolladores de hardware** — ampliar las integraciones de hardware y robótica.
- **Probadores** — descubrir errores y mejorar la fiabilidad.
- **Todos** — reportar problemas, mejorar la documentación y compartir ideas.

Para contribuir:

1. Haz un fork del repositorio.
2. Clona tu fork y crea una rama.
3. Realiza tus cambios y compromételos.
4. Abre un Pull Request a la rama `main`.

---

## Licencia

WorldLang se publica bajo la [Licencia MIT](LICENSE).
