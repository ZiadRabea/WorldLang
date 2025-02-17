import sys
from RT_result import *
from Tokens import *
from Lexer import *
from Parser import *
from Errors import *
from datatypes import String, List, Number, Dict
from datatypes.Function import *
import importlib
#from rich.console import Console
#from rich.markdown import Markdown

#genai.configure(api_key="AIzaSyAziOtWmL9G6UiYYzxo1ewULBfCoqevh0w")
#model = genai.GenerativeModel('gemini-1.5-flash')

# INTERPRETER

class Interpreter:
    def visit(self, node, context):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name, self.no_visit_method)
        return method(node, context)

    def no_visit_method(self, node, context):
        raise Exception(f'No visit_{type(node).__name__} method defined')

    ###################################

    def visit_NumberNode(self, node, context):
        return RTResult().success(
            Number(node.tok.value).set_context(context).set_pos(node.pos_start, node.pos_end)
        )

    def visit_StringNode(self, node, context):
        return RTResult().success(
            String(node.tok.value).set_context(context).set_pos(node.pos_start, node.pos_end)
        )

    def visit_ListNode(self, node, context):
        res = RTResult()
        elements = []

        for element_node in node.element_nodes:
            elements.append(res.register(self.visit(element_node, context)))
            if res.should_return(): return res

        return res.success(
            List(elements).set_context(context).set_pos(node.pos_start, node.pos_end)
        )

    def visit_VarAccessNode(self, node, context):
        res = RTResult()
        var_name = node.var_name_tok.value
        value = context.symbol_table.get(var_name)

        if not value:
            return res.failure(RTError(
                node.pos_start, node.pos_end,
                f"'{var_name}' is not defined",
                context
            ))

        value = value.copy().set_pos(node.pos_start, node.pos_end).set_context(context)
        return res.success(value)

    def visit_VarAssignNode(self, node, context):
        res = RTResult()
        var_name = node.var_name_tok.value
        value = res.register(self.visit(node.value_node, context))
        if res.should_return(): return res

        context.symbol_table.set(var_name, value)
        return res.success(value)

    def visit_BinOpNode(self, node, context):
        global error, result
        res = RTResult()
        left = res.register(self.visit(node.left_node, context))
        if res.should_return(): return res
        right = res.register(self.visit(node.right_node, context))
        if res.should_return(): return res

        if node.op_tok.type == TT_PLUS:
            result, error = left.added_to(right)
        elif node.op_tok.type == TT_MINUS:
            result, error = left.subbed_by(right)
        elif node.op_tok.type == TT_MUL:
            result, error = left.multed_by(right)
        elif node.op_tok.type == TT_DIV:
            result, error = left.dived_by(right)
        elif node.op_tok.type == TT_POW:
            result, error = left.powed_by(right)
        elif node.op_tok.type == TT_EE:
            result, error = left.get_comparison_eq(right)
        elif node.op_tok.type == TT_NE:
            result, error = left.get_comparison_ne(right)
        elif node.op_tok.type == TT_LT:
            result, error = left.get_comparison_lt(right)
        elif node.op_tok.type == TT_GT:
            result, error = left.get_comparison_gt(right)
        elif node.op_tok.type == TT_LTE:
            result, error = left.get_comparison_lte(right)
        elif node.op_tok.type == TT_GTE:
            result, error = left.get_comparison_gte(right)
        elif node.op_tok.matches(TT_KEYWORD, data_dict['and']):
            result, error = left.anded_by(right)
        elif node.op_tok.matches(TT_KEYWORD, data_dict['or']):
            result, error = left.ored_by(right)

        if error:
            return res.failure(error)
        else:
            return res.success(result.set_pos(node.pos_start, node.pos_end))

    def visit_UnaryOpNode(self, node, context):
        res = RTResult()
        number = res.register(self.visit(node.node, context))
        if res.should_return(): return res

        error = None

        if node.op_tok.type == TT_MINUS:
            number, error = number.multed_by(Number(-1))
        elif node.op_tok.matches(TT_KEYWORD, data_dict['not']):
            number, error = number.notted()

        if error:
            return res.failure(error)
        else:
            return res.success(number.set_pos(node.pos_start, node.pos_end))

    def visit_IfNode(self, node, context):
        res = RTResult()

        for condition, expr, should_return_null in node.cases:
            condition_value = res.register(self.visit(condition, context))
            if res.should_return(): return res

            if condition_value.is_true():
                expr_value = res.register(self.visit(expr, context))
                if res.should_return(): return res
                return res.success(Number.null if should_return_null else expr_value)

        if node.else_case:
            expr, should_return_null = node.else_case
            expr_value = res.register(self.visit(expr, context))
            if res.should_return():
                return res
            return res.success(Number.null if should_return_null else expr_value)

        return res.success(Number.null)

    def visit_DictNode(self, node, context):
        res = RTResult()
        elements = {}

        for key_node, value_node in node.key_value_pairs:
            key = res.register(self.visit(key_node, context))
            if res.should_return(): return res

            value = res.register(self.visit(value_node, context))
            if res.should_return(): return res

            elements[key.value] = value

        return res.success(Dict(elements))
    def visit_ForNode(self, node, context):
        res = RTResult()
        elements = []

        start_value = res.register(self.visit(node.start_value_node, context))
        if res.should_return(): return res

        end_value = res.register(self.visit(node.end_value_node, context))
        if res.should_return(): return res

        if node.step_value_node:
            step_value = res.register(self.visit(node.step_value_node, context))
            if res.should_return(): return res
        else:
            step_value = Number(1)

        i = start_value.value

        if step_value.value >= 0:
            condition = lambda: i < end_value.value
        else:
            condition = lambda: i > end_value.value

        while condition():
            context.symbol_table.set(node.var_name_tok.value, Number(i))
            i += step_value.value

            value = res.register(self.visit(node.body_node, context))
            if res.should_return() and res.loop_should_continue == False and res.loop_should_break == False: return res

            if res.loop_should_continue:
                continue

            if res.loop_should_break:
                break

            elements.append(value)

        return res.success(
            Number.null if node.should_return_null else
            List(elements).set_context(context).set_pos(node.pos_start, node.pos_end)
        )

    def visit_WhileNode(self, node, context):
        res = RTResult()
        elements = []

        while True:
            condition = res.register(self.visit(node.condition_node, context))
            if res.should_return(): return res

            if not condition.is_true():
                break

            value = res.register(self.visit(node.body_node, context))
            if res.should_return() and res.loop_should_continue == False and res.loop_should_break == False: return res

            if res.loop_should_continue:
                continue

            if res.loop_should_break:
                break

            elements.append(value)

        return res.success(
            Number.null if node.should_return_null else
            List(elements).set_context(context).set_pos(node.pos_start, node.pos_end)
        )

    def visit_FuncDefNode(self, node, context):
        res = RTResult()

        func_name = node.var_name_tok.value if node.var_name_tok else None
        body_node = node.body_node
        arg_names = [arg_name.value for arg_name in node.arg_name_toks]
        func_value = Function(func_name, body_node, arg_names, node.should_auto_return).set_context(context).set_pos(
            node.pos_start, node.pos_end)

        if node.var_name_tok:
            context.symbol_table.set(func_name, func_value)

        return res.success(func_value)

    def visit_CallNode(self, node, context):
        res = RTResult()
        args = []

        value_to_call = res.register(self.visit(node.node_to_call, context))
        if res.should_return(): return res
        value_to_call = value_to_call.copy().set_pos(node.pos_start, node.pos_end)

        for arg_node in node.arg_nodes:
            args.append(res.register(self.visit(arg_node, context)))
            if res.should_return(): return res

        return_value = res.register(value_to_call.execute(args))
        if res.should_return(): return res
        return_value = return_value.copy().set_pos(node.pos_start, node.pos_end).set_context(context)
        return res.success(return_value)

    def visit_ReturnNode(self, node, context):
        res = RTResult()

        if node.node_to_return:
            value = res.register(self.visit(node.node_to_return, context))
            if res.should_return(): return res
        else:
            value = Number.null

        return res.success_return(value)

    def visit_ContinueNode(self, node, context):
        return RTResult().success_continue()

    def visit_BreakNode(self, node, context):
        return RTResult().success_break()
    
class Function(BaseFunction):
    def __init__(self, name, body_node, arg_names, should_auto_return):
        super().__init__(name)
        self.body_node = body_node
        self.arg_names = arg_names
        self.should_auto_return = should_auto_return

    def execute(self, args):
        res = RTResult()
        interpreter = Interpreter()
        exec_ctx = self.generate_new_context()

        res.register(self.check_and_populate_args(False, False, self.arg_names, args, exec_ctx))
        if res.should_return(): return res

        value = res.register(interpreter.visit(self.body_node, exec_ctx))
        if res.should_return() and res.func_return_value == None: return res

        ret_value = (value if self.should_auto_return else None) or res.func_return_value or Number.null
        return res.success(ret_value)

    def copy(self):
        copy = Function(self.name, self.body_node, self.arg_names, self.should_auto_return)
        copy.set_context(self.context)
        copy.set_pos(self.pos_start, self.pos_end)
        return copy

    def __repr__(self):
        return f"<function {self.name}>"  
      
class deco:
    def __init__(self, cls):
        self.cls = cls

    def __call__(self, f):
        setattr(self.cls, f.__name__, f)
        return self.cls

@deco(BuiltInFunction)
def execute_run(self, exec_ctx):
    fn = exec_ctx.symbol_table.get("fn")

    if not isinstance(fn, String):
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "Second argument must be string",
            exec_ctx
        ))

    fn = fn.value

    try:
        with open(fn, "r", encoding="UTF-8") as f:
            script = f.read()
    except Exception as e:
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            f"Failed to load script \"{fn}\"\n" + str(e),
            exec_ctx
        ))

    _, error = run(fn, script)

    if error:
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            f"Failed to finish executing script \"{fn}\"\n" +
            error.as_string(),
            exec_ctx
        ))

    return RTResult().success(String.none)

BuiltInFunction.execute_run.arg_names = ["fn"]
BuiltInFunction.execute_run.infinite = False
BuiltInFunction.execute_run.accept_none = False

@deco(BuiltInFunction)
def execute_import(self, exec_ctx):
    fn = exec_ctx.symbol_table.get("fn")
    baseurl = "https://raw.githubusercontent.com/ZiadRabea/World-Programming/main/libs/"
    if not isinstance(fn, String):
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "Second argument must be string",
            exec_ctx
        ))

    fn = fn.value
    if ".world" in fn:
        try:
            with open(f"{app_path}/libs/{fn}", "r", encoding="UTF-8") as f:
                script = f.read()
        except Exception as e:
            try:
                response = requests.get(f"{baseurl}{fn}")
                response.raise_for_status()  # Raise an exception for any unsuccessful request
                with open(f"{app_path}/libs/{fn}", "w", encoding="UTF-8") as f:
                    f.write(response.text)
                with open(f"{app_path}/libs/{fn}", "r", encoding="UTF-8") as f:
                    script = f.read()
            except requests.exceptions.RequestException as e:
                return RTResult().failure(RTError(
                    self.pos_start, self.pos_end,
                    f"Failed to load script \"{fn}\"\n" + str(e),
                    exec_ctx
                ))
        _, error = run(fn, script)
        if error:
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                f"Failed to finish executing script \"{fn}\"\n" +
                error.as_string(),
                exec_ctx
            ))

    else:
        try: 
            importlib.import_module(f"_builtins.{fn}")
        except ImportError as e:
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                f"Failed to load script \"{fn}\"\n" + str(e),
                exec_ctx
            ))   

    return RTResult().success(String.none)

BuiltInFunction.execute_import.arg_names = ["fn"]
BuiltInFunction.execute_import.infinite = False
BuiltInFunction.execute_import.accept_none = False

@deco(BuiltInFunction)
def execute_run_ext(self, exec_ctx):
    fn = exec_ctx.symbol_table.get("fn")
    baseurl = "https://raw.githubusercontent.com/ZiadRabea/World-Programming/main/extensions/"
    if not isinstance(fn, String):
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "argument must be string",
            exec_ctx
        ))

    fn = fn.value + ".world"

    try:
        with open(f"{app_path}/libs/{fn}", "r", encoding="UTF-8") as f:
            script = f.read()
    except Exception as e:
        try:
            response = requests.get(f"{baseurl}{fn}")
            response.raise_for_status()  # Raise an exception for any unsuccessful request
            with open(f"{app_path}/../extensions/{fn}", "w", encoding="UTF-8") as f:
                f.write(response.text)
            with open(f"{app_path}/../extensions/{fn}", "r", encoding="UTF-8") as f:
                script = f.read()
        except requests.exceptions.RequestException as e:
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                f"Failed to load script \"{fn}\"\n" + str(e),
                exec_ctx
            ))

    _, error = run(fn, script)

    if error:
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            f"Failed to finish executing script \"{fn}\"\n" +
            error.as_string(),
            exec_ctx
        ))

    return RTResult().success(String.none)

BuiltInFunction.execute_run_ext.arg_names = ["fn"]
BuiltInFunction.execute_run_ext.infinite = False
BuiltInFunction.execute_run_ext.accept_none = False

@deco(BuiltInFunction)
def execute_exec(self, exec_ctx):
    code = exec_ctx.symbol_table.get('code')
    if not isinstance(code, String):
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "code must be a string",
            exec_ctx
        ))
    run("<stdin>", code.value)
    return RTResult().success(String.none)

BuiltInFunction.execute_exec.arg_names = ['code']
BuiltInFunction.execute_exec.infinite = False
BuiltInFunction.execute_exec.accept_none = False

@deco(BuiltInFunction)
def execute_eval(self, exec_ctx):
    result, error = run("<std-in>", exec_ctx.symbol_table.get('text').value)
    print(result)
    return RTResult().success(result.elements[0])

BuiltInFunction.execute_eval.arg_names = ['text']
BuiltInFunction.execute_eval.infinite = False
BuiltInFunction.execute_eval.accept_none = False

@deco(BuiltInFunction)
def execute_cwd(self, exec_ctx):
    result = os.getcwd()
    return RTResult().success(String(result))

BuiltInFunction.execute_cwd.arg_names = []
BuiltInFunction.execute_cwd.infinite = False
BuiltInFunction.execute_cwd.accept_none = False

@deco(BuiltInFunction)
def execute_exit(self, exec_ctx):
    sys.exit()
    return RTResult().success(String.none)

BuiltInFunction.execute_exit.arg_names = []
BuiltInFunction.execute_exit.infinite = False
BuiltInFunction.execute_exit.accept_none = False


BuiltInFunction.importfile = BuiltInFunction("import")
BuiltInFunction.run = BuiltInFunction("run")
BuiltInFunction.run_ext = BuiltInFunction("run_ext")
BuiltInFunction.eval = BuiltInFunction("eval")
BuiltInFunction.exec = BuiltInFunction("exec")
BuiltInFunction.cwd = BuiltInFunction("cwd")
BuiltInFunction.exit = BuiltInFunction("exit")

global_symbol_table.set(f"{data_dict['import']}", BuiltInFunction.importfile)
global_symbol_table.set(f"world", BuiltInFunction.run)
global_symbol_table.set(f"run", BuiltInFunction.run_ext)
global_symbol_table.set(f"{data_dict['exec']}", BuiltInFunction.exec)
global_symbol_table.set(f"{data_dict['eval']}", BuiltInFunction.eval)
global_symbol_table.set(f"{data_dict['cwd']}", BuiltInFunction.cwd)
global_symbol_table.set(f"exit", BuiltInFunction.exit)

def run(fn, text):
    # Generate tokens
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()
    if error: return None, error

    # Generate AST
    parser = Parser(tokens)
    ast = parser.parse()
    if ast.error: return None, ast.error

    # Run program
    interpreter = Interpreter()
    context = Context('<program>')
    context.symbol_table = global_symbol_table
    result = interpreter.visit(ast.node, context)

    return result.value, result.error
