from matplotlib import pyplot as plt
from datatypes import *
import numpy as np
mode = "plot"

class deco:
    def __init__(self, cls):
        self.cls = cls

    def __call__(self, f):
        setattr(self.cls, f.__name__, f)
        return self.cls


@deco(BuiltInFunction)
def execute_plotting_mode(self, exec_ctx):
    global mode
    new_mode = exec_ctx.symbol_table.get('mode')
    if not isinstance(new_mode, String):
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "mode must be a String",
            exec_ctx
        ))
    try:
        if new_mode.value == "رسم":
            mode = "plot"
        elif new_mode.value == "نقاط":
            mode = "scatter"
        elif new_mode.value == "أعمدة":
            mode = "bar"
        else:
            mode = "plot"
        return RTResult().success(String.none)
    except Exception as e:
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "An Error accurd" + str(e),
            exec_ctx
        ))
BuiltInFunction.execute_plotting_mode.arg_names = ["mode"]
BuiltInFunction.execute_plotting_mode.infinite = False
BuiltInFunction.execute_plotting_mode.accept_none = False

BuiltInFunction.plotting_mode = BuiltInFunction("plotting_mode")
global_symbol_table.set(f"{data_dict['plotting_mode']}", BuiltInFunction.plotting_mode)


@deco(BuiltInFunction)
def execute_plot(self, exec_ctx):
    x = exec_ctx.symbol_table.get('x')
    y = exec_ctx.symbol_table.get('y')
    if not isinstance(x, List):
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "x must be a List",
            exec_ctx
        ))
    if not isinstance(y, List):
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "y must be a List",
            exec_ctx
        ))
    try:
        x = [i.value for i in x.elements] 
        y = [i.value for i in y.elements]
        if mode == "plot":
            plt.plot(x, y)
        elif mode == "scatter":
            plt.scatter(x,y)
        elif mode == "bar":
            plt.bar(x, y)
        else:
            plt.plot(x, y)
        plt.show()
        return RTResult().success(String.none)
    except Exception as e:
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "An Error accurd" + str(e),
            exec_ctx
        ))
BuiltInFunction.execute_plot.arg_names = ["x", "y"]
BuiltInFunction.execute_plot.infinite = False
BuiltInFunction.execute_plot.accept_none = False

BuiltInFunction.plot = BuiltInFunction("plot")
global_symbol_table.set(f"{data_dict['plot']}", BuiltInFunction.plot)