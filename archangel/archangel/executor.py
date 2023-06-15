import sys
import os
import py_compile
import ast
import spacetraders
from colorama import Fore, Back, Style
# This module executes user scripts. It validates them, restricts size, spawns a new process, and executes it while providing API
import logger
from script_api import unwrap
from errors import ResponseException

FILE_SIZE_LIMIT_MB = 1 #MB

def execute(file_path, client, args, result={}):
    print(spacetraders.__file__)
    # We need to pass the client to the script so it can use the API
    _scr_client = client
    #_locals = locals() # includes _scr_client
    _globals = {
        "client": _scr_client,
        "logger": logger,
        "spacetraders": spacetraders,
        "args" : args,
        "unwrap": unwrap,
        "ResponseException": ResponseException,
        #FIXME: v v v 
        "execute": execute,
    }
    # FIXME: Currently, the token field of the client object can be accessed from the script.
    # This is a security issue. We need to find a way to restrict access to the token field.

    # Validate file path, ext, size
    if _validate_file(file_path):
        try:
            if scr_ast := _validate_compile(file_path): # Compiles script and returns AST
                # Execute script
                # TODO: spawn new process
                _global_keys = str(list(_globals.keys()))
                logger.log("Executing {f} with globals {g} and args {a}".format(
                    f=logger.colorize(file_path, Fore.WHITE),
                    g=logger.colorize(_global_keys, Fore.WHITE),
                    a=logger.colorize(str(_globals["args"]), Fore.WHITE)
                ), should_save=True)
                exec(compile(scr_ast, filename=file_path, mode='exec'), _globals, result)
            else: # If False or None, propagate error
                # TODO: this error doesnt give much info about the error itself (line number, etc)
                raise SyntaxError("Unable to compile file", scr_ast)
        except py_compile.PyCompileError as e: # If unable to compile, propagate error
            raise e
    else: # If file does not exist or is not a .py file, propagate error
        raise FileNotFoundError("File does not exist or is not a .py file")

# Checks if file exists and is a .py file. Returns true if valid, false if not
def _validate_file(file_path):
    try:
        if(os.path.isfile(file_path) and file_path.endswith(".py")):
            return _validate_file_size(file_path, FILE_SIZE_LIMIT_MB) if True else False
        else:
            return False
    except: 
        return False
    
# Checks if the file size is less than the set limit
def _validate_file_size(file_path, size_mb=1):
    try:
        file_size = os.stat(file_path).st_size / (1024*1024) # We divide by (1024*1024) to get the size in MB
        return file_size <= size_mb if True else False
    except: 
        return False

# Compiles the file into an AST and returns it. Propagates error  if unable to compile
def _validate_compile(file_path):
    try:
        _script = ast.parse(open(file_path).read(), filename=file_path, mode='exec')
        return _script
    except py_compile.PyCompileError as e:
        logger.log("Unable to compile file")
        raise e
    except FileNotFoundError as e:
        logger.log("File does not exist")
        raise e

# Returns a list of all scripts in the scripts folder
def get_scripts():
    scripts = []
    for file in os.listdir("../scripts"):
        if file.endswith(".py"):
            scripts.append(file)
    return scripts