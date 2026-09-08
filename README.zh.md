# WorldLang

<p align="center">

  <img src="images/world.png" alt="WorldLang 标志" width="200">

</p>

<p align="center">

  <a href="README.md">English</a> |

  <a href="README.ar.md">العربية</a> |

  <a href="README.fr.md">Français</a> |

  <a href="README.es.md">Español</a> |

  <a href="README.de.md">Deutsch</a> |

  <strong>中文</strong> |

  <a href="README.ja.md">日本語</a>

</p>

**一种多语言编程语言，允许您使用母语编写、运行、检测和翻译代码。**

<p align="center">

  <a href="https://github.com/ZiadRabea/WorldLang/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/ZiadRabea/WorldLang" alt="GitHub 许可证">
  </a>
  <br>
  <a href="https://marketplace.visualstudio.com/items?itemName=worldlangteam.WorldEn">
    <img src="https://vsmarketplacebadges.dev/version-short/worldlangteam.WorldEn.svg" alt="VSCode 扩展">
  </a>
  <br>
  <a href="https://www.researchgate.net/publication/377782413_A_Multilingual_Approach_with_Built-in_Code_Translation_and_Dynamic_Keyword_Importation">
    <img src="https://img.shields.io/badge/ResearchGate-preprint-brightgreen" alt="ResearchGate">
  </a>

</p>

**资源与链接：**

* 📖 **[官方文档](https://ziadrabea.github.io/WorldDocs)**
  * 🚀 [快速入门](https://ziadrabea.github.io/WorldDocs/installation.html)
  * 📚 [语言参考](https://ziadrabea.github.io/WorldDocs/features.html)
  * 🌍 [支持的语言](https://ziadrabea.github.io/WorldDocs/languages.html)
  * 🤝 [贡献指南](https://ziadrabea.github.io/WorldDocs/guide.html)

* 🌐 **[官方网站](https://ziadrabea.github.io/worldlanguage)**

* 💬 **[加入社区](https://flow.daisyscript.com)**

* 🔬 **[学术预印本 (ResearchGate)](https://www.researchgate.net/publication/377782413_A_Multilingual_Approach_with_Built-in_Code_Translation_and_Dynamic_Keyword_Importation)**

* 🧩 **[WorldLangEN VS Code 扩展](https://marketplace.visualstudio.com/items?itemName=worldlangteam.WorldEn)**

* 👤 **维护者：** Ziad Rabea ([LinkedIn](https://www.linkedin.com/in/ziadrabea/) | [邮箱](mailto:zidr2005@gmail.com))

WorldLang 是一个用 Python 构建的开源解释器，旨在消除编程中的语言障碍。您无需记忆英语关键字，而是使用所选语言的原生语法来编写代码。WorldLang 采用定制的 **Lexer → Parser → Runtime** 架构，并结合自动语言检测以及集成式源代码转换功能。

> **支持的语言：31 种** — 阿拉伯语、阿塞拜疆语、中文、荷兰语、英语、芬兰语、法语、德语、希腊语、印度尼西亚语、爱尔兰语、意大利语、日语、哈萨克语、韩语、库尔德语、拉脱维亚语、马来语、波斯语、波兰语、葡萄牙语、罗马尼亚语、俄语、西班牙语、瑞典语、土耳其语、乌克兰语、乌尔都语、乌兹别克语、越南语和印地语。

---

## 目录

* [特性](#特性)

* [系统要求](#系统要求)

* [安装](#安装)

* [使用方法](#使用方法)

* [语言检测与选择](#语言检测与选择)

* [代码翻译](#代码翻译)

* [代码示例](#代码示例)

* [内置库](#内置库)

* [架构](#架构)

* [语言与库管理](#语言与库管理)

* [参与贡献](#参与贡献)

* [许可证](#许可证)

---

## 特性

* **母语编程** — 使用所选语言的关键字编写代码。

* **31 个语言包**，通过动态加载的关键字映射提供。

* **混合语言选择** — 您可以手动选择语言，也可以让 WorldLang 自动检测语言。

* **基于 AI 的语言检测** — 当未手动选择语言时，在词法分析之前自动检测源代码使用的语言。

* **跨语言执行** — 无需手动切换全局语言，即可运行使用不同受支持语言编写的文件。

* **集成代码翻译** — 在受支持的语言之间翻译 WorldLang 源代码文件。

* **动态关键字映射** — 词法分析器会实时将母语关键字映射为通用 token。

* **功能完整的解释器** — 支持变量、函数、递归、循环、条件语句、列表、字典和算术运算。

* **硬件与机器人** — 通过串口与 Arduino 等微控制器通信。

* **语音功能** — 文本转语音和语音识别。

* **内置库** — 图像处理、绘图、随机数、文件系统等。

* **生成式 AI** — 可选的 Google Gemini 集成。

* **库与扩展管理** — 直接从网络获取 `.world` 库和扩展。

---

## 系统要求

* **Python 3.12+**

* **Windows、macOS 或 Linux**

核心功能所需的软件包：

| 软件包 | 用途 |
| --- | --- |
| `requests` | 下载语言包、库和扩展 |
| `numpy` | AI 语言检测和数值处理 |
| `keras` | 基于 AI 的语言检测 |
| `nltk` | 语言检测预处理 |
| `Pillow` | 图像处理（`_builtins/Image.py`） |
| `matplotlib` | 绘图（`_builtins/Graph.py`） |
| `pyautogui` | 鼠标/键盘控制（`_builtins/Controls.py`） |
| `pyserial` | 串口/硬件通信（`_builtins/Serial.py`） |
| `pyttsx3` | 文本转语音（`_builtins/Speech.py`） |
| `SpeechRecognition` | 语音识别（`_builtins/Speech.py`） |
| `google-generativeai` | 生成式 AI（`_builtins/GenAI.py`） |
| `rich` | AI 输出的 Markdown 渲染（`_builtins/GenAI.py`） |

> 仅 `requests` 是基础解释器的必需包。`Keras`、`NLTK` 和 `NumPy` 用于基于 AI 的自动语言检测。其余软件包仅在使用对应的可选内置库时需要。

---

## 安装

```bash
# 1. 克隆仓库

git clone https://github.com/ZiadRabea/WorldLang.git

cd WorldLang

# 2. （推荐）创建并激活虚拟环境

python -m venv venv

# Windows:

venv\Scripts\activate

# macOS / Linux:

source venv/bin/activate

# 3. 安装依赖

pip install requests numpy keras nltk Pillow matplotlib pyautogui pyserial pyttsx3 SpeechRecognition rich
```

如需启用 Google Gemini AI 功能：

```bash
pip install google-generativeai
```

---

## 使用方法

该解释器以 REPL（读取-求值-打印循环）形式运行。启动方式：

```bash
python bin/World.py
```

启动后会出现提示符：

```text
World >>
```

输入程序并按回车键即可执行。

### 特殊命令

| 命令 | 功能 |
| --- | --- |
| `world()` | 运行 WorldLang 源代码文件 |
| `libman` | 运行库管理器并下载 `.world` 库 |
| `langman` | 运行语言管理器并下载语言包 |
| `extman` | 运行扩展管理器并下载扩展 |
| `setlang` | 手动选择编程语言或启用自动检测 |
| `translate()` | 在受支持的语言之间翻译 WorldLang 源代码 |

---

## 语言检测与选择

WorldLang 支持**混合语言选择系统**。

您可以明确选择要使用的语言，也可以不设置语言，让解释器自动检测源代码所使用的语言。

### 手动选择语言

使用：

```text
setlang
```

示例：

```text
setlang -> ArabicKW
```

这会将 WorldLang 配置为使用阿拉伯语关键字表。

### 自动语言检测

将语言输入留空：

```text
setlang -> ""
```

这会启用自动语言检测。

启用自动检测后，WorldLang 会在词法分析/标记化阶段分析源代码，并确定合适的语言。

这样一来，使用不同受支持语言编写的代码及其导入模块可以**无需事先手动切换当前语言**即可运行。

### AI 检测模块

自动语言检测系统使用：

* `Keras`
* `NLTK`
* `NumPy`

手动使用 `setlang` 选择语言时，不要求启用检测系统。

---

## 代码翻译

WorldLang 内置**跨语言代码翻译器**。

它并非简单地使用文本替换，而是通过结构化的多语言处理管道来翻译源代码：

```text
源代码

   ↓

Lexer

   ↓

Translator

   ↓

DeLexer

   ↓

翻译后的源代码
```

源代码首先会被词法分析为与语言无关的表示形式。随后，Translator 将这些表示映射到目标语言，最后由 **DeLexer** 根据目标语言的关键字重建有效的 WorldLang 源代码。

### Translate 命令

```text
translate(filename.world, source_language, target_language)
```

示例：

```text
translate("factorial.world", "English", "Chinese")
```

WorldLang 会根据目标语言自动生成翻译后的源文件。

例如：

```text
factorial_Chinese.world
```

这样，您可以先使用一种语言编写 WorldLang 程序，再将同一份源代码转换为另一种受支持的语言。

---

## 代码示例

下面的阶乘计算器可以完全使用阿拉伯语编写：

```worldlang
# حاسبة المضروب

متغير الرقم = عدد_صحيح(استقبل("أدخل رقماً"))

دالة مضروب(رقم)

    اذا رقم == 1 او رقم == 0 نفذ ارجاع 1

    ارجاع رقم * مضروب(رقم - 1)

نهاية

طباعة(مضروب(الرقم))
```

同一个程序也可以使用英语编写：

```worldlang
# Factorial Calculator

var number = int(input("Enter a number:"))

func factorial(number)

    if number == 1 or number == 0 do return 1

    return number * factorial(number - 1)

end

print(factorial(number))
```

启用自动检测后，WorldLang 可以判断源代码所使用的受支持语言，而无需手动更改语言。

---

## 内置库

解释器提供了多个基于 Python 的库，并将其注册为 WorldLang 的原生函数：

| 库名 | 用途 | 底层模块 |
| --- | --- | --- |
| `String` | `split`、`uppercase`、`lowercase`、`contains`、`replace`…… | `_builtins/String.py` |
| `Random` | 随机数生成 | `_builtins/Random.py` |
| `os` | 文件系统：`chdir`、`mkdir`、`list_dir`、`move`、`system`…… | `_builtins/os.py` |
| `Image` | 加载/保存图像，以及与 RGB 列表相互转换 | `_builtins/Image.py` |
| `Graph` | `plot`、`scatter`、`bar` 图表绘制 | `_builtins/Graph.py` |
| `Controls` | 鼠标/键盘自动化 | `_builtins/Controls.py` |
| `Serial` | 硬件/Arduino 串口通信（`send`/`receive`） | `_builtins/Serial.py` |
| `Speech` | 文本转语音和语音识别 | `_builtins/Speech.py` |
| `GenAI` | 通过 Google Gemini 实现生成式 AI | `_builtins/GenAI.py` |

---

## 架构

WorldLang 是一个**树遍历解释器**，并采用扩展的多语言处理架构。

### 代码执行管道

```text
源代码

    ↓

语言选择 / AI 检测

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

结果
```

当未手动选择语言时，语言检测层会在词法分析之前动态确定应使用的关键字表。

### 代码翻译管道

```text
源代码

   ↓

Lexer

   ↓

语言无关表示

   ↓

Translator

   ↓

DeLexer

   ↓

翻译后的源代码
```

这种架构使 WorldLang 能够执行和翻译多语言源代码，同时保持底层解释器管道与具体语言无关。

### 核心组件

| 文件 / 组件 | 职责 |
| --- | --- |
| `World.py` | 入口点和 REPL Shell |
| `Lexer.py` | 词法分析器；从检测到或选择的语言表动态映射关键字 |
| `Parser.py` | 语法规则和 AST 生成 |
| `Interpreter.py` | 执行 AST 并提供标准库 |
| `Tokens.py` | Token 类型和关键字处理 |
| `Translator.py` | 在受支持语言之间转换词法化的源代码表示 |
| `DeLexer.py` | 使用目标语言的关键字映射重新构建源代码 |
| `Errors.py` | 错误类型（`IllegalChar`、`Syntax`、`Runtime`） |
| `RT_result.py` | 运行时结果、上下文和符号表 |
| `datatypes/` | `Value`、`Number`、`String`、`List`、`Dict`、`Function` |
| `_builtins/` | 基于 Python 的标准库 |
| `data/` | 关键字表和多语言资源 |

关键字表采用数据驱动的 JSON 文件，使新增语言无需重写核心解释器语法。

---

## 语言与库管理

WorldLang 可以在运行时从网络获取资源：

* **`langman`** — 将其他语言的关键字表下载到 `data/`。

* **`libman`** — 下载 `.world` 库。

* **`extman`** — 将扩展下载到 `extensions/`。

* **`setlang`** — 手动配置语言，或启用基于 AI 的自动语言检测。

* **`translate()`** — 在受支持的语言之间转换 WorldLang 源代码文件。

> 语言检测和代码翻译都建立在多语言关键字架构之上，因此不同语言包可以共享底层解释器。

---

## 参与贡献

WorldLang 是一个开源、社区驱动的项目。欢迎通过多种方式贡献：

* **语言贡献者** — 添加或改进本地化和关键字表。

* **编译器开发者** — 改进 Lexer、Parser、Translator、DeLexer、Runtime 和标准库。

* **AI 开发者** — 改进自动语言检测模型和预处理流程。

* **硬件开发者** — 扩展硬件与机器人集成。

* **测试者** — 发现 bug 并提高可靠性。

* **所有人** — 报告问题、改进文档和分享想法。

参与方式：

1. Fork 本仓库。

2. 克隆您的 Fork 并创建一个分支。

3. 进行修改并提交。

4. 向 `main` 分支发起 Pull Request。

---

## 许可证

WorldLang 在 [MIT 许可证](LICENSE) 下发布。
