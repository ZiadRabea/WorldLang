import serial
#from Interpreter import *
from RT_result import *
from Tokens import *
from Lexer import *
from datatypes import *
from Parser import *
from Errors import *

ser = ""
connected = False

class deco:
    def __init__(self, cls):
        self.cls = cls

    def __call__(self, f):
        setattr(self.cls, f.__name__, f)
        return self.cls
@deco(BuiltInFunction)
def execute_send(self, exec_ctx):
    global connected
    global ser
    com = exec_ctx.symbol_table.get('com')
    if not isinstance(com, String):
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "COM must be a string",
            exec_ctx
        ))
    port = exec_ctx.symbol_table.get('port')
    if not isinstance(port, Number):
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "port must be an integer",
            exec_ctx
        ))
    com = com.value
    port = port.value
    if not connected:
        try:
            ser = serial.Serial(com, port)
            time.sleep(2)
            connected = True
        except:
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                f"couldn't open {com}",
                exec_ctx
            ))
    data = exec_ctx.symbol_table.get('data')
    if isinstance(data, List):
        data_to_send = data.elements
        ser.write(data_to_send.encode())
    else:
        data_to_send = data.value
        ser.write(data_to_send.encode())
    time.sleep(0.5)

    return RTResult().success(String.none)

BuiltInFunction.execute_send.arg_names = ['com', 'port', 'data']
BuiltInFunction.execute_send.infinite = False
BuiltInFunction.execute_send.accept_none = False

@deco(BuiltInFunction)
def execute_receive(self, exec_ctx):
    global connected
    global ser
    com = exec_ctx.symbol_table.get('com')
    if not isinstance(com, String):
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "COM must be a string",
            exec_ctx
        ))
    port = exec_ctx.symbol_table.get('port')
    if not isinstance(port, Number):
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "port must be an integer",
            exec_ctx
        ))
    com = com.value
    port = port.value
    if not connected:
        try:
            ser = serial.Serial(com, port)
            time.sleep(2)
            connected = True
        except:
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                f"couldn't open {com}",
                exec_ctx
            ))

    try:
        received_data = ser.readline().decode().strip()
        # Read data from the Arduino

    except Exception as e:
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            f"Error while receiving data: {str(e)}",
            exec_ctx
        ))

    return RTResult().success(String(received_data))

BuiltInFunction.execute_receive.arg_names = ['com', 'port']
BuiltInFunction.execute_receive.infinite = False
BuiltInFunction.execute_receive.accept_none = False

BuiltInFunction.send = BuiltInFunction("send")
BuiltInFunction.receive = BuiltInFunction("receive")

global_symbol_table.set(f"{data_dict['receive']}", BuiltInFunction.receive)
global_symbol_table.set(f"{data_dict['send']}", BuiltInFunction.send)