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
  <a href="README.zh.md">中文</a> |
  <a href="README.ja.md">日本語</a>
</p>

**Un lenguaje de programación multilingüe que te permite escribir, ejecutar, detectar y traducir código en tu idioma nativo.**

<p align="center">
  <a href="https://github.com/ZiadRabea/WorldLang/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/ZiadRabea/WorldLang" alt="Licencia de GitHub">
  </a>
  <br>
  <a href="https://marketplace.visualstudio.com/items?itemName=worldlangteam.WorldEn">
    <img src="https://vsmarketplacebadges.dev/version-short/worldlangteam.WorldEn.svg" alt="Extensión de VS Code">
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
* 🔬 **[Prepublicación académica (ResearchGate)](https://www.researchgate.net/publication/377782413_A_Multilingual_Approach_with_Built-in_Code_Translation_and_Dynamic_Keyword_Importation)**
* 🧩 **[Extensión de VS Code WorldLangEN](https://marketplace.visualstudio.com/items?itemName=worldlangteam.WorldEn)**
* 👤 **Mantenedor:** Ziad Rabea ([LinkedIn](https://www.linkedin.com/in/ziadrabea/) | [Correo](mailto:zidr2005@gmail.com))

WorldLang es un intérprete de código abierto construido en Python que elimina la barrera del idioma en la programación. En lugar de tener que memorizar palabras clave en inglés, puedes escribir código utilizando sintaxis nativa — en árabe, francés, japonés y muchos otros idiomas.

El motor procesa y ejecuta el código mediante un pipeline personalizado de **Lexer → Parser → Runtime** y también admite detección automática del idioma y traducción de código fuente de WorldLang entre idiomas compatibles.

> **Idiomas compatibles: 31** — árabe, azerí, chino, neerlandés, inglés, finés, francés, alemán, griego, hindi, indonesio, irlandés, italiano, japonés, kazajo, coreano, kurdo, letón, malayo, persa, polaco, portugués, rumano, ruso, español, sueco, turco, ucraniano, urdu, uzbeko y vietnamita.

---

## Tabla de contenidos

- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Detección y selección del idioma](#detección-y-selección-del-idioma)
- [Traducción de código](#traducción-de-código)
- [Ejemplo de código](#ejemplo-de-código)
- [Bibliotecas integradas](#bibliotecas-integradas)
- [Arquitectura](#arquitectura)
- [Gestión de idiomas y bibliotecas](#gestión-de-idiomas-y-bibliotecas)
- [Contribuir](#contribuir)
- [Licencia](#licencia)

---

## Características

- **Programación en el idioma nativo** — escribe código utilizando las palabras clave de tu idioma elegido.
- **31 paquetes de idiomas compatibles** con mapeos de palabras clave cargados dinámicamente.
- **Selección híbrida del idioma** — selecciona manualmente un idioma o permite que WorldLang lo detecte automáticamente.
- **Detección del idioma mediante IA** — detecta automáticamente el idioma del código fuente cuando no se ha establecido uno manualmente.
- **Ejecución multilingüe** — ejecuta archivos escritos en diferentes idiomas compatibles sin tener que cambiar manualmente el idioma activo.
- **Traducción de código integrada** — traduce código fuente de WorldLang entre idiomas compatibles.
- **Mapeo dinámico de palabras clave** — el lexer asigna las palabras clave nativas a tokens genéricos durante la ejecución.
- **Intérprete completo** — variables, funciones, recursión, bucles, condicionales, listas, diccionarios y aritmética.
- **Hardware y robótica** — comunicación serie para microcontroladores como Arduino.
- **Voz** — conversión de texto a voz y reconocimiento de voz.
- **Bibliotecas integradas** — procesamiento de imágenes, gráficos, números aleatorios, sistema de archivos y más.
- **IA generativa** — integración opcional con Google Gemini.
- **Gestión de bibliotecas y extensiones** — descarga bibliotecas y extensiones `.world` directamente desde la red.

---

## Requisitos

- **Python 3.12+**
- **Windows, macOS o Linux**

Paquetes necesarios:

| Paquete | Uso |
|---------|-----|
| `requests` | Descarga de paquetes de idiomas, bibliotecas y extensiones |
| `numpy` | Detección del idioma mediante IA y procesamiento numérico |
| `keras` | Detección del idioma mediante IA |
| `nltk` | Preprocesamiento para la detección del idioma |
| `Pillow` | Procesamiento de imágenes (`_builtins/Image.py`) |
| `matplotlib` | Gráficos (`_builtins/Graph.py`) |
| `pyautogui` | Control del ratón y el teclado (`_builtins/Controls.py`) |
| `pyserial` | Comunicación serie y con hardware (`_builtins/Serial.py`) |
| `pyttsx3` | Texto a voz (`_builtins/Speech.py`) |
| `SpeechRecognition` | Reconocimiento de voz (`_builtins/Speech.py`) |
| `google-generativeai` | IA generativa (`_builtins/GenAI.py`) |
| `rich` | Renderizado de Markdown para las salidas de IA (`_builtins/GenAI.py`) |

> Solo `requests` es necesario para la funcionalidad básica del intérprete. `Keras`, `NLTK` y `NumPy` se necesitan para la detección automática del idioma mediante IA. Los demás paquetes solo son necesarios para sus respectivas bibliotecas integradas opcionales.

---

## Instalación

```bash
# 1. Clona el repositorio
git clone https://github.com/ZiadRabea/WorldLang.git
cd WorldLang

# 2. (Recomendado) Crea y activa un entorno virtual
python -m venv venv

# Windows:
venv\Scripts\activate

# macOS / Linux:
source venv/bin/activate

# 3. Instala las dependencias
pip install requests numpy keras nltk Pillow matplotlib pyautogui pyserial pyttsx3 SpeechRecognition rich
```

Para habilitar las funciones de IA de Google Gemini:

```bash
pip install google-generativeai
```

---

## Uso

El intérprete se distribuye como un REPL (bucle de lectura-evaluación-impresión). Para iniciarlo:

```bash
python bin/World.py
```

Aparece un indicador:

```text
World >>
```

Escribe un programa y pulsa Enter para ejecutarlo.

### Comandos especiales

| Comando | Acción |
|---|---|
| `libman` | Ejecutar el gestor de bibliotecas y descargar bibliotecas `.world` |
| `langman` | Ejecutar el gestor de idiomas y descargar/cambiar paquetes de idiomas |
| `extman` | Ejecutar el gestor de extensiones y descargar extensiones |
| `setlang` | Seleccionar manualmente un idioma o activar la detección automática |
| `world()` | Ejecutar un archivo de código fuente de WorldLang |
| `translate()` | Traducir código fuente de WorldLang entre idiomas compatibles |

---

## Detección y selección del idioma

WorldLang admite un **sistema híbrido de selección del idioma**.

Puedes seleccionar explícitamente el idioma que quieres utilizar o dejarlo sin especificar y permitir que WorldLang detecte automáticamente el idioma del código fuente.

### Selección manual del idioma

Utiliza:

```text
setlang
```

Ejemplo:

```text
setlang -> ArabicKW
```

Esto configura manualmente la tabla de palabras clave de árabe como idioma activo.

### Detección automática del idioma

Deja vacío el argumento del idioma:

```text
setlang -> ""
```

Esto activa la detección automática del idioma.

Cuando la detección automática está activada, WorldLang analiza el código fuente y determina el idioma adecuado durante la fase de análisis léxico/tokenización.

Esto permite ejecutar archivos y módulos importados escritos en diferentes idiomas compatibles **sin tener que cambiar manualmente el idioma activo de antemano**.

### Módulos de detección mediante IA

El sistema de detección automática del idioma utiliza:

- `Keras`
- `NLTK`
- `NumPy`

La detección automática es opcional cuando se selecciona manualmente un idioma mediante `setlang`.

---

## Traducción de código

WorldLang incluye un **traductor integrado de código entre idiomas**.

En lugar de traducir el código mediante simples sustituciones de texto, el traductor procesa el código fuente mediante un pipeline multilingüe estructurado:

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

Primero, el código fuente se convierte en representaciones independientes del idioma mediante el lexer. A continuación, el Translator asigna esas representaciones al idioma de destino antes de que el **DeLexer** reconstruya un código fuente válido de WorldLang.

### Comando Translate

```text
translate(filename.world, source_language, target_language)
```

Ejemplo:

```text
translate("factorial.world", "English", "Chinese")
```

WorldLang genera automáticamente un archivo de código fuente traducido utilizando el idioma de destino.

Por ejemplo:

```text
factorial_Chinese.world
```

De este modo, puedes escribir un programa de WorldLang en un idioma y convertirlo posteriormente a otro idioma compatible.

---

## Ejemplo de código

Una **calculadora de factorial recursiva** escrita completamente con palabras clave nativas en árabe:

```world
# حاسبة المضروب
متغير الرقم = عدد_صحيح(استقبل("أدخل رقماً"))

دالة مضروب(رقم)
    اذا رقم == 1 او رقم == 0 نفذ ارجاع 1
    ارجاع رقم * مضروب(رقم - 1)
نهاية

طباعة(مضروب(5))
```

El mismo programa también puede escribirse en inglés:

```worldlang
# Factorial Calculator
var number = int(input("Enter a number:"))

func factorial(number)
    if number == 1 or number == 0 do return 1
    return number * factorial(number - 1)
end

print(factorial(number))
```

Con la detección automática activada, WorldLang puede determinar qué idioma compatible utiliza el código fuente sin necesidad de seleccionarlo manualmente antes.

---

## Bibliotecas integradas

El intérprete proporciona varias bibliotecas respaldadas por Python, registradas como funciones nativas de WorldLang:

| Biblioteca | Propósito | Módulo de respaldo |
|---------|---------|----------------|
| `String` | `split`, `uppercase`, `lowercase`, `contains`, `replace`, ... | `_builtins/String.py` |
| `Random` | Generación de números aleatorios | `_builtins/Random.py` |
| `os` | Sistema de archivos: `chdir`, `mkdir`, `list_dir`, `move`, `system`, ... | `_builtins/os.py` |
| `Image` | Cargar/guardar imágenes y convertir a/de listas RGB | `_builtins/Image.py` |
| `Graph` | `plot`, `scatter`, `bar` para gráficos | `_builtins/Graph.py` |
| `Controls` | Automatización del ratón y el teclado | `_builtins/Controls.py` |
| `Serial` | Comunicación serie con hardware/Arduino (`send`/`receive`) | `_builtins/Serial.py` |
| `Speech` | Texto a voz y reconocimiento de voz | `_builtins/Speech.py` |
| `GenAI` | IA generativa mediante Google Gemini | `_builtins/GenAI.py` |

---

## Arquitectura

WorldLang es un **intérprete de recorrido de árboles** con una arquitectura ampliada para el procesamiento multilingüe.

### Pipeline de ejecución

```text
Código fuente
    ↓
Selección de idioma / Detección mediante IA
    ↓
Lexer
    ↓
Tokens
    ↓
Parser
    ↓
Árbol de Sintaxis Abstracta
    ↓
Runtime
    ↓
Resultado
```

La capa de detección determina la tabla de palabras clave adecuada antes de la tokenización cuando no se ha seleccionado manualmente ningún idioma.

### Pipeline de traducción

```text
Source
   ↓
Lexer
   ↓
Representación independiente del idioma
   ↓
Translator
   ↓
DeLexer
   ↓
Translated Source
```

Esta arquitectura permite a WorldLang ejecutar y traducir código fuente multilingüe manteniendo independiente del idioma la estructura interna del intérprete.

### Componentes principales

| Archivo / Componente | Función |
|---|---|
| `World.py` | Punto de entrada y shell del REPL |
| `Lexer.py` | Tokenizador; asigna dinámicamente las palabras clave del idioma detectado o seleccionado |
| `Parser.py` | Reglas gramaticales → generación del AST |
| `Interpreter.py` | Ejecuta el AST y proporciona la biblioteca estándar |
| `Tokens.py` | Tipos de tokens y gestión de palabras clave |
| `Translator.py` | Traduce representaciones tokenizadas entre idiomas compatibles |
| `DeLexer.py` | Reconstruye el código fuente utilizando las palabras clave del idioma de destino |
| `Errors.py` | Tipos de error (`IllegalChar`, `Syntax`, `Runtime`) |
| `RT_result.py` | Resultados de ejecución, contexto y tablas de símbolos |
| `datatypes/` | `Value`, `Number`, `String`, `List`, `Dict`, `Function` |
| `_builtins/` | Bibliotecas estándar respaldadas por Python |
| `data/` | Tablas de palabras clave y recursos multilingües |

Las tablas de palabras clave son archivos JSON basados en datos, lo que permite añadir nuevos idiomas sin tener que reescribir la gramática principal del intérprete.

---

## Gestión de idiomas y bibliotecas

WorldLang puede obtener recursos de la red durante la ejecución:

- **`langman`** — descargar tablas de palabras clave para idiomas adicionales en `data/`.
- **`libman`** — descargar bibliotecas `.world`.
- **`extman`** — descargar extensiones en `extensions/`.
- **`setlang`** — establecer manualmente un idioma o activar la detección automática mediante IA.
- **`world()`** — ejecutar archivos de código fuente de WorldLang.
- **`translate()`** — traducir código fuente de WorldLang entre idiomas compatibles.

> La detección de idiomas y la traducción utilizan la arquitectura de palabras clave multilingüe, lo que permite que diferentes paquetes de idiomas compartan la misma estructura subyacente del intérprete.

---

## Contribuir

WorldLang es de código abierto y está impulsado por la comunidad. Las contribuciones son bienvenidas de muchas formas:

- **Contribuidores de idiomas** — añadir o mejorar tablas de localización y palabras clave.
- **Desarrolladores del intérprete** — mejorar el lexer, parser, translator, DeLexer, runtime y la biblioteca estándar.
- **Desarrolladores de IA** — mejorar los modelos y el preprocesamiento para la detección automática del idioma.
- **Desarrolladores de hardware** — ampliar las integraciones de hardware y robótica.
- **Probadores** — descubrir errores y mejorar la fiabilidad.
- **Todos** — informar de problemas, mejorar la documentación y compartir ideas.

Para contribuir:

1. Haz un fork del repositorio.
2. Clona tu fork y crea una rama.
3. Realiza tus cambios y haz commit.
4. Abre un Pull Request hacia la rama `main`.

---

## Licencia

WorldLang se publica bajo la [Licencia MIT](LICENSE).
