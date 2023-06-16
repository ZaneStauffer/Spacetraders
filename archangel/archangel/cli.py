from colorama import just_fix_windows_console
from colorama import Fore, Back, Style
import logger
import py_compile
import executor
import re
import code
from errors import *

# Command line interface module for Archangel CLI
class Session:
    from colorama import just_fix_windows_console
    from colorama import Fore, Back, Style

    def __init__(self, client):
        self.client = client
        self.state = True
        self.commands = {
            "help": {
                "desc": "Displays this help message",
                "usage": "help",
                "func": self._help,
                "args": []
            },
            "run": {
                "desc": "Runs a script",
                "usage": "run <script> <[args...]>",
                "func": self._run,
                "args": ["script", "[args...]"]
            },
            "processes": {
                "desc": "Displays a list of running processes",
                "usage": "processes",
                "func": self._processes,
                "args": []
            },
            "token": {
                "desc": "Sets the token for the client and updates the client",
                "usage": "token <token>",
                "func": self._token,
                "args": ["token"]
            },
            "exit": {
                "desc": "Exits the CLI",
                "usage": "exit",
                "func": lambda: exit(0),
                "args": []
            },
            "list": {
                "desc": "Lists all available scripts",
                "usage": "list",
                "func": self._list,
                "args": []
            },
            "register": {
                "desc": "Registers a new agent and updates the client",
                "usage": "register <symbol>",
                "func": self._register,
                "args": ["symbol"]
            },
            "exec": {
                "desc": "Allows execution of arbitrary python code",
                "usage": "exec",
                "func": self._exec_usr_code,
                "args": []
            },
        }
        just_fix_windows_console()

    # allows input and execution of arbitrary python code in the context of the cli
    # we need to pass the global scope of executor to this function so that it can be used in the context of the cli
    def _exec_usr_code(self): 
        print(logger.colorize("<:: BE CAREFUL WHEN EXECUTING ARBITRARY CODE ::>", Fore.RED))
        _globals = executor.get_globals(self.client) # get the global scope of executor
        code.interact(local=_globals) # start the interactive console with the global scope of executor

    def _register(self, symbol):
        pass
   
    def _help(self):
        print(logger.colorize("Available commands:", Fore.YELLOW))
        for command in self.commands:
            print("\t" + logger.colorize(command, Fore.GREEN) + ": " + self.commands[command]["desc"])
            print("\t\tUsage: " + self.commands[command]["usage"])

    def _list(self):
        print(logger.colorize("Available scripts:", Fore.YELLOW))
        for script_name in executor.get_scripts():
            print("\t" + logger.colorize(script_name, Fore.GREEN))
            # Print their docstring with _get_docstring
            docstring = self._get_docstring("../scripts/" + script_name)
            if docstring is not None:
                print("\t\t" + docstring.replace("\n", "\n\t\t"))    

    # Runs a given script
    # args is a list of arguments to pass to the script
    def _run(self, script, args=[]):
        if args == []: # If no args are given (just run) then list all available scripts
            self._list()
        try:
            script_path = "../scripts/" + script
            result = {}
            executor.execute(script_path, self.client, args, result)
            print(result["result"])
            
        except py_compile.PyCompileError as e:
            raise e
        except FileNotFoundError as e: # Also, list all available scripts
            raise e
        except SyntaxError as e:
            raise SyntaxError("Syntax error in script {0}".format(script))
        

    def _processes(self):
        print("Processes:")

    def _token(self, token):
        pass

    # Validates that a given command is valid.
    # checks number of arguments
    # Checks if the command exists in the commands dict
    # -> bool (True if valid, raise exception if not)
    def _validate_command(self, command):
        if command[0] == "run" and len(command[1]) >= 1: # Special case for run command
            # run command takes unlimited arguments
            return True
        if command[0] not in self.commands: # Check if command exists
            raise CommandNotFoundException()
        elif len(command[1]) != len(self.commands[command[0]]["args"]): # Check if number of arguments is correct
            raise InvalidArgsException(command[0], len(self.commands[command[0]]["args"]), len(command[1]))
        else:
            return True

    # Parses a given command string into a command and its arguments
    # Returns a tuple containing the command and its arguments
    # -> (command, [args]])
    def _parse_command(self, command_str):
        result = command_str.split()
        return (result[0], result[1:])
    
    # If we claim to be without sin, we deceive ourselves and the truth is not in us. 
    # If we confess our sins, he is faithful and just and will forgive us our sins and purify us from all unrighteousness.
    # If we claim we have not sinned, we make him out to be a liar and his word is not in us.
    # 1 John 1:8-10
    # anyways here's docstring
    # -> str
    def _get_docstring(self, script):
        if script is not None:
            with open(script, 'r') as _scr_file:
                _text = _scr_file.read()
                _docstring = r'\"\"\"([\s\S]*?)\"\"\"' # Regex for docstring
                _search = re.search(_docstring, _text)
                if _search is not None:
                    _docstring = _search.group(1)
                else:
                    _docstring = None
                    
                return _docstring
    
     # Starts the CLI loop and waits for user input
    def start(self):
        while(self.state):
            _input = input(":> ")
            usr_command = self._parse_command(_input) # Parse the command
            if usr_command[0] == "run" and len(usr_command[1]) == 0: # Special case for run command
                self._list()
            try:
                if self._validate_command(usr_command): # Validate the command
                    logger.log("Command {0} inputted with arguments {1}".format(
                        logger.colorize(usr_command[0], Fore.WHITE),
                        logger.colorize(str(usr_command[1]), Fore.WHITE)
                    ), should_save=True)
                    # RUN THE COMMAND !!!! :D :D :D :D :D :D :D :D :D :D :D :D :D :D :D :D :D 
                    if usr_command[0] == "run": # Special case for run command 
                        self.commands[usr_command[0]]["func"](usr_command[1][0], usr_command[1][1:]) 
                    else: # All other commands
                        self.commands[usr_command[0]]["func"](*usr_command[1]) # Call the command's function
                    # done (:
            except InvalidArgsException as e: # Argument length mismatch
                print(str(e))
            except CommandNotFoundException as e: # Command not found
                print(str(e))
            except py_compile.PyCompileError as e: # Syntax error in script
                print(logger.colorize("PyCompileError: ", Fore.RED) + str(e))
            except FileNotFoundError as e: # Script not found
                print(logger.colorize("FileNotFoundError: ", Fore.RED) + str(e))
            except SyntaxError as e: # Syntax error in script
                print(logger.colorize("SyntaxError: ", Fore.RED) + str(e))
            except Exception as e: # Generic exception
                print(logger.colorize("Exception: ", Fore.RED) + str(e))
