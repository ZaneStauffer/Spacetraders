from colorama import just_fix_windows_console
from colorama import Fore, Back, Style
import logger
import json

# ============= Command Exception ===============
class InvalidCommandException(Exception): pass
# Sub Exceptions for invalid commands
class InvalidArgsException(InvalidCommandException):
    def __init__(self, command, expected, actual):
        self.command = command
        self.expected = expected
        self.actual = actual

    def __str__(self):
        return Fore.RED + "InvalidArgsException:" + Fore.RESET + " Command '{0}' expected {1} arguments, got {2} instead"\
        .format(Fore.WHITE + str(self.command) + Fore.RESET,
                Fore.WHITE + str(self.expected) + Fore.RESET,
                Fore.WHITE + str(self.actual) + Fore.RESET
               )
# Command not found exception
class CommandNotFoundException(InvalidCommandException):
    def __str__(self):
        return Fore.RED + "CommandNotFoundException:" + Fore.RESET + " Command not found."
# =================================================

# ============= Response Exceptions ===================
class ResponseException(Exception):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message

    def __str__(self):
        return logger.colorize("ResponseException:", Fore.RED) + " Response status code is not 200. Status code: {0} Message: {1}"\
            .format(logger.colorize(str(self.status_code),Fore.RED),
                    logger.colorize(str(json.loads(self.message)["error"]["message"]), Fore.RED))
# =====================================================
# ============= Script Exceptions =====================
class ScriptException(Exception):
    def __init__(self, message):
        self.message = message