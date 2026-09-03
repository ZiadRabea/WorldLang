from Interpreter import *

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
    context.symbol_table = create_global_symbol_table(data_dict, run)
    result = interpreter.visit(ast.node, context)
    
    return result.value, result.error
