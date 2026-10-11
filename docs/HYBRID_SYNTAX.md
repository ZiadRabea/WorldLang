# WorldLang Next: experimental Arabic hybrid lexer

Tracking RFC: https://github.com/ZiadRabea/WorldLang/issues/13

This opt-in prototype does **not** modify the existing WorldLang interpreter, parser, translator, or keyword packs. It tokenizes Arabic natural phrases and compact equivalents into canonical token kinds, and emits indentation tokens.

Examples:

```text
اجعل العمر يساوي 20
إذا كان العمر أكبر من أو يساوي 18
    اطبع "بالغ"
```

```text
اجعل العمر = 20
إذا العمر >= 18
    اطبع "بالغ"
```

Run tests from the repository root:

```sh
python -m unittest discover -s tests -v
```

**Status:** lexer prototype only; no Next parser, AST integration, execution support, or proven backward-compatibility suite yet. Existing Classic files are untouched. Future changes require maintainer review.
