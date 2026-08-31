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

**ネイティブ言語でコードを記述・実行できる多言語プログラミング言語。**

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

WorldLangはPythonで構築されたオープンソースのインタープリターで、プログラミングにおける言語障壁を取り除きます。英語のキーワードを暗記する代わりに、選択した言語のネイティブ構文を使用してコードを記述します — アラビア語、フランス語、日本語、その他18の言語 — エンジンはカスタム Lexer → Parser → Runtime パイプラインを通じてトークン化し、実行します。

> **対応言語: 21** — アラビア語、中国語、オランダ語、英語、フランス語、ドイツ語、インドネシア語、イタリア語、日本語、カザフ語、韓国語、ペルシャ語、ポーランド語、ポルトガル語、ルーマニア語、ロシア語、スペイン語、トルコ語、ウクライナ語、ウルドゥー語、ベトナム語。

---

## 目次

- [主な特徴](#主な特徴)
- [環境要件](#環境要件)
- [インストール](#インストール)
- [使い方](#使い方)
- [コード例](#コード例)
- [組み込みライブラリ](#組み込みライブラリ)
- [アーキテクチャ](#アーキテクチャ)
- [言語・ライブラリ管理](#言語・ライブラリ管理)
- [コントリビューション](#コントリビューション)
- [ライセンス](#ライセンス)

---

## 主な特徴

- **ネイティブ言語プログラミング** — 選択した言語のキーワードを使用してコードを記述。
- **21の言語パック** が `data/` にJSONキーワードテーブルとして同梱。
- **動的キーワードマッピング** — レキサーがネイティブキーワードを汎用トークンに動的にマッピング。
- **フル機能のインタープリター** — 変数、関数、再帰、ループ、条件分岐、リスト、ディクショナリ、算術演算。
- **ハードウェア＆ロボティクス** — マイコン（Arduinoなど）とのシリアル通信。
- **音声** — テキスト読み上げと音声認識。
- **組み込みライブラリ** — 画像処理、グラフ描画、ランダム、ファイルシステムなど。
- **生成AI** — オプションのGoogle Gemini統合。
- **ライブラリ・拡張管理** — ネットワークから直接 `.world` ライブラリや拡張を取得。

---

## 環境要件

- **Python 3.12+**
- **Windows、macOS、またはLinux**

コアパッケージ（[インストール](#インストール)を参照）:

| パッケージ | 用途 |
|---------|----------|
| `requests` | 言語パック、ライブラリ、拡張のダウンロード |
| `Pillow` | 画像処理 (`_builtins/Image.py`) |
| `matplotlib` & `numpy` | グラフ描画 (`_builtins/Graph.py`) |
| `pyautogui` | マウス/キーボード制御 (`_builtins/Controls.py`) |
| `pyserial` | シリアル/ハードウェア通信 (`_builtins/Serial.py`) |
| `pyttsx3` | テキスト読み上げ (`_builtins/Speech.py`) |
| `SpeechRecognition` | 音声認識 (`_builtins/Speech.py`) |
| `google-generativeai` | 生成AI (`_builtins/GenAI.py`) |
| `rich` | AI出力のMarkdownレンダリング (`_builtins/GenAI.py`) |

> コア機能には `requests` のみが必要です。残りのパッケージは、上記で指定された特定のオプション組み込みライブラリにのみ必要です。

---

## インストール

```bash
# 1. リポジトリをクローン
git clone https://github.com/ZiadRabea/WorldLang.git
cd WorldLang

# 2. （推推奨）仮想環境を作成して有効化
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS / Linux:
source venv/bin/activate

# 3. 依存関係をインストール
pip install requests Pillow matplotlib numpy pyautogui pyserial pyttsx3 SpeechRecognition rich
```

AI機能を有効にするには、追加で以下が必要です:

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

```
World >>
```

プログラムを入力し、Enterキーを押して実行します。プロンプトで使用できる特別なコマンド:

| コマンド    | アクション                                                        |
|------------|---------------------------------------------------------------|
| `libman`   | ライブラリマネージャーを実行（`.world` ライブラリのダウンロード）         |
| `langman`  | 言語マネージャーを実行（言語パックのダウンロード/切り替え）     |
| `extman`   | 拡張マネージャーを実行（拡張のダウンロード）               |

`WorldLang` はデフォルトでアラビア語です。アラビア語のキーワードは `bin/keywords.json` から読み込まれます。`langman` マネージャーで言語の切り替えや追加を行います。

---

## コード例

完全にネイティブのアラビア語キーワードのみで記述された **再帰的阶乗計算機**:

```world
# حاسبة المضروب
متغير الرقم = عدد_صحيح(استقبل("أدخل رقماً"))

دالة مضروب(رقم)
    اذا رقم == 1 او رقم == 0 نفذ ارجاع 1
    ارجاع رقم * مضروب(رقم - 1)
نهاية

طباعة(مضروب(5))
```

レキサーがコードを読み込む様子:

| アラビア語キーワード | 意味 |
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

## 組み込みライブラリ

インタープリターは、ネイティブWorldLang関数として登録された複数のPython ベースライブラリを提供します:

| ライブラリ | 用途 | バックモジュール |
|---------|---------|----------------|
| `String` | `split`, `uppercase`, `lowercase`, `contains`, `replace`, ... | `_builtins/String.py` |
| `Random` | ランダム数生成 | `_builtins/Random.py` |
| `os` | ファイルシステム: `chdir`, `mkdir`, `list_dir`, `move`, `system`, ... | `_builtins/os.py` |
| `Image` | 画像の読み込み/保存（RGBリストへの変換/変換元） | `_builtins/Image.py` |
| `Graph` | `plot`, `scatter`, `bar` チャート描画 | `_builtins/Graph.py` |
| `Controls` | マウス/キーボード自動化 | `_builtins/Controls.py` |
| `Serial` | ハードウェア/Arduino シリアル通信 (`send`/`receive`) | `_builtins/Serial.py` |
| `Speech` | テキスト読み上げと音声認識 | `_builtins/Speech.py` |
| `GenAI` | Google Gemini経由の生成AI | `_builtins/GenAI.py` |

---

## アーキテクチャ

WorldLangは **ツリー走査インタープリター** です。ソースコードは3段階のパイプラインを通過します:

```
1. Lexer  ──→  Tokens (native keywords mapped to generic tokens)
2. Parser ──→  AST  (language-agnostic Abstract Syntax Tree)
3. Runtime ──→ Result (interpreter walks the AST, managing symbols & scope)
```

**`bin/` 内の主要コンポーネント:**

| ファイル | 役割 |
|------|------|
| `World.py` | エントリポイント — REPLシェル |
| `Lexer.py` | トークナイザー；アクティブな言語テーブルからキーワードを動的にマッピング |
| `Parser.py` | 文法ルール → AST生成 |
| `Interpreter.py` | ASTを実行し、標準ライブラリを提供 |
| `Tokens.py` | トークン型；キーワードテーブル（`keywords.json`）を読み込み |
| `Errors.py` | エラー型（`IllegalChar`、`Syntax`、`Runtime`） |
| `RT_result.py` | ランタイム結果、コンテキスト、シンボルテーブル |
| `datatypes/` | `Value`、`Number`、`String`、`List`、`Dict`、`Function` |
| `_builtins/` | Python ベースの標準ライブラリ |

キーワードテーブルは `data/` 配下のプレーンJSONファイル（言語ごとに1つ、例: `Arabic_KW.json`）で、エンジンの言語サポートを完全にデータ駆動方式で維持します。

---

## 言語・ライブラリ管理

WorldLangはランタイムにネットワークリソースを取得できます:

- **`langman`** — 追加言語のキーワードテーブルを `data/` にダウンロード。
- **`libman`** — `.world` ライブラリをダウンロード（例: `math.world`、`json_ar.world`）。
- **`extman`** — 拡張を `extensions/` にダウンロード（例: ボイスコーディング拡張 `vcode.world`）。

> これらの機能にはインターネット接続と、インタープリターが参照するリモートリポジトリへのアクセスが必要です。

---

## コントリビューション

WorldLangはオープンソースでコミュニティ主導のプロジェクトです。さまざまな形での貢献を歓迎します:

- **言語貢献者** — ローカライズテーブル（`data/*_KW.json`）の追加・改善。
- **コンパイラ開発者** — レキサー、パーサー、ランタイム、標準ライブラリの改善。
- **ハードウェア開発者** — ハードウェア・ロボティクス統合の拡充。
- **テスター** — バグの発見と信頼性の向上。
- **全員** — 問題の報告、ドキュメントの改善、アイデアの共有。

貢献するには:

1. リポジトリをフォーク。
2. フォークをクローンし、ブランチを作成。
3. 変更を加えてコミット。
4. `main` ブランチに対してプルリクエストを作成。

---

## ライセンス

WorldLangは [MITライセンス](LICENSE) の下で公開されています。
