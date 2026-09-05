from Tokens import *

ops = {
    TT_PLUS : "+",
    TT_MINUS : "-",
    TT_MUL : "*",
    TT_DIV : "/",
    TT_POW : "^",
    TT_EE : "==",
    TT_GT : ">",
    TT_GTE : ">=",
    TT_LT : "<",
    TT_LTE : "<=",
    TT_EQ : "=",
    TT_NE : "!=",
    TT_RBRACE : "}",
    TT_LBRACE : "{",
    TT_LSQUARE : "[",
    TT_RSQUARE : "]",
    TT_COLON : ":",
    TT_ARROW : "->",
    TT_LPAREN : "(",
    TT_RPAREN : ")",
    TT_COMMA : ",",
    TT_SPACE : " ",
    TT_TAB : "\t"
}

class DeLexer:
    def __init__(self, fn, tokens):
        self.fn = fn
        self.tokens = tokens
        self.tok_idx = -1
        self.advance()

    def advance(self):
        self.tok_idx += 1
        self.update_current_tok()
        return self.current_tok

    def update_current_tok(self):
        if self.tok_idx >= 0 and self.tok_idx < len(self.tokens):
            self.current_tok = self.tokens[self.tok_idx]

    def detokenize(self):
        source = ""
        
        while self.current_tok != None:
            if self.current_tok.type == TT_NEWLINE:
                source += "\n"
                self.advance()

            elif self.current_tok.type in [TT_KEYWORD, TT_INT, TT_FLOAT, TT_IDENTIFIER]:
                source += f"{self.current_tok.value}"
                self.advance()

            elif self.current_tok.type == TT_STRING:
                source += f"\"{self.current_tok.value}\""
                self.advance()

            elif self.current_tok.type in ops:
                source += ops[self.current_tok.type]
                self.advance()
            
            elif self.current_tok.type == TT_EOF:
                break

        return source