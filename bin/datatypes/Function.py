from .Value import *
from .String import *
from .Number import *
from .List import *
from .Dict import *
import os
import sys
import requests
import json
import time
import importlib
Number.null = Number(0)
String.none = String("")
Number.false = Number(0)
Number.true = Number(1)
Number.math_PI = Number(3.141592653589793)

if getattr(sys, 'frozen', False):
    app_path = os.path.dirname(sys.executable)
else:
    app_path = os.path.dirname(os.path.abspath(__file__))

class CustomListEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, List) or isinstance(obj, Dict):
            return obj.elements
        elif isinstance(obj, String) or isinstance(obj, Number):
            return obj.value
        return super().default(obj)

class BaseFunction(Value):
    def __init__(self, name):
        super().__init__()
        self.name = name or "<anonymous>"

    def generate_new_context(self):
        new_context = Context(self.name, self.context, self.pos_start)
        new_context.symbol_table = SymbolTable(new_context.parent.symbol_table)
        return new_context

    def check_args(self, infinite, accept_none, arg_names, args):
        res = RTResult()

        if len(args) > len(arg_names):
            if infinite:
                return res.success(None)
            return res.failure(RTError(
                self.pos_start, self.pos_end,
                f"{len(args) - len(arg_names)} too many args passed into {self}",
                self.context
            ))

        if len(args) < len(arg_names):
            if len(arg_names) == 1 and accept_none:
                return res.success(None)
            else:
                return res.failure(RTError(
                    self.pos_start, self.pos_end,
                    f"{len(arg_names) - len(args)} too few args passed into {self}",
                    self.context
                ))

        return res.success(None)

    def populate_args(self, infinite, arg_names, args, exec_ctx):
        for i in range(len(args)):
            if infinite:
                arg_name = arg_names[0]
                # print(x for x in args)
                arg_value = List([x for x in args])
            else:
                arg_name = arg_names[i]
                arg_value = args[i]

            arg_value.set_context(exec_ctx)
            exec_ctx.symbol_table.set(arg_name, arg_value)

    def check_and_populate_args(self, infinite, accept_none, arg_names, args, exec_ctx):
        res = RTResult()
        res.register(self.check_args(infinite, accept_none, arg_names, args))
        if res.should_return(): return res
        self.populate_args(infinite, arg_names, args, exec_ctx)
        return res.success(None)
      
class BuiltInFunction(BaseFunction):
    def __init__(self, name, data_dict=None, runner=None):
        super().__init__(name)
        self.data_dict = data_dict
        self.runner = runner

    def execute(self, args):
        res = RTResult()
        exec_ctx = self.generate_new_context()

        method_name = f'execute_{self.name}'
        method = getattr(self, method_name, self.no_visit_method)

        res.register(
            self.check_and_populate_args(method.infinite, method.accept_none, method.arg_names, args, exec_ctx))
        if res.should_return(): return res

        return_value = res.register(method(exec_ctx))
        if res.should_return(): return res
        return res.success(return_value)

    def no_visit_method(self, node, context):
        raise Exception(f'No execute_{self.name} method defined')

    def copy(self):
        copy = BuiltInFunction(self.name, self.data_dict, self.runner)
        copy.set_context(self.context)
        copy.set_pos(self.pos_start, self.pos_end)
        return copy

    def __repr__(self):
        return f"<built-in function {self.name}>"

    #####################################

    def execute_print(self, exec_ctx):
        for i in exec_ctx.symbol_table.get('value').elements:
            if isinstance(i, List) or isinstance(i, Dict):
                print(i.elements)
            else:
                print(str(i.value))
        return RTResult().success(String.none)

    execute_print.arg_names = ['value']
    execute_print.infinite = True
    execute_print.accept_none = True

    def execute_print_ret(self, exec_ctx):
        return RTResult().success(String(str(exec_ctx.symbol_table.get('value'))))

    execute_print_ret.arg_names = ['value']
    execute_print_ret.infinite = True
    execute_print_ret.accept_none = True

    def execute_input(self, exec_ctx):
        message = exec_ctx.symbol_table.get('prompt') if exec_ctx.symbol_table.get('prompt') else ""
        text = input(message)
        return RTResult().success(String(text))

    execute_input.arg_names = ["prompt"]
    execute_input.infinite = False
    execute_input.accept_none = True

    def execute_input_int(self, exec_ctx):
        message = exec_ctx.symbol_table.get('prompt') if exec_ctx.symbol_table.get('prompt') else ""
        while True:
            text = input(message)
            try:
                number = int(text)
                break
            except ValueError:
                print(f"'{text}' must be an integer. Try again!")
        return RTResult().success(Number(number))

    execute_input_int.arg_names = ["prompt"]
    execute_input_int.infinite = False
    execute_input_int.accept_none = True

    def execute_clear(self, exec_ctx):
        os.system('cls' if os.name == 'nt' else 'cls')
        return RTResult().success(String.none)

    execute_clear.arg_names = []
    execute_clear.infinite = False
    execute_clear.accept_none = False

    def execute_is_number(self, exec_ctx):
        is_number = isinstance(exec_ctx.symbol_table.get("value"), Number)
        return RTResult().success(Number.true if is_number else Number.false)

    execute_is_number.arg_names = ["value"]
    execute_is_number.infinite = False
    execute_is_number.accept_none = False

    def execute_is_dict(self, exec_ctx):
        is_dict = isinstance(exec_ctx.symbol_table.get("value"), Dict)
        return RTResult().success(Number.true if is_dict else Number.false)

    execute_is_dict.arg_names = ["value"]
    execute_is_dict.infinite = False
    execute_is_dict.accept_none = False

    def execute_is_string(self, exec_ctx):
        is_number = isinstance(exec_ctx.symbol_table.get("value"), String)
        return RTResult().success(Number.true if is_number else Number.false)

    execute_is_string.arg_names = ["value"]
    execute_is_string.infinite = False
    execute_is_string.accept_none = False

    def execute_is_list(self, exec_ctx):
        is_number = isinstance(exec_ctx.symbol_table.get("value"), List)
        return RTResult().success(Number.true if is_number else Number.false)

    execute_is_list.arg_names = ["value"]
    execute_is_list.infinite = False
    execute_is_list.accept_none = False

    def execute_is_function(self, exec_ctx):
        is_number = isinstance(exec_ctx.symbol_table.get("value"), BaseFunction)
        return RTResult().success(Number.true if is_number else Number.false)

    execute_is_function.arg_names = ["value"]
    execute_is_function.infinite = False
    execute_is_function.accept_none = False

    def execute_append(self, exec_ctx):
        list_ = exec_ctx.symbol_table.get("list")
        value = exec_ctx.symbol_table.get("value")

        if not isinstance(list_, List):
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                "First argument must be list",
                exec_ctx
            ))

        list_.elements.append(value)
        return RTResult().success(String.none)

    execute_append.arg_names = ["list", "value"]
    execute_append.infinite = False
    execute_append.accept_none = False

    def execute_pop(self, exec_ctx):
        list_ = exec_ctx.symbol_table.get("list")
        index = exec_ctx.symbol_table.get("index")

        if not isinstance(list_, List):
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                "First argument must be list",
                exec_ctx
            ))

        if not isinstance(index, Number):
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                "Second argument must be number",
                exec_ctx
            ))

        try:
            element = list_.elements.pop(index.value)
        except:
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                'Element at this index could not be removed from list because index is out of bounds',
                exec_ctx
            ))
        return RTResult().success(element)

    execute_pop.arg_names = ["list", "index"]
    execute_pop.infinite = False
    execute_pop.accept_none = False

    def execute_extend(self, exec_ctx):
        listA = exec_ctx.symbol_table.get("listA")
        listB = exec_ctx.symbol_table.get("listB")

        if not isinstance(listA, List):
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                "First argument must be list",
                exec_ctx
            ))

        if not isinstance(listB, List):
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                "Second argument must be list",
                exec_ctx
            ))

        listA.elements.extend(listB.elements)
        return RTResult().success(String.none)

    execute_extend.arg_names = ["listA", "listB"]
    execute_extend.infinite = False
    execute_extend.accept_none = False

    def execute_len(self, exec_ctx):
        list_ = exec_ctx.symbol_table.get("list")
        if isinstance(list_, List):
            param = list_.elements
        elif isinstance(list_, String):
            param = list_.value
        else:
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                "Argument must be list",
                exec_ctx
            ))

        return RTResult().success(Number(len(param)))

    execute_len.arg_names = ["list"]
    execute_len.infinite = False
    execute_len.accept_none = False

    def execute_readfile(self, exec_ctx):
        fn = exec_ctx.symbol_table.get("fn")
        if not isinstance(fn, String):
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                "Second argument must be string",
                exec_ctx
            ))

        fn = fn.value

        if "https://" in fn or "http://" in fn:
            try:
                response = requests.get(fn)
                response.raise_for_status()  # Raise an exception for any unsuccessful request
                return RTResult().success(String(response.text))
            except requests.exceptions.RequestException as e:
                return RTResult().failure(RTError(
                    self.pos_start, self.pos_end,
                    f"Error occurred while fetching the file: \"{e}\"\n" + str(e),
                    exec_ctx
                ))

        try:
            with open(fn, "r", encoding="UTF-8") as f:
                content = f.read()
        except Exception as e:
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                f"Failed to load file \"{fn}\"\n" + str(e),
                exec_ctx
            ))

        return RTResult().success(String(content))

    execute_readfile.arg_names = ["fn"]
    execute_readfile.infinite = False
    execute_readfile.accept_none = False

    def execute_writefile(self, exec_ctx):
        fn = exec_ctx.symbol_table.get("fn")
        content = exec_ctx.symbol_table.get("content")

        if not isinstance(fn, String):
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                "First an Second argument must be string",
                exec_ctx
            ))

        fn = fn.value
        content = content.value
        try:
            with open(fn, "w", encoding="UTF-8") as f:
                content = f.write(content)
        except Exception as e:
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                f"Failed to load file \"{fn}\"\n" + str(e),
                exec_ctx
            ))

        return RTResult().success(String.none)

    execute_writefile.arg_names = ["fn", "content"]
    execute_writefile.infinite = False
    execute_writefile.accept_none = False

    def execute_to_string(self, exec_ctx):
        content = exec_ctx.symbol_table.get("content")

        content = content.elements
        try:
            output = json.dumps(content, indent=4, cls=CustomListEncoder)
        except Exception as e:
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                f"Failed to parse data",
                exec_ctx
            ))

        return RTResult().success(String(output))

    execute_to_string.arg_names = ["content"]
    execute_to_string.infinite = False
    execute_to_string.accept_none = False

    def execute_keys(self, exec_ctx):
        content = exec_ctx.symbol_table.get("dict")
        if not isinstance(content, Dict):
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                f"Argument must be a Dict",
                exec_ctx
            ))
        content = content.elements
        mylist = list()
        for i in content.keys():
            if isinstance(i, int):
                mylist.append(Number(i))
            if isinstance(i, str):
                mylist.append(String(i))
            if isinstance(i, list):
                mylist.append(List(i))
            if isinstance(i, dict):
                mylist.append(Dict(i))

        return RTResult().success(List(mylist))

    execute_keys.arg_names = ["dict"]
    execute_keys.infinite = False
    execute_keys.accept_none = False


    def execute_python(self, exec_ctx):
        exec(exec_ctx.symbol_table.get('code').value, locals())
        return RTResult().success(Number.null)

    execute_python.arg_names = ['code']
    execute_python.infinite = False
    execute_python.accept_none = False

    def execute_abspath(self, exec_ctx):
        return RTResult().success(String(f"{app_path}"))

    execute_abspath.arg_names = []
    execute_abspath.infinite = False
    execute_abspath.accept_none = False

    def execute_sum(self, exec_ctx):
        list_ = exec_ctx.symbol_table.get("list")

        if not isinstance(list_, List):
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                "Argument must be list",
                exec_ctx
            ))

        newlist = [int(f"{i}") for i in list_.elements]
        return RTResult().success(Number(sum(newlist)))

    execute_sum.arg_names = ["list"]
    execute_sum.infinite = False
    execute_sum.accept_none = False

    def execute_max(self, exec_ctx):
        list_ = exec_ctx.symbol_table.get("list")

        if not isinstance(list_, List):
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                "Argument must be list",
                exec_ctx
            ))
        newlist = [int(f"{i}") for i in list_.elements]
        return RTResult().success(Number(max(newlist)))

    execute_max.arg_names = ["list"]
    execute_max.infinite = False
    execute_max.accept_none = False

    def execute_min(self, exec_ctx):
        list_ = exec_ctx.symbol_table.get("list")

        if not isinstance(list_, List):
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                "Argument must be list",
                exec_ctx
            ))
        newlist = [int(f"{i}") for i in list_.elements]
        return RTResult().success(Number(min(newlist)))

    execute_min.arg_names = ["list"]
    execute_min.infinite = False
    execute_min.accept_none = False

    def execute_abs(self, exec_ctx):
        result = abs(int(exec_ctx.symbol_table.get('number').value))
        return RTResult().success(Number(result))

    execute_abs.arg_names = ['number']
    execute_abs.infinite = False
    execute_abs.accept_none = False

    def execute_int(self, exec_ctx):
        result = int(exec_ctx.symbol_table.get('number').value)
        return RTResult().success(Number(result))

    execute_int.arg_names = ['number']
    execute_int.infinite = False
    execute_int.accept_none = False

    def execute_float(self, exec_ctx):
        result = float(exec_ctx.symbol_table.get('number').value)
        return RTResult().success(Number(result))

    execute_float.arg_names = ['number']
    execute_float.infinite = False
    execute_float.accept_none = False

    def execute_str(self, exec_ctx):
        result = str(exec_ctx.symbol_table.get('number').value)
        return RTResult().success(String(result))

    execute_str.arg_names = ['number']
    execute_str.infinite = False
    execute_str.accept_none = False

    def execute_load_img(self, exec_ctx):
        print(
            "يبدوا أنك نسيت استدعاء مكتبة (Image)")

        return RTResult().success(Number.null)

    execute_load_img.arg_names = ['path']
    execute_load_img.infinite = False
    execute_load_img.accept_none = False

    def execute_save_img(self, exec_ctx):
        print(
            "يبدوا أنك نسيت استدعاء مكتبة (Image)")

        return RTResult().success(Number.null)

    execute_save_img.arg_names = ['list', 'path']
    execute_save_img.infinite = False
    execute_save_img.accept_none = False

    def execute_send(self, exec_ctx):
        print(
            "يبدوا انك نسيت استدعاء المكتبة (Serial)")
        return RTResult().success(Number.null)

    execute_send.arg_names = ['com', 'port', 'data']
    execute_send.infinite = False
    execute_send.accept_none = False


    def execute_sleep(self, exec_ctx):
        if not isinstance(exec_ctx.symbol_table.get('number'), Number):
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                "argument must be a number",
                exec_ctx
            ))
        time.sleep(exec_ctx.symbol_table.get('number').value)
        return RTResult().success(String.none)

    execute_sleep.arg_names = ['number']
    execute_sleep.infinite = False
    execute_sleep.accept_none = False

    def execute_listen(self, exec_ctx):
        print(
            "يبدوا انك نسيت استدعاء المكتبة (Speech)")

        return RTResult().success(Number.null)

    execute_listen.arg_names = []
    execute_listen.infinite = False
    execute_listen.accept_none = False

    def execute_speak(self, exec_ctx):
        print(
            "يبدوا انك نسيت استدعاء المكتبة (Speech)")
        return RTResult().success(Number.null)

    execute_speak.arg_names = ['text']
    execute_speak.infinite = False
    execute_speak.accept_none = False

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

    execute_exec.arg_names = ['code']
    execute_exec.infinite = False
    execute_exec.accept_none = False

    def execute_eval(self, exec_ctx):
        result, error = run("<std-in>", exec_ctx.symbol_table.get('text').value)
        print(result)
        return RTResult().success(result.elements[0])

    execute_eval.arg_names = ['text']
    execute_eval.infinite = False
    execute_eval.accept_none = False

    def execute_cwd(self, exec_ctx):
        result = os.getcwd()
        return RTResult().success(String(result))

    execute_cwd.arg_names = []
    execute_cwd.infinite = False
    execute_cwd.accept_none = False


    def execute_import(self, exec_ctx):
        fn = exec_ctx.symbol_table.get("fn")
        baseurl = "https://raw.githubusercontent.com/ZiadRabea/WorldLang/main/libs/"
        if not isinstance(fn, String):
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                "Second argument must be string",
                exec_ctx
            ))

        fn = fn.value
        if ".world" in fn:
            try:
                with open(f"{app_path}/../libs/{fn}", "r", encoding="UTF-8") as f:
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
                    
            print(self.runner)
            _, error = self.runner(fn, script)
            if error:
                return RTResult().failure(RTError(
                    self.pos_start, self.pos_end,
                    f"Failed to finish executing script \"{fn}\"\n" +
                    error.as_string(),
                    exec_ctx
                ))

        else:
            try: 
                module = importlib.import_module(f"_builtins.{fn}")
                module.append_to_global_symbol_table(self.data_dict)
            except ImportError as e:
                return RTResult().failure(RTError(
                    self.pos_start, self.pos_end,
                    f"Failed to load script \"{fn}\"\n" + str(e),
                    exec_ctx
                ))   

        return RTResult().success(String.none)

    execute_import.arg_names = ["fn"]
    execute_import.infinite = False
    execute_import.accept_none = False


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
        _, error = self.runner(fn, script)

        if error:
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                f"Failed to finish executing script \"{fn}\"\n" +
                error.as_string(),
                exec_ctx
            ))

        return RTResult().success(String.none)

    execute_run.arg_names = ["fn"]
    execute_run.infinite = False
    execute_run.accept_none = False


    def execute_run_ext(self, exec_ctx):
        fn = exec_ctx.symbol_table.get("fn")
        baseurl = "https://raw.githubusercontent.com/ZiadRabea/WorldLang/main/extensions/"
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

        _, error = self.runner(fn, script)

        if error:
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                f"Failed to finish executing script \"{fn}\"\n" +
                error.as_string(),
                exec_ctx
            ))

        return RTResult().success(String.none)

    execute_run_ext.arg_names = ["fn"]
    execute_run_ext.infinite = False
    execute_run_ext.accept_none = False


    def execute_exit(self, exec_ctx):
        sys.exit()
        return RTResult().success(String.none)

    execute_exit.arg_names = []
    execute_exit.infinite = False
    execute_exit.accept_none = False

global_symbol_table = SymbolTable()

def create_global_symbol_table(data_dict, runner):
    

    BuiltInFunction.print = BuiltInFunction("print")
    BuiltInFunction.print_ret = BuiltInFunction("print_ret")
    BuiltInFunction.input = BuiltInFunction("input")
    BuiltInFunction.input_int = BuiltInFunction("input_int")
    BuiltInFunction.clear = BuiltInFunction("clear")
    BuiltInFunction.is_number = BuiltInFunction("is_number")
    BuiltInFunction.is_string = BuiltInFunction("is_string")
    BuiltInFunction.is_dict = BuiltInFunction("is_dict")
    BuiltInFunction.is_list = BuiltInFunction("is_list")
    BuiltInFunction.is_function = BuiltInFunction("is_function")
    BuiltInFunction.append = BuiltInFunction("append")
    BuiltInFunction.pop = BuiltInFunction("pop")
    BuiltInFunction.extend = BuiltInFunction("extend")
    BuiltInFunction.len = BuiltInFunction("len")
    BuiltInFunction.sum = BuiltInFunction("sum")
    BuiltInFunction.max = BuiltInFunction("max")
    BuiltInFunction.min = BuiltInFunction("min")
    BuiltInFunction.abs = BuiltInFunction("abs")
    BuiltInFunction.run = BuiltInFunction("run")

    BuiltInFunction.readfile = BuiltInFunction("readfile")
    BuiltInFunction.writefile = BuiltInFunction("writefile")
    BuiltInFunction.python = BuiltInFunction("python")
    BuiltInFunction.int = BuiltInFunction("int")
    BuiltInFunction.str = BuiltInFunction("str")
    BuiltInFunction.float = BuiltInFunction("float")
    BuiltInFunction.load_img = BuiltInFunction("load_img")
    BuiltInFunction.save_img = BuiltInFunction("save_img")
    BuiltInFunction.send = BuiltInFunction("send")
    BuiltInFunction.listen = BuiltInFunction("listen")
    BuiltInFunction.speak = BuiltInFunction("speak")
    BuiltInFunction.sleep = BuiltInFunction("sleep")
    BuiltInFunction.to_string = BuiltInFunction("to_string")
    BuiltInFunction.keys = BuiltInFunction("keys")
    BuiltInFunction.abspath = BuiltInFunction("abspath")
    BuiltInFunction.eval = BuiltInFunction("eval")
    BuiltInFunction.exec = BuiltInFunction("exec")
    BuiltInFunction.cwd = BuiltInFunction("cwd")
    BuiltInFunction.importfile = BuiltInFunction("import", data_dict, runner)
    BuiltInFunction.run = BuiltInFunction("run", data_dict, runner)
    BuiltInFunction.run_ext = BuiltInFunction("run_ext", data_dict, runner)

    BuiltInFunction.exit = BuiltInFunction("exit")

    global_symbol_table.set(f"{data_dict['null']}", Number.null)
    global_symbol_table.set(f"{data_dict['false']}", Number.false)
    global_symbol_table.set(f"{data_dict['true']}", Number.true)
    global_symbol_table.set("MATH_PI", Number.math_PI)
    global_symbol_table.set(f"{data_dict['print']}", BuiltInFunction.print)
    global_symbol_table.set("print_ret", BuiltInFunction.print_ret)
    global_symbol_table.set(f"{data_dict['input']}", BuiltInFunction.input)
    global_symbol_table.set(f"{data_dict['int_input']}", BuiltInFunction.input_int)
    global_symbol_table.set(f"{data_dict['clear']}", BuiltInFunction.clear)
    global_symbol_table.set("cls", BuiltInFunction.clear)
    global_symbol_table.set(f"{data_dict['is_int']}", BuiltInFunction.is_number)
    global_symbol_table.set(f"{data_dict['is_str']}", BuiltInFunction.is_string)
    global_symbol_table.set(f"{data_dict['is_lst']}", BuiltInFunction.is_list)
    global_symbol_table.set(f"{data_dict['is_func']}", BuiltInFunction.is_function)
    global_symbol_table.set(f"{data_dict['append']}", BuiltInFunction.append)
    global_symbol_table.set(f"{data_dict['pop']}", BuiltInFunction.pop)
    global_symbol_table.set(f"{data_dict['extend']}", BuiltInFunction.extend)
    global_symbol_table.set(f"{data_dict['len']}", BuiltInFunction.len)
    global_symbol_table.set("world", BuiltInFunction.run)
    global_symbol_table.set(f"{data_dict['readf']}", BuiltInFunction.readfile)
    global_symbol_table.set(f"{data_dict['writef']}", BuiltInFunction.writefile)
    global_symbol_table.set(f"python", BuiltInFunction.python)
    global_symbol_table.set(f"{data_dict['sum']}", BuiltInFunction.sum)
    global_symbol_table.set(f"{data_dict['max']}", BuiltInFunction.max)
    global_symbol_table.set(f"{data_dict['min']}", BuiltInFunction.min)
    global_symbol_table.set(f"{data_dict['abs']}", BuiltInFunction.abs)
    global_symbol_table.set(f"{data_dict['int']}", BuiltInFunction.int)
    global_symbol_table.set(f"{data_dict['float']}", BuiltInFunction.int)
    global_symbol_table.set(f"{data_dict['str']}", BuiltInFunction.str)
    global_symbol_table.set(f"{data_dict['load']}", BuiltInFunction.load_img)
    global_symbol_table.set(f"{data_dict['save_img']}", BuiltInFunction.save_img)
    global_symbol_table.set(f"{data_dict['send']}", BuiltInFunction.send)
    global_symbol_table.set(f"{data_dict['listen']}", BuiltInFunction.listen)
    global_symbol_table.set(f"{data_dict['speak']}", BuiltInFunction.speak)
    global_symbol_table.set(f"{data_dict['is_dict']}", BuiltInFunction.is_dict)
    global_symbol_table.set(f"{data_dict['sleep']}", BuiltInFunction.sleep)
    global_symbol_table.set(f"{data_dict['to_string']}", BuiltInFunction.to_string)
    global_symbol_table.set(f"{data_dict['keys']}", BuiltInFunction.keys)
    global_symbol_table.set(f"{data_dict['abspath']}", BuiltInFunction.abspath)
    global_symbol_table.set(f"{data_dict['exec']}", BuiltInFunction.exec)
    global_symbol_table.set(f"{data_dict['eval']}", BuiltInFunction.eval)
    global_symbol_table.set(f"{data_dict['cwd']}", BuiltInFunction.cwd)
    global_symbol_table.set(f"{data_dict['import']}", BuiltInFunction.importfile)
    global_symbol_table.set(f"world", BuiltInFunction.run)
    global_symbol_table.set(f"run", BuiltInFunction.run_ext)

    global_symbol_table.set(f"exit", BuiltInFunction.exit)

    return global_symbol_table