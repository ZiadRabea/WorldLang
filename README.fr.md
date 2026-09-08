# WorldLang

<p align="center">

  <img src="images/world.png" alt="Logo WorldLang" width="200">

</p>

<p align="center">

  <a href="README.md">English</a> |

  <strong>Français</strong> |

  <a href="README.ar.md">العربية</a> |

  <a href="README.es.md">Español</a> |

  <a href="README.de.md">Deutsch</a> |

  <a href="README.zh.md">中文</a> |

  <a href="README.ja.md">日本語</a>

</p>

**Un langage de programmation multilingue qui vous permet d'écrire, d'exécuter, de détecter et de traduire du code dans votre langue maternelle.**

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

- 📖 **[Documentation officielle](https://ziadrabea.github.io/WorldDocs)**
  - 🚀 [Démarrage rapide](https://ziadrabea.github.io/WorldDocs/installation.html)
  - 📚 [Référence du langage](https://ziadrabea.github.io/WorldDocs/features.html)
  - 🌍 [Langues prises en charge](https://ziadrabea.github.io/WorldDocs/languages.html)
  - 🤝 [Guide de contribution](https://ziadrabea.github.io/WorldDocs/guide.html)

- 🌐 **[Site web officiel](https://ziadrabea.github.io/worldlanguage)**
- 💬 **[Rejoindre la communauté](https://flow.daisyscript.com)**
- 🔬 **[Pré-publication académique (ResearchGate)](https://www.researchgate.net/publication/377782413_A_Multilingual_Approach_with_Built-in_Code_Translation_and_Dynamic_Keyword_Importation)**
- 🧩 **[Extension VS Code WorldLangEN](https://marketplace.visualstudio.com/items?itemName=worldlangteam.WorldEn)**
- 👤 **Mainteneur :** Ziad Rabea ([LinkedIn](https://www.linkedin.com/in/ziadrabea/) | [Email](mailto:zidr2005@gmail.com))

WorldLang est un interpréteur open-source construit en Python qui supprime la barrière linguistique en programmation. Au lieu d'exiger des programmeurs qu'ils écrivent avec des mots-clés anglais, WorldLang permet d'écrire du code en utilisant une syntaxe dans la langue maternelle choisie.

L'interpréteur prend en charge un pipeline d'exécution multilingue basé sur une architecture personnalisée **Lexer → Parser → Runtime**, ainsi que la détection automatique de la langue et la traduction intégrée du code source.

> **Langues prises en charge : 31** — Arabe, Azerbaïdjanais, Chinois, Néerlandais, Anglais, Finnois, Français, Allemand, Grec, Indonésien, Irlandais, Italien, Japonais, Kazakh, Coréen, Kurde, Letton, Malais, Persan, Polonais, Portugais, Roumain, Russe, Espagnol, Suédois, Turc, Ukrainien, Ourdou, Ouzbek, Vietnamien et Hindi.

---

## Table des matières

- [Fonctionnalités](#fonctionnalités)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Détection et sélection de la langue](#détection-et-sélection-de-la-langue)
- [Traduction du code](#traduction-du-code)
- [Exemple de code](#exemple-de-code)
- [Bibliothèques intégrées](#bibliothèques-intégrées)
- [Architecture](#architecture)
- [Gestion des langues et des bibliothèques](#gestion-des-langues-et-des-bibliothèques)
- [Contribuer](#contribuer)
- [Licence](#licence)

---

## Fonctionnalités

- **Programmation en langue maternelle** — écrivez du code en utilisant les mots-clés de la langue de votre choix.
- **31 packs de langues pris en charge** avec des correspondances de mots-clés chargées dynamiquement.
- **Sélection hybride de la langue** — sélectionnez manuellement une langue ou laissez WorldLang la détecter automatiquement.
- **Détection de langue basée sur l'IA** — détecte automatiquement la syntaxe de la langue avant le lexage lorsqu'aucune langue n'est sélectionnée manuellement.
- **Exécution multilingue** — exécutez des fichiers écrits dans différentes langues prises en charge sans devoir changer manuellement la langue globale.
- **Traduction intégrée du code** — traduisez les fichiers source WorldLang entre les langues prises en charge.
- **Correspondance dynamique des mots-clés** — le lexer associe dynamiquement les mots-clés natifs à des jetons génériques.
- **Interpréteur complet** — variables, fonctions, récursivité, boucles, conditions, listes, dictionnaires et opérations arithmétiques.
- **Matériel et robotique** — communication série pour des microcontrôleurs tels qu'Arduino.
- **Parole** — synthèse vocale et reconnaissance vocale.
- **Bibliothèques intégrées** — traitement d'images, graphiques, utilitaires aléatoires, outils du système de fichiers, etc.
- **IA générative** — intégration optionnelle de Google Gemini.
- **Gestion des bibliothèques et extensions** — récupérez directement des bibliothèques et extensions `.world` depuis le réseau.

---

## Prérequis

- **Python 3.12+**
- **Windows, macOS ou Linux**

Paquets principaux :

| Paquet | Utilisation |
|---|---|
| `requests` | Téléchargement des packs de langues, bibliothèques et extensions |
| `numpy` | Détection de langue par IA et traitements numériques |
| `keras` | Détection de langue basée sur l'IA |
| `nltk` | Prétraitement pour la détection de langue |
| `Pillow` | Traitement d'images (`_builtins/Image.py`) |
| `matplotlib` | Création de graphiques (`_builtins/Graph.py`) |
| `pyautogui` | Contrôle de la souris et du clavier (`_builtins/Controls.py`) |
| `pyserial` | Communication série et matérielle (`_builtins/Serial.py`) |
| `pyttsx3` | Synthèse vocale (`_builtins/Speech.py`) |
| `SpeechRecognition` | Reconnaissance vocale (`_builtins/Speech.py`) |
| `google-generativeai` | IA générative (`_builtins/GenAI.py`) |
| `rich` | Rendu Markdown pour les sorties IA (`_builtins/GenAI.py`) |

> Seul `requests` est requis pour l'interpréteur de base. `Keras`, `NLTK` et `NumPy` sont nécessaires pour la détection automatique de langue par IA. Les autres paquets ne sont requis que pour les bibliothèques intégrées optionnelles correspondantes.

---

## Installation

```bash
# 1. Cloner le dépôt
git clone https://github.com/ZiadRabea/WorldLang.git

cd WorldLang

# 2. (Recommandé) Créer et activer un environnement virtuel
python -m venv venv

# Windows :
venv\Scripts\activate

# macOS / Linux :
source venv/bin/activate

# 3. Installer les dépendances
pip install requests numpy keras nltk Pillow matplotlib pyautogui pyserial pyttsx3 SpeechRecognition rich
```

Pour activer les fonctionnalités Google Gemini :

```bash
pip install google-generativeai
```

---

## Utilisation

L'interpréteur est livré sous forme de REPL (*Read–Eval–Print Loop*). Pour le lancer :

```bash
python bin/World.py
```

Un prompt apparaît :

```text
World >>
```

Tapez un programme et appuyez sur Entrée pour l'exécuter.

### Commandes spéciales

| Commande | Action |
|---|---|
| `world()` | Exécuter des fichiers source WorldLang |
| `libman` | Lancer le gestionnaire de bibliothèques et télécharger des bibliothèques `.world` |
| `langman` | Lancer le gestionnaire de langues et télécharger des packs de langues |
| `extman` | Lancer le gestionnaire d'extensions et télécharger des extensions |
| `setlang` | Sélectionner manuellement une langue de programmation ou activer la détection automatique |
| `translate()` | Traduire le code source WorldLang entre les langues prises en charge |

---

## Détection et sélection de la langue

WorldLang prend en charge un **système hybride de sélection de la langue**.

Vous pouvez sélectionner explicitement la langue que vous souhaitez utiliser, ou laisser la langue non définie afin que l'interpréteur détecte automatiquement la langue du code source.

### Sélection manuelle de la langue

Utilisez :

```text
setlang
```

Exemple :

```text
setlang -> ArabicKW
```

Cela configure manuellement WorldLang pour utiliser la table de mots-clés arabes.

### Détection automatique de la langue

Laissez l'entrée de langue vide :

```text
setlang -> ""
```

Cela active la détection automatique de la langue.

Lorsque la détection automatique est activée, WorldLang analyse le code source et détermine la langue appropriée pendant la phase de lexage/tokenisation.

Cela permet à du code et à des modules importés écrits dans différentes langues prises en charge de s'exécuter **sans devoir changer manuellement la langue active au préalable**.

### Modules de détection par IA

Le système automatique de détection de langue utilise :

- `Keras`
- `NLTK`
- `NumPy`

La détection automatique est optionnelle lorsque vous sélectionnez manuellement une langue avec `setlang`.

---

## Traduction du code

WorldLang inclut un **traducteur de code multilingue intégré**.

Au lieu de traduire le code par simple remplacement de texte, le traducteur traite la source à travers un pipeline multilingue structuré :

```text
Source

   ↓

Lexer

   ↓

Translator

   ↓

DeLexer

   ↓

Source traduite
```

Le code source est d'abord lexé en représentations indépendantes de la langue. Le traducteur associe ensuite ces représentations à la langue cible, puis le **DeLexer** reconstruit un code source WorldLang valide.

### Commande de traduction

```text
translate(filename.world, source_language, target_language)
```

Exemple :

```text
translate("factorial.world", "English", "Chinese")
```

WorldLang génère automatiquement un nouveau fichier source utilisant la langue cible.

Par exemple :

```text
factorial_Chinese.world
```

Cela permet d'écrire un programme WorldLang dans une langue et de convertir le même code source vers une autre langue prise en charge.

---

## Exemple de code

Une **calculatrice de factorielle** peut être écrite en arabe :

```worldlang
# حاسبة المضروب

متغير الرقم = عدد_صحيح(استقبل("أدخل رقماً"))

دالة مضروب(رقم)

    اذا رقم == 1 او رقم == 0 نفذ ارجاع 1

    ارجاع رقم * مضروب(رقم - 1)

نهاية

طباعة(مضروب(الرقم))
```

Le même programme peut également être écrit en anglais :

```worldlang
# Factorial Calculator

var number = int(input("Enter a number:"))

func factorial(number)

    if number == 1 or number == 0 do return 1

    return number * factorial(number - 1)

end

print(factorial(number))
```

Lorsque la détection automatique est activée, WorldLang peut déterminer la langue prise en charge utilisée par le code source sans nécessiter de changement manuel de langue.

---

## Bibliothèques intégrées

L'interpréteur expose plusieurs bibliothèques basées sur Python, enregistrées en tant que fonctions natives de WorldLang :

| Bibliothèque | Objectif | Module sous-jacent |
|---|---|---|
| `String` | `split`, `uppercase`, `lowercase`, `contains`, `replace`, ... | `_builtins/String.py` |
| `Random` | Génération de nombres aléatoires | `_builtins/Random.py` |
| `os` | Opérations sur le système de fichiers : `chdir`, `mkdir`, `list_dir`, `move`, `system`, ... | `_builtins/os.py` |
| `Image` | Charger/enregistrer des images et convertir vers/depuis des listes RGB | `_builtins/Image.py` |
| `Graph` | `plot`, `scatter`, `bar` pour la création de graphiques | `_builtins/Graph.py` |
| `Controls` | Automatisation de la souris et du clavier | `_builtins/Controls.py` |
| `Serial` | Communication série avec du matériel/Arduino (`send`/`receive`) | `_builtins/Serial.py` |
| `Speech` | Synthèse vocale et reconnaissance vocale | `_builtins/Speech.py` |
| `GenAI` | IA générative via Google Gemini | `_builtins/GenAI.py` |

---

## Architecture

WorldLang est un **interpréteur à parcours d'arbre (*tree-walking interpreter*)** avec une architecture de traitement multilingue étendue.

### Pipeline d'exécution du code

```text
Code source

    ↓

Sélection de la langue / Détection par IA

    ↓

Lexer

    ↓

Tokens

    ↓

Parser

    ↓

Arbre syntaxique abstrait (AST)

    ↓

Runtime

    ↓

Résultat
```

La couche de détection linguistique permet à WorldLang de déterminer dynamiquement quelle table de mots-clés doit être utilisée avant la tokenisation lorsqu'aucune langue n'a été sélectionnée manuellement.

### Pipeline de traduction du code

```text
Source

   ↓

Lexer

   ↓

Représentation indépendante de la langue

   ↓

Translator

   ↓

DeLexer

   ↓

Source traduite
```

Cette architecture permet à WorldLang d'exécuter et de traduire du code source multilingue tout en gardant le pipeline interne de l'interpréteur indépendant de la langue.

### Composants principaux

| Fichier / composant | Rôle |
|---|---|
| `World.py` | Point d'entrée et shell REPL |
| `Lexer.py` | Tokenizer ; associe dynamiquement les mots-clés depuis la table de langue détectée ou sélectionnée |
| `Parser.py` | Règles grammaticales et génération de l'AST |
| `Interpreter.py` | Exécute l'AST et fournit la bibliothèque standard |
| `Tokens.py` | Types de tokens et gestion des mots-clés |
| `Translator.py` | Convertit les représentations tokenisées du code entre les langues prises en charge |
| `DeLexer.py` | Reconstruit le code source avec les correspondances de mots-clés de la langue cible |
| `Errors.py` | Types d'erreurs (`IllegalChar`, `Syntax`, `Runtime`) |
| `RT_result.py` | Résultats d'exécution, contextes et tables de symboles |
| `datatypes/` | `Value`, `Number`, `String`, `List`, `Dict`, `Function` |
| `_builtins/` | Bibliothèques standard basées sur Python |
| `data/` | Tables de mots-clés et ressources linguistiques multilingues |

Les tables de mots-clés sont des fichiers JSON pilotés par les données, ce qui permet d'ajouter des langues supplémentaires sans réécrire la grammaire principale de l'interpréteur.

---

## Gestion des langues et des bibliothèques

WorldLang peut récupérer des ressources depuis le réseau à l'exécution :

- **`langman`** — télécharger des tables de mots-clés pour des langues supplémentaires dans `data/`.
- **`libman`** — télécharger des bibliothèques `.world`.
- **`extman`** — télécharger des extensions dans `extensions/`.
- **`setlang`** — configurer manuellement une langue ou activer la détection automatique basée sur l'IA.
- **`translate()`** — convertir des fichiers source WorldLang entre les langues prises en charge.

> La détection de langue et la traduction reposent sur l'architecture multilingue des mots-clés, ce qui permet à différents packs linguistiques de partager le même interpréteur sous-jacent.

---

## Contribuer

WorldLang est open-source et communautaire. Les contributions sont les bienvenues sous plusieurs formes :

- **Contributeurs linguistiques** — ajouter ou améliorer la localisation et les tables de mots-clés.
- **Développeurs du compilateur/interpréteur** — améliorer le lexer, le parser, le traducteur, le DeLexer, le runtime et la bibliothèque standard.
- **Développeurs IA** — améliorer les modèles de détection automatique de langue et le prétraitement.
- **Développeurs matériel** — étendre les intégrations matérielles et robotiques.
- **Testeurs** — découvrir des bugs et améliorer la fiabilité.
- **Tout le monde** — signaler des problèmes, améliorer la documentation et partager des idées.

Pour contribuer :

1. Forkez le dépôt.
2. Clonez votre fork et créez une branche.
3. Effectuez vos modifications et créez un commit.
4. Ouvrez une Pull Request vers la branche `main`.

---

## Licence

WorldLang est distribué sous la [Licence MIT](LICENSE).
