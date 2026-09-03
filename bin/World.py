from run import run
import json
from setlang import set_lang
import os
import sys
if getattr(sys, 'frozen', False):
    app_path = os.path.dirname(sys.executable)
else:
    app_path = os.path.dirname(os.path.abspath(__file__))

while True:
    text = input('World >> ')
    if text == "setlang":
        lang = input("Enter your language File Name. ex: English_KW (leave blank for automatic language detection) : ")
        set_lang(lang)
    elif text == "libman":
        path = app_path.replace('\\', '/')
        result, error = run('<stdin>', f"world('{path}/libman.world')")
        if error:
            print(error.as_string())
        elif result:
            print(u"{}".format(result))
    elif text == "langman":
        path = app_path.replace('\\', '/')
        result, error = run('<stdin>', f"world('{path}/langman.world')")
        if error:
            print(error.as_string())
        elif result:
            print(u"{}".format(result))
    elif text == "extman":
        path = app_path.replace('\\', '/')
        result, error = run('<stdin>', f"world('{path}/extman.world')")
        if error:
            print(error.as_string())
        elif result:
            print(u"{}".format(result))
    else:
        result, error = run('<stdin>', text)

        if error:
            print(error.as_string())
        elif result:
            print(u"{}".format(result))
