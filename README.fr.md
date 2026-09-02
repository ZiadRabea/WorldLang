# WorldLang

<p align="center">
  <img src="images/world.png" alt="Logo WorldLang" width="200">
</p>

<p align="center">
  <a href="README.md">English</a> |
  <a href="README.ar.md">العربية</a> |
  <strong>Français</strong> |
  <a href="README.es.md">Español</a> |
  <a href="README.de.md">Deutsch</a> |
  <a href="README.zh.md">中文</a> |
  <a href="README.ja.md">日本語</a>
</p>

**Un langage de programmation multilingue qui vous permet d'écrire et d'exécuter du code dans votre langue maternelle.**

<p align="center">
  <a href="https://github.com/ZiadRabea/WorldLang/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/ZiadRabea/WorldLang" alt="Licence GitHub">
  </a>
  <br>
  <a href="https://marketplace.visualstudio.com/items?itemName=worldlangteam.WorldEn">
    <img src="https://vsmarketplacebadges.dev/version-short/worldlangteam.WorldEn.svg" alt="Extension VSCode">
  </a>
  <br>
  <a href="https://www.researchgate.net/publication/377782413_A_Multilingual_Approach_with_Built-in_Code_Translation_and_Dynamic_Keyword_Importation">
    <img src="https://img.shields.io/badge/ResearchGate-preprint-brightgreen" alt="ResearchGate">
  </a>
</p>

**Ressources et liens :**

* 📖 **[Documentation officielle](https://ziadrabea.github.io/WorldDocs)**
  * 🚀 [Démarrage rapide](https://ziadrabea.github.io/WorldDocs/installation.html)
  * 📚 [Référence du langage](https://ziadrabea.github.io/WorldDocs/features.html)
  * 🌍 [Langues prises en charge](https://ziadrabea.github.io/WorldDocs/languages.html)
  * 🤝 [Guide de contribution](https://ziadrabea.github.io/WorldDocs/guide.html)
* 🌐 **[Site web officiel](https://ziadrabea.github.io/worldlanguage)**
* 💬 **[Rejoindre la communauté](https://flow.daisyscript.com)**
* 🔬 **[Pré-publication académique (ResearchGate)](https://www.researchgate.net/publication/377782413_A_Multilingual_Approach_with_Built-in_Code_Translation_and_Dynamic_Keyword_Importation)**
* 🧩 **[Extension VS Code WorldLangEN](https://marketplace.visualstudio.com/items?itemName=worldlangteam.WorldEn)**
* 👤 **Mainteneur :** Ziad Rabea ([LinkedIn](https://www.linkedin.com/in/ziadrabea/) | [Email](mailto:zidr2005@gmail.com))

WorldLang est un interpréteur open-source construit en Python qui supprime la barrière linguistique en programmation. Au lieu de mémoriser des mots-clés en anglais, vous écrivez du code en utilisant une syntaxe native — arabe, français, japonais et 18 autres langues — et le moteur le tokenize et l'exécute via un pipeline Lexer → Parser → Runtime personnalisé.

> **Langues supportées : 21** — Arabe, Chinois, Néerlandais, Anglais, Français, Allemand, Indonésien, Italien, Japonais, Kazakh, Coréen, Persan, Polonais, Portugais, Roumain, Russe, Espagnol, Turc, Ukrainien, Ourdou, Vietnamien.

---

## Table des matières

- [Fonctionnalités](#fonctionnalités)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Exemple de code](#exemple-de-code)
- [Bibliothèques intégrées](#bibliothèques-intégrées)
- [Architecture](#architecture)
- [Gestion des langues et des bibliothèques](#gestion-des-langues-et-des-bibliothèques)
- [Contribuer](#contribuer)
- [Licence](#licence)

---

## Fonctionnalités

- **Programmation en langue maternelle** — écrivez du code en utilisant les mots-clés de la langue de votre choix.
- **21 packs de langues** fournis dans `data/` sous forme de tableaux de mots-clés JSON.
- **Correspondance dynamique des mots-clés** — le lexer associe les mots-clés natifs aux jetons génériques à la volée.
- **Interpréteur complet** — variables, fonctions, récursion, boucles, conditions, listes, dictionnaires et arithmétique.
- **Matériel et robotique** — communication série pour microcontrôleurs (par ex. Arduino).
- **Parole** — synthèse vocale et reconnaissance vocale.
- **Bibliothèques intégrées** — traitement d'images, traitements graphiques, aléatoire, système de fichiers, et plus encore.
- **IA générative** — intégration optionnelle avec Google Gemini.
- **Gestion des bibliothèques et extensions** — récupérez des bibliothèques et extensions `.world` directement depuis le réseau.

---

## Prérequis

- **Python 3.12+**
- **Windows, macOS ou Linux**

Paquets principaux nécessaires (voir [Installation](#installation)) :

| Paquet | Utilisation |
|---------|----------|
| `requests` | Téléchargement des packs de langues, bibliothèques et extensions |
| `Pillow` | Traitement d'images (`_builtins/Image.py`) |
| `matplotlib` & `numpy` | Traitements graphiques (`_builtins/Graph.py`) |
| `pyautogui` | Contrôle souris/clavier (`_builtins/Controls.py`) |
| `pyserial` | Communication série/matériel (`_builtins/Serial.py`) |
| `pyttsx3` | Synthèse vocale (`_builtins/Speech.py`) |
| `SpeechRecognition` | Reconnaissance vocale (`_builtins/Speech.py`) |
| `google-generativeai` | IA générative (`_builtins/GenAI.py`) |
| `rich` | Rendu Markdown pour les sorties IA (`_builtins/GenAI.py`) |

> Seul `requests` est requis pour les fonctionnalités de base. Les paquets restants ne sont nécessaires que pour les bibliothèques intégrées optionnelles spécifiques listées ci-dessus.

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

Pour activer les fonctionnalités IA, vous avez également besoin de :

```bash
pip install google-generativeai
```

---

## Utilisation

L'interpréteur est livré sous forme de REPL (Boucle d'évaluation interactive). Pour le lancer :

```bash
python bin/World.py
```

Un prompt apparaît :

```
World >>
```

Tapez un programme et appuyez sur Entrée pour l'exécuter. Commandes spéciales au prompt :

| Commande   | Action                                                        |
|------------|---------------------------------------------------------------|
| `libman`   | Lancer le gestionnaire de bibliothèques (télécharger des bibliothèques `.world`) |
| `langman`  | Lancer le gestionnaire de langues (télécharger/changer de packs de langues) |
| `extman`   | Lancer le gestionnaire d'extensions (télécharger des extensions) |

`WorldLang` utilise l'arabe par défaut. Les mots-clés arabes sont chargés depuis `bin/keywords.json`. Changez ou ajoutez des langues via le gestionnaire `langman`.

---

## Exemple de code

Une **calculatrice de factorielle** récursive entièrement écrite avec des mots-clés arabes natifs :

```world
# حاسبة المضروب
متغير الرقم = عدد_صحيح(استقبل("أدخل رقماً"))

دالة مضروب(رقم)
    اذا رقم == 1 او رقم == 0 نفذ ارجاع 1
    ارجاع رقم * مضروب(رقم - 1)
نهاية

طباعة(مضروب(5))
```

Comment le lexer le lit :

| Mot-clé arabe | Signification |
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

## Bibliothèques intégrées

L'interpréteur expose plusieurs bibliothèques basées sur Python, enregistrées en tant que fonctions natives de WorldLang :

| Bibliothèque | Objectif | Module sous-jacent |
|---------|---------|----------------|
| `String` | `split`, `uppercase`, `lowercase`, `contains`, `replace`, ... | `_builtins/String.py` |
| `Random` | Génération de nombres aléatoires | `_builtins/Random.py` |
| `os` | Système de fichiers : `chdir`, `mkdir`, `list_dir`, `move`, `system`, ... | `_builtins/os.py` |
| `Image` | Chargement/sauvegarde d'images (conversion vers/depuis des listes RGB) | `_builtins/Image.py` |
| `Graph` | `plot`, `scatter`, `bar` — traitements graphiques | `_builtins/Graph.py` |
| `Controls` | Automatisation souris/clavier | `_builtins/Controls.py` |
| `Serial` | Communication série matériel/Arduino (`send`/`receive`) | `_builtins/Serial.py` |
| `Speech` | Synthèse vocale et reconnaissance vocale | `_builtins/Speech.py` |
| `GenAI` | IA générative via Google Gemini | `_builtins/GenAI.py` |

---

## Architecture

WorldLang est un **interpréteur à parcours d'arbre**. Le code source passe par un pipeline en trois étapes :

```
1. Lexer  ──→  Tokens (mots-clés natifs mappés à des jetons génériques)
2. Parser ──→  AST  (arbre syntaxique abstrait indépendant de la langue)
3. Runtime ──→ Résultat (l'interpréteur parcourt l'AST, gérant les symboles et la portée)
```

**Composants principaux dans `bin/` :**

| Fichier | Rôle |
|------|------|
| `World.py` | Point d'entrée — shell REPL |
| `Lexer.py` | Tokenizer ; associe dynamiquement les mots-clés depuis la table de langue active |
| `Parser.py` | Règles grammaticales → génération d'AST |
| `Interpreter.py` | Exécute l'AST et fournit la bibliothèque standard |
| `Tokens.py` | Types de jetons ; charge les tableaux de mots-clés (`keywords.json`) |
| `Errors.py` | Types d'erreurs (`IllegalChar`, `Syntax`, `Runtime`) |
| `RT_result.py` | Résultats d'exécution, contexte et tables de symboles |
| `datatypes/` | `Value`, `Number`, `String`, `List`, `Dict`, `Function` |
| `_builtins/` | Bibliothèques standard basées sur Python |

Les tableaux de mots-clés sont des fichiers JSON bruts sous `data/` (un par langue, par ex. `Arabic_KW.json`), ce qui rend le support linguistique du moteur entièrement basé sur les données.

---

## Gestion des langues et des bibliothèques

WorldLang peut récupérer des ressources depuis le réseau à l'exécution :

- **`langman`** — télécharger des tableaux de mots-clés pour des langues supplémentaires dans `data/`.
- **`libman`** — télécharger des bibliothèques `.world` (par ex. `math.world`, `json_ar.world`).
- **`extman`** — télécharger des extensions dans `extensions/` (par ex. l'extension de codage vocal `vcode.world`).

> Ces fonctionnalités nécessitent une connexion Internet et l'accès au dépôt de ressources distant référencé par l'interpréteur.

---

## Contribuer

WorldLang est open-source et communautaire. Les contributions sont bienvenues sous plusieurs formes :

- **Contributeurs linguistiques** — ajoutez ou améliorez les tableaux de localisation (`data/*_KW.json`).
- **Développeurs compilateurs** — améliorez le lexer, le parser, le runtime et la bibliothèque standard.
- **Développeurs matériel** — étendez les intégrations matériel et robotique.
- **Testeurs** — découvrez des bugs et améliorez la fiabilité.
- **Tout le monde** — signalez des problèmes, améliorez la documentation et partagez des idées.

Pour contribuer :

1. Forkez le dépôt.
2. Clonez votre fork et créez une branche.
3. Effectuez vos modifications et commitez-les.
4. Ouvrez une Pull Request vers la branche `main`.

---

## Licence

WorldLang est distribué sous la [Licence MIT](LICENSE).
