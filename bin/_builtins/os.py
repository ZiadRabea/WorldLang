##################
# Imports
##################
import os
import platform
import webbrowser
from datatypes import *

##################
# Constants
##################
class deco:
    def __init__(self, cls):
        self.cls = cls

    def __call__(self, f):
        setattr(self.cls, f.__name__, f)
        return self.cls
    
##################
# Logic
##################
@deco(BuiltInFunction)
def execute_chdir(self, exec_ctx):
    path = exec_ctx.symbol_table.get('path')
    if not isinstance(path, String):
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "path must be a string",
            exec_ctx
        ))
    try:
        os.chdir(f"{path.value}")
        return RTResult().success(String.none)
    except:
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "Error : Dir doesn't exist",
            exec_ctx
        ))
BuiltInFunction.execute_chdir.arg_names = ["path"]
BuiltInFunction.execute_chdir.infinite = False
BuiltInFunction.execute_chdir.accept_none = False

@deco(BuiltInFunction)
def execute_mkdir(self, exec_ctx):
    path = exec_ctx.symbol_table.get('path')
    if not isinstance(path, String):
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "path must be a string",
            exec_ctx
        ))
    os.mkdir(f"{path.value}")
    return RTResult().success(String.none)

BuiltInFunction.execute_mkdir.arg_names = ["path"]
BuiltInFunction.execute_mkdir.infinite = False
BuiltInFunction.execute_mkdir.accept_none = False

@deco(BuiltInFunction)
def execute_visit_url(self, exec_ctx):
    url = exec_ctx.symbol_table.get('url')
    if not isinstance(url, String):
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "path must be a string",
            exec_ctx
        ))
    webbrowser.open(f"{url.value}")
    return RTResult().success(String.none)

BuiltInFunction.execute_visit_url.arg_names = ["url"]
BuiltInFunction.execute_visit_url.infinite = False
BuiltInFunction.execute_visit_url.accept_none = False

@deco(BuiltInFunction)
def execute_processor(self, exec_ctx):
    result = str(platform.processor())
    return RTResult().success(String(result))

BuiltInFunction.execute_processor.arg_names = []
BuiltInFunction.execute_processor.infinite = False
BuiltInFunction.execute_processor.accept_none = False

@deco(BuiltInFunction)
def execute_platform(self, exec_ctx):
    result = str(platform.platform())
    return RTResult().success(String(result))

BuiltInFunction.execute_platform.arg_names = []
BuiltInFunction.execute_platform.infinite = False
BuiltInFunction.execute_platform.accept_none = False

@deco(BuiltInFunction)
def execute_machine(self, exec_ctx):
    result = str(platform.machine())
    return RTResult().success(String(result))

BuiltInFunction.execute_machine.arg_names = []
BuiltInFunction.execute_machine.infinite = False
BuiltInFunction.execute_machine.accept_none = False

@deco(BuiltInFunction)
def execute_list_dir(self, exec_ctx):
    dir = exec_ctx.symbol_table.get('dir')
    if not isinstance(dir, String):
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "path must be a string",
            exec_ctx
    ))
    try:
        lst = os.listdir(dir.value) if dir.value != "" else os.listdir()
        result = [String(x) for x in lst]
        return RTResult().success(List(result))
    except Exception as e:
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "Error : Please make sure the dir exists",
            exec_ctx
        ))
        
BuiltInFunction.execute_list_dir.arg_names = ["dir"]
BuiltInFunction.execute_list_dir.infinite = False
BuiltInFunction.execute_list_dir.accept_none = False


@deco(BuiltInFunction)
def execute_is_dir(self, exec_ctx):
    dir = exec_ctx.symbol_table.get('dir')
    if not isinstance(dir, String):
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "path must be a string",
            exec_ctx
    ))
    result = os.path.isdir(dir.value)
    return RTResult().success(Number(result))

BuiltInFunction.execute_is_dir.arg_names = ["dir"]
BuiltInFunction.execute_is_dir.infinite = False
BuiltInFunction.execute_is_dir.accept_none = False

@deco(BuiltInFunction)
def execute_move(self, exec_ctx):
    dir = exec_ctx.symbol_table.get('dir')
    fn = exec_ctx.symbol_table.get('fn')
    if not isinstance(dir, String):
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "path must be a string",
            exec_ctx
    ))
    try:

        result = os.replace(f'{fn.value}', f'{dir.value}/{fn.value}')
        return RTResult().success(String.none)
    except Exception as e:
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "Error : Please check file name and make sure the dir exists",
            exec_ctx
        ))
BuiltInFunction.execute_move.arg_names = ["fn", "dir"]
BuiltInFunction.execute_move.infinite = False
BuiltInFunction.execute_move.accept_none = False

@deco(BuiltInFunction)
def execute_system(self, exec_ctx):
    fn = exec_ctx.symbol_table.get('fn')
    if not isinstance(fn, String):
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "path must be a string",
            exec_ctx
    ))
    try:
        result = os.system(f"{fn.value}")
        return RTResult().success(String.none)
    except Exception as e:
         return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "Error : " + str(e),
            exec_ctx
    ))
BuiltInFunction.execute_system.arg_names = ["fn"]
BuiltInFunction.execute_system.infinite = False
BuiltInFunction.execute_system.accept_none = False

BuiltInFunction.chdir = BuiltInFunction("chdir")
BuiltInFunction.mkdir = BuiltInFunction("mkdir")
BuiltInFunction.visit_url = BuiltInFunction("visit_url")
BuiltInFunction.processor = BuiltInFunction("processor")
BuiltInFunction.os = BuiltInFunction("platform")
BuiltInFunction.architecture = BuiltInFunction("machine")
BuiltInFunction.list_dir = BuiltInFunction("list_dir")
BuiltInFunction.is_dir = BuiltInFunction("is_dir")
BuiltInFunction.move = BuiltInFunction("move")
BuiltInFunction.system = BuiltInFunction("system")

def append_to_global_symbol_table(data_dict):

    global_symbol_table.set(f"{data_dict['system']}", BuiltInFunction.system)
    global_symbol_table.set(f"{data_dict['chdir']}", BuiltInFunction.chdir)
    global_symbol_table.set(f"{data_dict['mkdir']}", BuiltInFunction.mkdir)
    global_symbol_table.set(f"{data_dict['visit']}", BuiltInFunction.visit_url)
    global_symbol_table.set(f"{data_dict['processor']}", BuiltInFunction.processor)
    global_symbol_table.set(f"{data_dict['os']}", BuiltInFunction.os)
    global_symbol_table.set(f"{data_dict['architecture']}", BuiltInFunction.architecture)
    global_symbol_table.set(f"{data_dict['list_dir']}", BuiltInFunction.list_dir)
    global_symbol_table.set(f"{data_dict['is_dir']}", BuiltInFunction.is_dir)
    global_symbol_table.set(f"{data_dict['move']}", BuiltInFunction.move)
