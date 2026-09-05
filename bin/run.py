from Interpreter import *
from Translator import *
from DeLexer import *

def run(fn, text):
    # Generate tokens
    lexer = Lexer(fn, text)
    data_dict, tokens, error = lexer.make_tokens()
    if error: return None, error

    # Generate AST
    parser = Parser(tokens, data_dict)
    ast = parser.parse()
    if ast.error: return None, ast.error

    # Run program
    interpreter = Interpreter(data_dict)
    context = Context('<program>', data_dict)
    context.symbol_table = create_global_symbol_table(data_dict, run, translate)
    result = interpreter.visit(ast.node, context)
    
    return result.value, result.error


def translate(fn, text, language, target_lang):
    lexer = Lexer(fn, text, translating=True)
    _, tokens, _ = lexer.make_tokens()
    translator = Translate(tokens, language, target_lang)
    translated_tokens = translator.translate()

    delexer = DeLexer(fn, translated_tokens)

    return delexer.detokenize()

