import random
from datatypes import *

class deco:
    def __init__(self, cls):
        self.cls = cls

    def __call__(self, f):
        setattr(self.cls, f.__name__, f)
        return self.cls

@deco(BuiltInFunction)
def execute_split(self, exec_ctx):
    text = exec_ctx.symbol_table.get('text')
    splitpoint = exec_ctx.symbol_table.get('splitpoint')
    if not isinstance(text, String) and not isinstance(splitpoint, String):
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "argument must be a string",
            exec_ctx
    ))
    result = [String(n) for n in text.value.split(splitpoint.value)]
    return RTResult().success(List(result))

BuiltInFunction.execute_split.arg_names = ["text", "splitpoint"]
BuiltInFunction.execute_split.infinite = False
BuiltInFunction.execute_split.accept_none = False

BuiltInFunction.split = BuiltInFunction("split")
global_symbol_table.set(f"{data_dict['split']}", BuiltInFunction.split)

@deco(BuiltInFunction)
def execute_uppercase(self, exec_ctx):
    text = exec_ctx.symbol_table.get('text')
    if not isinstance(text, String):
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "argument must be a string",
            exec_ctx
    ))
    result = text.value.upper()
    return RTResult().success(List(result))

BuiltInFunction.execute_uppercase.arg_names = ["text"]
BuiltInFunction.execute_uppercase.infinite = False
BuiltInFunction.execute_uppercase.accept_none = False

BuiltInFunction.upper = BuiltInFunction("uppercase")
global_symbol_table.set(f"{data_dict['uppercase']}", BuiltInFunction.upper)


@deco(BuiltInFunction)
def execute_lowercase(self, exec_ctx):
    text = exec_ctx.symbol_table.get('text')
    if not isinstance(text, String):
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "argument must be a string",
            exec_ctx
    ))
    result = text.value.lower()
    return RTResult().success(List(result))

BuiltInFunction.execute_lowercase.arg_names = ["text"]
BuiltInFunction.execute_lowercase.infinite = False
BuiltInFunction.execute_lowercase.accept_none = False

BuiltInFunction.lower = BuiltInFunction("lowercase")
global_symbol_table.set(f"{data_dict['lowercase']}", BuiltInFunction.lower)

@deco(BuiltInFunction)
def execute_capitalize(self, exec_ctx):
    text = exec_ctx.symbol_table.get('text')
    if not isinstance(text, String):
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "argument must be a string",
            exec_ctx
    ))
    result = text.value.capitalize()
    return RTResult().success(List(result))

BuiltInFunction.execute_capitalize.arg_names = ["text"]
BuiltInFunction.execute_capitalize.infinite = False
BuiltInFunction.execute_capitalize.accept_none = False

BuiltInFunction.capitalize = BuiltInFunction("capitalize")
global_symbol_table.set(f"{data_dict['capitalize']}", BuiltInFunction.capitalize)


@deco(BuiltInFunction)
def execute_contains(self, exec_ctx):
    text1 = exec_ctx.symbol_table.get('text1')
    text2 = exec_ctx.symbol_table.get('text2')
    if not isinstance(text1, String) or isinstance(text1, List):
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "second argument must be a iterable (String or List)",
            exec_ctx
    ))
    if isinstance(text2, String) : 
        text1 = text1.value
    else:
        text1 = text1.elements
    result = text2.value in text1
    return RTResult().success(Number(result))

BuiltInFunction.execute_contains.arg_names = ["text1", "text2"]
BuiltInFunction.execute_contains.infinite = False
BuiltInFunction.execute_contains.accept_none = False

BuiltInFunction.contains = BuiltInFunction("contains")
global_symbol_table.set(f"{data_dict['contains']}", BuiltInFunction.contains)


@deco(BuiltInFunction)
def execute_replace(self, exec_ctx):
    text1 = exec_ctx.symbol_table.get('text1')
    text2 = exec_ctx.symbol_table.get('text2')
    if not isinstance(text1, String):
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "first argument must be a String",
            exec_ctx
    ))
    if not isinstance(text2, List):
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "second argument must be a List",
            exec_ctx
    ))
    replacements = [i.value for i in text2.elements]
    result = text1.value.replace(replacements[0], replacements[1])
    return RTResult().success(String(result))

BuiltInFunction.execute_replace.arg_names = ["text1", "text2"]
BuiltInFunction.execute_replace.infinite = False
BuiltInFunction.execute_replace.accept_none = False

BuiltInFunction.replace = BuiltInFunction("replace")
global_symbol_table.set(f"{data_dict['replace']}", BuiltInFunction.replace)
