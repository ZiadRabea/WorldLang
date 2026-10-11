import unittest
from next_syntax.lexer import lex, SyntaxErrorNext

class HybridLexerTests(unittest.TestCase):
    def kinds(self, source):
        return [t.kind for t in lex(source)]

    def test_natural_compact_equivalence(self):
        natural = 'اجعل العمر يساوي 20\nإذا كان العمر أكبر من أو يساوي 18\n    اطبع "بالغ"'
        compact = 'اجعل العمر = 20\nإذا العمر >= 18\n    اطبع "بالغ"'
        self.assertEqual(self.kinds(natural), self.kinds(compact))

    def test_strings_are_not_normalized(self):
        result = lex('اطبع "إذا كان العمر أكبر من"')
        self.assertEqual([t.kind for t in result], ['PRINT','STRING','NEWLINE','EOF'])

    def test_indent_dedent(self):
        self.assertEqual(self.kinds('إذا صحيح\n    اطبع "نعم"\nاطبع "تم"').count('DEDENT'),1)

    def test_tabs_rejected(self):
        with self.assertRaises(SyntaxErrorNext): lex('إذا صحيح\n\tاطبع "نعم"')

    def test_inconsistent_indent_rejected(self):
        with self.assertRaises(SyntaxErrorNext): lex('إذا صحيح\n    اطبع 1\n  اطبع 2')

    def test_unterminated_string_rejected(self):
        with self.assertRaises(SyntaxErrorNext): lex('اطبع "نص')

    def test_arabic_comma(self):
        self.assertIn('COMMA', self.kinds('جمع(1، 2)'))

if __name__ == '__main__': unittest.main()
