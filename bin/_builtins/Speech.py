import speech_recognition
import pyttsx3
#from Interpreter import *
from RT_result import *
from Tokens import *
from Lexer import *
from datatypes import *
from Parser import *
from Errors import *

class deco:
    def __init__(self, cls):
        self.cls = cls

    def __call__(self, f):
        setattr(self.cls, f.__name__, f)
        return self.cls
    
@deco(BuiltInFunction)
def execute_listen(self, exec_ctx):
    recognizer = speech_recognition.Recognizer()
    language = exec_ctx.symbol_table.get('language')
    # Use the default microphone as the audio source
    with speech_recognition.Microphone() as source:
        print("Listening...")

        # Adjust for ambient noise levels
        recognizer.adjust_for_ambient_noise(source)

        # Listen to the user's input
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")

        # Use Google Speech Recognition to convert audio to text
        text = recognizer.recognize_google(audio, language=language.value)
        return RTResult().success(String(text))

    except speech_recognition.UnknownValueError:
        print("Sorry, I could not understand your speech.")

    except speech_recognition.RequestError:
        print("Sorry, there was an issue with the speech recognition service.")

    return RTResult().success(String.none)

BuiltInFunction.execute_listen.arg_names = ["language"]
BuiltInFunction.execute_listen.infinite = False
BuiltInFunction.execute_listen.accept_none = False

@deco(BuiltInFunction)
def execute_speak(self, exec_ctx):
    text = exec_ctx.symbol_table.get('text')
    if not isinstance(text, String):
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "argument must be a string",
            exec_ctx
        ))
        # Initialize the pyttsx3 engine
    engine = pyttsx3.init()

    # Set the properties for the speech
    engine.setProperty('rate', 150)  # Speed of speech (words per minute)
    engine.setProperty('volume', 0.8)  # Volume level (0.0 to 1.0)

    # Speak the given text
    engine.say(text.value)
    engine.runAndWait()
    return RTResult().success(String.none)
BuiltInFunction.execute_speak.arg_names = ['text']
BuiltInFunction.execute_speak.infinite = False
BuiltInFunction.execute_speak.accept_none = False


BuiltInFunction.listen = BuiltInFunction("listen")
BuiltInFunction.speak = BuiltInFunction("speak")

def append_to_global_symbol_table(data_dict):
    global_symbol_table.set(f"{data_dict['listen']}", BuiltInFunction.listen)
    global_symbol_table.set(f"{data_dict['speak']}", BuiltInFunction.speak)
