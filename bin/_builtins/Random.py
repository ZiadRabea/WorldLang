import random
from datatypes import *

class deco:
    def __init__(self, cls):
        self.cls = cls

    def __call__(self, f):
        setattr(self.cls, f.__name__, f)
        return self.cls

@deco(BuiltInFunction)
def execute_random_gen(self, exec_ctx):
    n1 = exec_ctx.symbol_table.get('n1')
    n2 = exec_ctx.symbol_table.get('n2')
    if not isinstance(n1, Number) and not isinstance(n2, Number):
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "argument must be a number",
            exec_ctx
    ))
    result = random.randint(n1.value, n2.value)
    return RTResult().success(Number(result))

BuiltInFunction.execute_random_gen.arg_names = ["n1", "n2"]
BuiltInFunction.execute_random_gen.infinite = False
BuiltInFunction.execute_random_gen.accept_none = False

BuiltInFunction.gen_random = BuiltInFunction("random_gen")

def append_to_global_symbol_table(data_dict):
    global_symbol_table.set(f"{data_dict['gen_random']}", BuiltInFunction.gen_random)
    print(global_symbol_table.get(data_dict['gen_random']))