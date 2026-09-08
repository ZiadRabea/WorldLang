# WorldLang

<p align="center">
  <img src="images/world.png" alt="WorldLang ロゴ" width="200">
</p>

<p align="center">
  <a href="README.md">English</a> |
  <a href="README.ar.md">العربية</a> |
  <a href="README.fr.md">Français</a> |
  <a href="README.es.md">Español</a> |
  <a href="README.de.md">Deutsch</a> |
  <a href="README.zh.md">中文</a> |
  <strong>日本語</strong>
</p>

**ネイティブ言語でコードを記述・実行・検出・翻訳できる多言語プログラミング言語。**

<p align="center">
  <a href="https://github.com/ZiadRabea/WorldLang/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/ZiadRabea/WorldLang" alt="GitHub ライセンス">
  </a>
  <br>
  <a href="https://marketplace.visualstudio.com/items?itemName=worldlangteam.WorldEn">
    <img src="https://vsmarketplacebadges.dev/version-short/worldlangteam.WorldEn.svg" alt="VSCode 拡張機能">
  </a>
  <br>
  <a href="https://www.researchgate.net/publication/377782413_A_Multilingual_Approach_with_Built-in_Code_Translation_and_Dynamic_Keyword_Importation">
    <img src="https://img.shields.io/badge/ResearchGate-preprint-brightgreen" alt="ResearchGate">
  </a>
</p>

**リソースとリンク:**

* 📖 **[公式ドキュメント](https://ziadrabea.github.io/WorldDocs)**
  * 🚀 [はじめに](https://ziadrabea.github.io/WorldDocs/installation.html)
  * 📚 [言語リファレンス](https://ziadrabea.github.io/WorldDocs/features.html)
  * 🌍 [対応言語](https://ziadrabea.github.io/WorldDocs/languages.html)
  * 🤝 [コントリビューションガイド](https://ziadrabea.github.io/WorldDocs/guide.html)
* 🌐 **[公式ウェブサイト](https://ziadrabea.github.io/worldlanguage)**
* 💬 **[コミュニティに参加](https://flow.daisyscript.com)**
* 🔬 **[学術プレプリント (ResearchGate)](https://www.researchgate.net/publication/377782413_A_Multilingual_Approach_with_Built-in_Code_Translation_and_Dynamic_Keyword_Importation)**
* 🧩 **[WorldLangEN VS Code 拡張機能](https://marketplace.visualstudio.com/items?itemName=worldlangteam.WorldEn)**
* 👤 **メンテナー:** Ziad Rabea ([LinkedIn](https://www.linkedin.com/in/ziadrabea/) | [メール](mailto:zidr2005@gmail.com))

WorldLangはPythonで構築されたオープンソースのインタープリターで、プログラミングにおける言語障壁を取り除きます。英語のキーワードを暗記する代わりに、選択した言語のネイティブ構文を使用してコードを記述できます。WorldLangは、カスタム **Lexer → Parser → Runtime** アーキテクチャに加え、自動言語検出と組み込みのソースコード間翻訳を備えた多言語実行パイプラインを提供します。

> **対応言語: 31** — アラビア語、アゼルバイジャン語、中国語、オランダ語、英語、フィンランド語、フランス語、ドイツ語、ギリシャ語、インドネシア語、アイルランド語、イタリア語、日本語、カザフ語、韓国語、クルド語、ラトビア語、マレー語、ペルシャ語、ポーランド語、ポルトガル語、ルーマニア語、ロシア語、スペイン語、スウェーデン語、トルコ語、ウクライナ語、ウルドゥー語、ウズベク語、ベトナム語、ヒンディー語。

---

## 目次

* [主な特徴](#主な特徴)
* [環境要件](#環境要件)
* [インストール](#インストール)
* [使い方](#使い方)
* [言語の検出と選択](#言語の検出と選択)
* [コード翻訳](#コード翻訳)
* [コード例](#コード例)
* [組み込みライブラリ](#組み込みライブラリ)
* [アーキテクチャ](#アーキテクチャ)
* [言語・ライブラリ管理](#言語ライブラリ管理)
* [コントリビューション](#コントリビューション)
* [ライセンス](#ライセンス)

---

## 主な特徴

* **ネイティブ言語プログラミング** — 選択した言語のキーワードを使用してコードを記述。
* **31の対応言語パック** — 動的に読み込まれるキーワードマッピングを提供。
* **ハイブリッド言語選択** — 言語を手動で選択するか、WorldLangに自動検出させることが可能。
* **AIベースの言語検出** — 言語が手動指定されていない場合、レキシング前にコード構文から言語を自動検出。
* **クロス言語実行** — アクティブなグローバル言語を手動で切り替えなくても、異なる対応言語で書かれたファイルを実行可能。
* **組み込みコード翻訳** — WorldLangのソースファイルを対応言語間で翻訳。
* **動的キーワードマッピング** — レキサーがネイティブキーワードを汎用トークンへ動的にマッピング。
* **フル機能のインタープリター** — 変数、関数、再帰、ループ、条件分岐、リスト、ディクショナリ、算術演算に対応。
* **ハードウェア＆ロボティクス** — Arduinoなどのマイクロコントローラーとのシリアル通信。
* **音声** — テキスト読み上げと音声認識。
* **組み込みライブラリ** — 画像処理、グラフ描画、ランダム処理、ファイルシステム操作など。
* **生成AI** — オプションのGoogle Gemini統合。
* **ライブラリ＆拡張管理** — ネットワークから直接 `.world` ライブラリや拡張を取得。

---

## 環境要件

* **Python 3.12+**
* **Windows、macOS、またはLinux**

コアパッケージ:

| パッケージ | 用途 |
|---|---|
| `requests` | 言語パック、ライブラリ、拡張のダウンロード |
| `numpy` | AI言語検出と数値処理 |
| `keras` | AIベースの言語検出 |
| `nltk` | 言語検出の前処理 |
| `Pillow` | 画像処理 (`_builtins/Image.py`) |
| `matplotlib` | グラフ描画 (`_builtins/Graph.py`) |
| `pyautogui` | マウス/キーボード制御 (`_builtins/Controls.py`) |
| `pyserial` | シリアル/ハードウェア通信 (`_builtins/Serial.py`) |
| `pyttsx3` | テキスト読み上げ (`_builtins/Speech.py`) |
| `SpeechRecognition` | 音声認識 (`_builtins/Speech.py`) |
| `google-generativeai` | 生成AI (`_builtins/GenAI.py`) |
| `rich` | AI出力のMarkdownレンダリング (`_builtins/GenAI.py`) |

> 基本インタープリターには `requests` のみが必要です。AIベースの自動言語検出には `Keras`、`NLTK`、`NumPy` が必要です。その他のパッケージは、それぞれ対応するオプションの組み込みライブラリを使用する場合にのみ必要です。

---

## インストール

```bash
# 1. リポジトリをクローン
git clone https://github.com/ZiadRabea/WorldLang.git
cd WorldLang

# 2. （推奨）仮想環境を作成して有効化
python -m venv venv

# Windows:
venv\Scripts\activate

# macOS / Linux:
source venv/bin/activate

# 3. 依存関係をインストール
pip install requests numpy keras nltk Pillow matplotlib pyautogui pyserial pyttsx3 SpeechRecognition rich
```

Google Gemini AI機能を有効にするには、追加で以下を実行します:

```bash
pip install google-generativeai
```

---

## 使い方

インタープリターはREPL（Read–Eval–Print Loop）として提供されます。起動するには:

```bash
python bin/World.py
```

プロンプトが表示されます:

```text
World >>
```

プログラムを入力してEnterキーを押すと実行されます。

### 特別なコマンド

| コマンド | アクション |
|---|---|
| `world()` | WorldLangソースファイルを実行 |
| `libman` | ライブラリマネージャーを実行し、`.world` ライブラリをダウンロード |
| `langman` | 言語マネージャーを実行し、言語パックをダウンロード |
| `extman` | 拡張マネージャーを実行し、拡張をダウンロード |
| `setlang` | プログラミング言語を手動選択、または自動検出を有効化 |
| `translate()` | 対応言語間でWorldLangソースコードを翻訳 |

---

## 言語の検出と選択

WorldLangは**ハイブリッド言語選択システム**をサポートしています。

使用する言語を明示的に選択することも、言語を未設定のままにしてソースコードの言語を自動検出させることもできます。

### 手動での言語選択

以下を使用します:

```text
setlang
```

例:

```text
setlang -> ArabicKW
```

これにより、WorldLangはアラビア語のキーワードテーブルを使用するよう手動で設定されます。

### 自動言語検出

言語入力を空白のままにします:

```text
setlang -> ""
```

これにより、自動言語検出が有効になります。

自動検出が有効な場合、WorldLangはソースコードを分析し、レキシング/トークン化の段階で適切な言語を判定します。

これにより、**事前にアクティブな言語を手動で切り替えなくても、異なる対応言語で書かれたコードやインポートされたモジュールを実行できます。**

### AI検出モジュール

自動言語検出システムでは以下を使用します:

* `Keras`
* `NLTK`
* `NumPy`

言語を `setlang` で手動指定する場合、これらのAI検出機能は必須ではありません。

---

## コード翻訳

WorldLangには、**クロス言語コード翻訳機能**が組み込まれています。

単純なテキスト置換ではなく、翻訳システムは構造化された多言語パイプラインを使用します:

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

ソースコードはまず言語に依存しない表現へトークン化されます。次にTranslatorがその表現を対象言語へマッピングし、**DeLexer**が有効なWorldLangソースコードとして再構築します。

### Translateコマンド

```text
translate(filename.world, source_language, target_language)
```

例:

```text
translate("factorial.world", "English", "Chinese")
```

WorldLangは対象言語を使用した翻訳済みソースファイルを自動生成します。

例:

```text
factorial_Chinese.world
```

これにより、ある言語で記述したWorldLangプログラムを、対応する別の言語へ変換できます。

---

## コード例

以下の階乗計算機はアラビア語で記述できます:

```worldlang
# حاسبة المضروب

متغير الرقم = عدد_صحيح(استقبل("أدخل رقماً"))

دالة مضروب(رقم)
    اذا رقم == 1 او رقم == 0 نفذ ارجاع 1
    ارجاع رقم * مضروب(رقم - 1)
نهاية

طباعة(مضروب(الرقم))
```

同じプログラムを英語で記述することもできます:

```worldlang
# Factorial Calculator

var number = int(input("Enter a number:"))

func factorial(number)
    if number == 1 or number == 0 do return 1
    return number * factorial(number - 1)
end

print(factorial(number))
```

自動検出が有効な場合、WorldLangは手動で言語を変更しなくても、ソースコードがどの対応言語で記述されているかを判定できます。

---

## 組み込みライブラリ

インタープリターは、ネイティブWorldLang関数として登録された複数のPythonベースライブラリを提供します:

| ライブラリ | 用途 | バックエンドモジュール |
|---|---|---|
| `String` | `split`, `uppercase`, `lowercase`, `contains`, `replace`, ... | `_builtins/String.py` |
| `Random` | ランダム数生成 | `_builtins/Random.py` |
| `os` | ファイルシステム操作: `chdir`, `mkdir`, `list_dir`, `move`, `system`, ... | `_builtins/os.py` |
| `Image` | 画像の読み込み/保存、RGBリストとの相互変換 | `_builtins/Image.py` |
| `Graph` | `plot`, `scatter`, `bar` によるグラフ描画 | `_builtins/Graph.py` |
| `Controls` | マウス/キーボード自動化 | `_builtins/Controls.py` |
| `Serial` | ハードウェア/Arduinoとのシリアル通信 (`send`/`receive`) | `_builtins/Serial.py` |
| `Speech` | テキスト読み上げと音声認識 | `_builtins/Speech.py` |
| `GenAI` | Google Geminiによる生成AI | `_builtins/GenAI.py` |

---

## アーキテクチャ

WorldLangは**ツリー走査インタープリター**であり、拡張された多言語処理アーキテクチャを採用しています。

### コード実行パイプライン

```text
Source Code
    ↓
Language Selection / AI Detection
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
Result
```

手動で言語が選択されていない場合、言語検出層がトークン化前に使用するキーワードテーブルを動的に決定します。

### コード翻訳パイプライン

```text
Source
   ↓
Lexer
   ↓
Language-Independent Representation
   ↓
Translator
   ↓
DeLexer
   ↓
Translated Source
```

この構成により、WorldLangは内部のインタープリターパイプラインを言語に依存しない形で維持しながら、多言語ソースコードを実行・翻訳できます。

### 主要コンポーネント

| ファイル / コンポーネント | 役割 |
|---|---|
| `World.py` | エントリーポイントとREPLシェル |
| `Lexer.py` | トークナイザー。検出または選択された言語テーブルからキーワードを動的にマッピング |
| `Parser.py` | 文法規則とAST生成 |
| `Interpreter.py` | ASTを実行し、標準ライブラリを提供 |
| `Tokens.py` | トークン型とキーワード処理 |
| `Translator.py` | 対応言語間でトークン化されたソース表現を変換 |
| `DeLexer.py` | 対象言語のキーワードマッピングを用いてソースコードを再構築 |
| `Errors.py` | エラー型 (`IllegalChar`, `Syntax`, `Runtime`) |
| `RT_result.py` | ランタイム結果、コンテキスト、シンボルテーブル |
| `datatypes/` | `Value`, `Number`, `String`, `List`, `Dict`, `Function` |
| `_builtins/` | Pythonベースの標準ライブラリ |
| `data/` | 言語キーワードテーブルと多言語リソース |

キーワードテーブルはデータ駆動型のJSONファイルで管理されているため、コアとなるインタープリターの文法を書き換えることなく新しい言語を追加できます。

---

## 言語・ライブラリ管理

WorldLangは実行時にネットワークからリソースを取得できます:

* **`langman`** — 追加言語のキーワードテーブルを `data/` にダウンロード。
* **`libman`** — `.world` ライブラリをダウンロード。
* **`extman`** — 拡張を `extensions/` にダウンロード。
* **`setlang`** — 言語を手動設定、またはAIベースの自動言語検出を有効化。
* **`translate()`** — WorldLangソースファイルを対応言語間で変換。

> 言語検出と翻訳はいずれも多言語キーワードアーキテクチャ上で動作し、異なる言語パックが同じ基盤となるインタープリターを共有できます。

---

## コントリビューション

WorldLangはオープンソースでコミュニティ主導のプロジェクトです。さまざまな形での貢献を歓迎します:

* **言語コントリビューター** — ローカライズとキーワードテーブルを追加・改善。
* **コンパイラー開発者** — レキサー、パーサー、Translator、DeLexer、ランタイム、標準ライブラリを改善。
* **AI開発者** — 自動言語検出モデルと前処理を改善。
* **ハードウェア開発者** — ハードウェア・ロボティクス統合を拡張。
* **テスター** — バグを発見し、信頼性を向上。
* **すべての人** — Issueを報告し、ドキュメントを改善し、アイデアを共有。

貢献するには:

1. リポジトリをフォーク。
2. フォークをクローンし、ブランチを作成。
3. 変更を加えてコミット。
4. `main` ブランチに対してPull Requestを作成。

---

## ライセンス

WorldLangは [MITライセンス](LICENSE) の下で公開されています。
