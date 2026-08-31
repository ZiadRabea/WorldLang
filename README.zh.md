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
  <strong>中文</strong>
</p>

**一种多语言编程语言，允许您使用母体语言编写和运行代码。**

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

WorldLang 是一个用 Python 构建的开源解释器，旨在消除编程中的语言障碍。您无需记忆英语关键字，而是使用母体语法编写代码——支持阿拉伯语、法语、日语等 21 种语言——引擎通过自定义的 Lexer → Parser → Runtime 管道对其进行词法分析和执行。

> **支持的语言：21 种** — Arabic, Chinese, Dutch, English, French, German, Indonesian, Italian, Japanese, Kazakh, Korean, Persian, Polish, Portuguese, Romanian, Russian, Spanish, Turkish, Ukrainian, Urdu, Vietnamese.

---

## 目录

- [特性](#features)
- [系统要求](#requirements)
- [安装](#installation)
- [使用方法](#usage)
- [代码示例](#code-example)
- [内置库](#built-in-libraries)
- [架构](#architecture)
- [语言与库管理](#language--library-management)
- [参与贡献](#contributing)
- [许可证](#license)

---

## 特性

- **母体语言编程** — 使用您所选语言的关键字编写代码。
- **21 个语言包** 以 JSON 关键字表的形式存放在 `data/` 中。
- **动态关键字映射** — 词法分析器实时将母体关键字映射为通用 token。
- **功能完整的解释器** — 支持变量、函数、递归、循环、条件语句、列表、字典和算术运算。
- **硬件与机器人** — 通过串口通信与微控制器交互（例如 Arduino）。
- **语音功能** — 文本转语音和语音识别。
- **内置库** — 图像处理、绘图、随机数、文件系统等。
- **生成式 AI** — 可选的 Google Gemini 集成。
- **库与扩展管理** — 直接从网络获取 `.world` 库和扩展。

---

## 系统要求

- **Python 3.12+**
- **Windows、macOS 或 Linux**

核心功能所需的基础包（参见[安装](#installation)）：

| 包名 | 用途 |
|---------|----------|
| `requests` | 下载语言包、库和扩展 |
| `Pillow` | 图像处理（`_builtins/Image.py`） |
| `matplotlib` & `numpy` | 绘图（`_builtins/Graph.py`） |
| `pyautogui` | 鼠标/键盘控制（`_builtins/Controls.py`） |
| `pyserial` | 串口/硬件通信（`_builtins/Serial.py`） |
| `pyttsx3` | 文本转语音（`_builtins/Speech.py`） |
| `SpeechRecognition` | 语音识别（`_builtins/Speech.py`） |
| `google-generativeai` | 生成式 AI（`_builtins/GenAI.py`） |
| `rich` | AI 输出的 Markdown 渲染（`_builtins/GenAI.py`） |

> 仅 `requests` 是核心功能的必需包。其余包仅在使用上述特定的可选内置库时才需要。

---

## 安装

```bash
# 1. Clone the repository
git clone https://github.com/jabar-reda/WorldLang.git
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

如需启用 AI 功能，还需额外安装：

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

```
World >>
```

输入程序并按回车键即可执行。提示符下可用的特殊命令：

| 命令 | 功能 |
|------------|---------------------------------------------------------------|
| `libman`   | 运行库管理器（下载 `.world` 库）         |
| `langman`  | 运行语言管理器（下载/切换语言包）     |
| `extman`   | 运行扩展管理器（下载扩展）               |

`WorldLang` 默认使用阿拉伯语。阿拉伯语关键字从 `bin/keywords.json` 加载。可通过 `langman` 管理器切换或添加语言。

---

## 代码示例

一个完全使用阿拉伯语母体关键字编写的递归**阶乘计算器**：

```world
# حاسبة المضروب
متغير الرقم = عدد_صحيح(استقبل("أدخل رقماً"))

دالة مضروب(رقم)
    اذا رقم == 1 او رقم == 0 نفذ ارجاع 1
    ارجاع رقم * مضروب(رقم - 1)
نهاية

طباعة(مضروب(5))
```

词法分析器的读取方式：

| 阿拉伯语关键字 | 含义 |
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

## 内置库

解释器提供了多个基于 Python 的库，注册为 WorldLang 的原生函数：

| 库名 | 用途 | 底层模块 |
|---------|---------|----------------|
| `String` | `split`、`uppercase`、`lowercase`、`contains`、`replace`…… | `_builtins/String.py` |
| `Random` | 随机数生成 | `_builtins/Random.py` |
| `os` | 文件系统：`chdir`、`mkdir`、`list_dir`、`move`、`system`…… | `_builtins/os.py` |
| `Image` | 加载/保存图像（与 RGB 列表互转） | `_builtins/Image.py` |
| `Graph` | `plot`、`scatter`、`bar` 图表绘制 | `_builtins/Graph.py` |
| `Controls` | 鼠标/键盘自动化 | `_builtins/Controls.py` |
| `Serial` | 硬件/Arduino 串口通信（`send`/`receive`） | `_builtins/Serial.py` |
| `Speech` | 文本转语音和语音识别 | `_builtins/Speech.py` |
| `GenAI` | 通过 Google Gemini 实现生成式 AI | `_builtins/GenAI.py` |

---

## 架构

WorldLang 是一个**树遍历解释器**。源代码经过三阶段管道处理：

```
1. Lexer  ──→  Tokens (native keywords mapped to generic tokens)
2. Parser ──→  AST  (language-agnostic Abstract Syntax Tree)
3. Runtime ──→ Result (interpreter walks the AST, managing symbols & scope)
```

**`bin/` 目录中的核心组件：**

| 文件 | 职责 |
|------|------|
| `World.py` | 入口点 — REPL 交互界面 |
| `Lexer.py` | 词法分析器；从当前语言表动态映射关键字 |
| `Parser.py` | 语法规则 → AST 生成 |
| `Interpreter.py` | 执行 AST 并提供标准库 |
| `Tokens.py` | Token 类型定义；加载关键字表（`keywords.json`） |
| `Errors.py` | 错误类型（`IllegalChar`、`Syntax`、`Runtime`） |
| `RT_result.py` | 运行时结果、上下文和符号表 |
| `datatypes/` | `Value`、`Number`、`String`、`List`、`Dict`、`Function` |
| `_builtins/` | 基于 Python 的标准库 |

关键字表是 `data/` 下的纯 JSON 文件（每种语言一个，例如 `Arabic_KW.json`），使引擎的语言支持完全由数据驱动。

---

## 语言与库管理

WorldLang 可以在运行时从网络获取资源：

- **`langman`** — 将额外语言的关键字表下载到 `data/` 目录。
- **`libman`** — 下载 `.world` 库（例如 `math.world`、`json_ar.world`）。
- **`extman`** — 将扩展下载到 `extensions/` 目录（例如语音编码扩展 `vcode.world`）。

> 这些功能需要网络连接以及对解释器所引用的远程资源仓库的访问权限。

---

## 参与贡献

WorldLang 是一个开源的社区驱动项目。欢迎以多种形式参与贡献：

- **语言贡献者** — 添加或改进本地化表（`data/*_KW.json`）。
- **编译器开发者** — 改进词法分析器、语法分析器、运行时和标准库。
- **硬件开发者** — 扩展硬件和机器人集成。
- **测试者** — 发现 bug 并提高可靠性。
- **所有人** — 报告问题、改进文档、分享想法。

参与方式：

1. Fork 本仓库。
2. 克隆您的 Fork 并创建一个分支。
3. 进行修改并提交。
4. 向 `main` 分支发起 Pull Request。

---

## 许可证

WorldLang 在 [MIT 许可证](LICENSE) 下发布。
