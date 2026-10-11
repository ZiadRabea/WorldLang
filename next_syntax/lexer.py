"""Experimental opt-in WorldLang Next lexer; does not alter the Classic lexer."""
from dataclasses import dataclass
import re

@dataclass(frozen=True)
class Token:
    kind: str
    value: str
    line: int
    column: int

class SyntaxErrorNext(ValueError):
    pass

PHRASES = {
    'أكبر من أو يساوي': 'GE', 'اكبر من او يساوي': 'GE',
    'أصغر من أو يساوي': 'LE', 'اصغر من او يساوي': 'LE',
    'أكبر من': 'GT', 'اكبر من': 'GT',
    'أصغر من': 'LT', 'اصغر من': 'LT',
    'إذا كان': 'IF', 'إذا كانت': 'IF', 'اذا كان': 'IF', 'اذا كانت': 'IF',
    'وإلا إذا': 'ELIF', 'والا اذا': 'ELIF',
    'وإلا': 'ELSE', 'والا': 'ELSE',
    'اجعل': 'LET', 'إذا': 'IF', 'اذا': 'IF', 'اطبع': 'PRINT',
    'يساوي': 'ASSIGN', 'أو': 'OR', 'او': 'OR', 'و': 'AND',
}
PHRASE_ORDER = sorted(PHRASES, key=len, reverse=True)
IDENT = re.compile(r'[^\W\d]\w*', re.UNICODE)
NUMBER = re.compile(r'\d+(?:\.\d+)?')
SYMBOLS = {'=':'ASSIGN', '>':'GT', '<':'LT', '+':'PLUS', '-':'MINUS',
           '*':'MUL', '/':'DIV', '(':'LPAREN', ')':'RPAREN', ':':'COLON',
           ',':'COMMA', '،':'COMMA'}

def lex(source: str) -> list[Token]:
    tokens: list[Token] = []
    indents = [0]
    for line_no, line in enumerate(source.splitlines(), 1):
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        prefix = line[:len(line)-len(line.lstrip(' \t'))]
        if '\t' in prefix:
            raise SyntaxErrorNext(f'Line {line_no}: tabs are not allowed in indentation')
        depth = len(prefix)
        if depth > indents[-1]:
            indents.append(depth)
            tokens.append(Token('INDENT', '', line_no, 1))
        elif depth < indents[-1]:
            while len(indents)>1 and depth < indents[-1]:
                indents.pop()
                tokens.append(Token('DEDENT', '', line_no, 1))
            if depth != indents[-1]:
                raise SyntaxErrorNext(f'Line {line_no}: inconsistent indentation')
        i = depth
        while i < len(line):
            c = line[i]
            if c.isspace():
                i += 1; continue
            if c == '#':
                break
            if c in '"\'':
                quote = c; start = i; i += 1; escaped = False
                while i < len(line):
                    if not escaped and line[i] == quote:
                        i += 1; break
                    if not escaped and line[i] == '\\': escaped = True
                    else: escaped = False
                    i += 1
                else:
                    raise SyntaxErrorNext(f'Line {line_no}: unterminated string')
                tokens.append(Token('STRING', line[start:i], line_no, start+1)); continue
            phrase = next((p for p in PHRASE_ORDER if line.startswith(p, i)
                and (i == 0 or not (line[i-1].isalnum() or line[i-1]=='_'))
                and (i+len(p)==len(line) or not (line[i+len(p)].isalnum() or line[i+len(p)]=='_'))), None)
            if phrase:
                tokens.append(Token(PHRASES[phrase], phrase, line_no, i+1))
                i += len(phrase); continue
            if line.startswith(('>=','<=','==','!='), i):
                op=line[i:i+2]
                tokens.append(Token({'>=':'GE','<=':'LE','==':'EQ','!=':'NE'}[op],op,line_no,i+1))
                i+=2;continue
            match = NUMBER.match(line,i)
            if match:
                tokens.append(Token('NUMBER',match.group(),line_no,i+1));i=match.end();continue
            match = IDENT.match(line,i)
            if match:
                tokens.append(Token('IDENT',match.group(),line_no,i+1));i=match.end();continue
            if c in SYMBOLS:
                tokens.append(Token(SYMBOLS[c],c,line_no,i+1));i+=1;continue
            raise SyntaxErrorNext(f'Line {line_no}, column {i+1}: unexpected character {c!r}')
        tokens.append(Token('NEWLINE','',line_no,len(line)+1))
    for _ in indents[1:]:
        tokens.append(Token('DEDENT','',len(source.splitlines())+1,1))
    tokens.append(Token('EOF','',len(source.splitlines())+1,1))
    return tokens
