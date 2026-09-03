from datatypes import *
import pyautogui

class deco:
    def __init__(self, cls):
        self.cls = cls

    def __call__(self, f):
        setattr(self.cls, f.__name__, f)
        return self.cls
    
@deco(BuiltInFunction)
def execute_typewrite(self, exec_ctx):
    text = exec_ctx.symbol_table.get('text')
    if isinstance(text, String) or isinstance(text, Number):
        pyautogui.typewrite(str(text.value))
    else:
        pyautogui.typewrite(str(text.elements))
    return RTResult().success(String.none)

BuiltInFunction.execute_typewrite.arg_names = ['text']
BuiltInFunction.execute_typewrite.infinite = False
BuiltInFunction.execute_typewrite.accept_none = False

@deco(BuiltInFunction)
def execute_cursor_location(self, exec_ctx):
    x = pyautogui.position()[0]
    y = pyautogui.position()[1]
    values = {
        "x": x,
        "y": y
    }
    return RTResult().success(Dict(values))

BuiltInFunction.execute_cursor_location.arg_names = []
BuiltInFunction.execute_cursor_location.infinite = False
BuiltInFunction.execute_cursor_location.accept_none = False

@deco(BuiltInFunction)
def execute_set_co_ords(self, exec_ctx):
    x = exec_ctx.symbol_table.get('x')
    y = exec_ctx.symbol_table.get('y')
    if not isinstance(x, Number) and not isinstance(y, Number):
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "argument must be a number",
            exec_ctx
        ))
    pyautogui.moveTo(x.value, y.value, duration=0.5)
    return RTResult().success(String.none)

BuiltInFunction.execute_set_co_ords.arg_names = ["x", "y"]
BuiltInFunction.execute_set_co_ords.infinite = False
BuiltInFunction.execute_set_co_ords.accept_none = False

@deco(BuiltInFunction)
def execute_click(self, exec_ctx):
    pyautogui.click()
    return RTResult().success(String.none)

BuiltInFunction.execute_click.arg_names = []
BuiltInFunction.execute_click.infinite = False
BuiltInFunction.execute_click.accept_none = False

@deco(BuiltInFunction)
def execute_press(self, exec_ctx):
    key = exec_ctx.symbol_table.get('key')
    try:
        pyautogui.press(key.value)
    except:
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "argument must be a valid keyboard key",
            exec_ctx
        ))
    return RTResult().success(String.none)

BuiltInFunction.execute_press.arg_names = ["key"]
BuiltInFunction.execute_press.infinite = False
BuiltInFunction.execute_press.accept_none = False

BuiltInFunction.typewrite = BuiltInFunction("typewrite")
BuiltInFunction.click = BuiltInFunction("click")
BuiltInFunction.press = BuiltInFunction("press")
BuiltInFunction.mouse_loc = BuiltInFunction("cursor_location")
BuiltInFunction.set_loc = BuiltInFunction("set_co_ords")

def append_to_global_symbol_table(data_dict):
    global_symbol_table.set(f"{data_dict['write']}", BuiltInFunction.typewrite)
    global_symbol_table.set(f"{data_dict['click']}", BuiltInFunction.click)
    global_symbol_table.set(f"{data_dict['mouse_location']}", BuiltInFunction.mouse_loc)
    global_symbol_table.set(f"{data_dict['set_location']}", BuiltInFunction.set_loc)
    global_symbol_table.set(f"{data_dict['press']}", BuiltInFunction.press)
