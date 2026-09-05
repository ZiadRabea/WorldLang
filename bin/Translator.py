##############################
# Imports
##############################
from Tokens import *

import json
import sys
import os


if getattr(sys, 'frozen', False):
    app_path = os.path.dirname(sys.executable)
else:
    app_path = os.path.dirname(os.path.abspath(__file__))


class Translate:
    def __init__(self, tokens, src_lang, target_lang):
        self.tokens = tokens
        self.tok_idx = -1
        self.src_lang = src_lang
        self.target_lang = target_lang
        self.generate_flipped_dict()
        self.advance()
        
    def advance(self):
        self.tok_idx += 1
        self.update_current_tok()
        return self.current_tok

    def update_current_tok(self):
        if self.tok_idx >= 0 and self.tok_idx < len(self.tokens):
            self.current_tok = self.tokens[self.tok_idx]

    def generate_flipped_dict(self):
        with open(f"{app_path}/data/{self.src_lang}_KW.json", "r", encoding="utf-8") as f:
            self.flipped_dict = {value: key for key, value in json.load(f)["keywords"][0].items()}
            
        with open(f"{app_path}/data/{self.target_lang}_KW.json", "r", encoding="utf-8") as f:
            self.target_dict = json.load(f)["keywords"][0]
     
    def translate(self):
        tokens = []

        while self.current_tok != None:
            if self.current_tok.type == TT_KEYWORD:
                self.current_tok.value = self.target_dict[self.flipped_dict[self.current_tok.value]]
                tokens.append(self.current_tok)
                self.advance()
            elif self.current_tok.type == TT_IDENTIFIER:
                tokens.append(self.process_identifiers())
            elif self.current_tok.type == TT_EOF:
                tokens.append(self.current_tok)
                break
            else:
                tokens.append(self.current_tok)
                self.advance()

        return tokens

    def process_identifiers(self):
        tok_type = TT_IDENTIFIER
        tok_value = self.current_tok.value

        self.advance()

        if self.current_tok.type == TT_LPAREN:
            try:
                tok_value = self.target_dict[self.flipped_dict[self.current_tok.value]]
            except:
                pass

        return Token(tok_type, tok_value)
            
    
        
       