####################
# Imports
####################
from datatypes import *
import google.generativeai as genai
from rich.console import Console
from rich.markdown import Markdown

import os 
####################
# Constants
####################
genai.configure(api_key=os.environ.get("GenAI_API_Key"))
model = genai.GenerativeModel('gemini-1.5-flash')

class deco:
    def __init__(self, cls):
        self.cls = cls

    def __call__(self, f):
        setattr(self.cls, f.__name__, f)
        return self.cls

###################
# Logic
###################
@deco(BuiltInFunction)
def execute_run_ai(self, exec_ctx):
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

    chat = model.start_chat(history=[])
    chat.send_message("you are a coding model, you take ideas and generate python code immediately without any introductions or extra text or explanation, example : input = show hello world on the console, response = print('Hello world'), just this do not include explanation .") 
    chat.send_message("example 1 : input = print hello world please, output = print('Hello world')")
    chat.send_message("example 2 : input = save a string input to a variable called name, output = name = input('Enter your name please')")

    response = model.generate_content(f"{script}, don't explain the code and test the function.")
    exec(response.text.replace("```python", "").replace("```",""))
    
    return RTResult().success(String.none)

BuiltInFunction.execute_run_ai.arg_names = ["fn"]
BuiltInFunction.execute_run_ai.infinite = False
BuiltInFunction.execute_run_ai.accept_none = False


@deco(BuiltInFunction)
def execute_generate(self, exec_ctx):
    text = exec_ctx.symbol_table.get("text")
    fn = exec_ctx.symbol_table.get("file")
    if not text or text == "":
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "First Argument (Prompt) is Required",
            exec_ctx
        ))
    if not isinstance(fn, String):
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "Second argument must be string",
            exec_ctx
        ))
    chat = model.start_chat(history=[])
    fn = fn.value
    if fn != "":
        try:
            with open(fn, "r", encoding="UTF-8") as f:
                script = f.read()
                chat.send_message(f"{text}, {script}")
    
                response = model.generate_content(f"{text}, {script}")
                result = response.text
                Console().print(Markdown(result))
                return RTResult().success(String(f"{result}"))

    
        except Exception as e:
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                f"Failed to load script \"{fn}\"\n" + str(e),
                exec_ctx
            ))
    else :
        chat.send_message(f"{text}")
        response = model.generate_content(f"{text}")
        return RTResult().success(String(f"{response.text}"))
    
BuiltInFunction.execute_generate.arg_names = ["text", "file"]
BuiltInFunction.execute_generate.infinite = False
BuiltInFunction.execute_generate.accept_none = False


BuiltInFunction.generate = BuiltInFunction("generate")
BuiltInFunction.run_ai = BuiltInFunction("run_ai")


def append_to_global_symbol_table(data_dict):
    global_symbol_table.set(f"{data_dict['generate']}", BuiltInFunction.generate)
    global_symbol_table.set(f"run_ai", BuiltInFunction.run_ai)
