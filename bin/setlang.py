import subprocess, os

def set_lang(value):
    try : 
        result = subprocess.run(
            ["setx", "wlanguage", str(value)],
            capture_output=True,
            text=True,
            check=True
        )
        
        # Update current process environment so get_lang() works immediately
        os.environ["wlanguage"] = str(value)
        print("Language changed successfully.")
    except:
        print("something went wrong")


def get_lang():
    language = os.environ.get("wlanguage")
    return  language