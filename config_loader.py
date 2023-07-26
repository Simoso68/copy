from json import loads, JSONDecodeError
from platform import system
from os import getenv, geteuid
from sys import exit

def replaceCFG(location):
    replacement = """
{
    "progressbar": {
        "bar": {
            "completed":"#",
            "incomplete":"-"
        },
        "container": {
            "opening":"[",
            "closing":"]"
        }
    },
    "backend": {
        "chars-per-iteration":256
    }
}""".replace("\n", "", 1)
    try:
        open(location, "w").write(replacement)
    except Exception as x:
        print("copy: not able to replace configuration file")
        print(f"Given information: {x}")
        exit()

def readfile(path):
    try:
        with open(path, "r") as conf:
            j = loads(conf.read())
            vallist = []
            vallist.append(j["progressbar"]["bar"]["completed"])
            vallist.append(j["progressbar"]["bar"]["incomplete"])
            vallist.append(j["progressbar"]["container"]["opening"])
            vallist.append(j["progressbar"]["container"]["closing"])
            vallist.append(j["backend"]["chars-per-iteration"])
            return vallist
    except FileNotFoundError:
        print(f"copy: config file does not exist at {path}, creating a new configuration file ...")
        replaceCFG(path)
    except KeyError:
        print(f"copy: configuration file at {path} is invalid, values are missing")
        exit()
    except JSONDecodeError:
        print(f"copy: configuration file at {path} is invalid, unvalid JSON format")
        exit()
    except Exception as x:
        print(f"copy: unknown exception during configuration replacement creation. \ncopy: Given information: {x}")
        exit()

def parseCFG():
    if system() == "Windows":
        conffile = "C:/Users/" + getenv("USERNAME") + "/.copy.conf.json"
        return readfile(conffile)
    elif system() == "Linux" or system() == "Darwin":
        if geteuid() == 0:
            conffile = "/root/.copy.conf.json"
        else:
            conffile = "/home/" + getenv("USER") + "/.copy.conf.json"
        return readfile(conffile)
    else:
        print("copy: was not able to detect your operating system, using default config.")
        return ["#", "-", "[", "]", 256]