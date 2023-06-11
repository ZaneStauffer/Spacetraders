import time
from colorama import Fore, Back, Style

LOG_LOCATION = "logs/"

def log(message, should_save=False):
    print(time.strftime("[%Y-%m-%d %H:%M:%S]", time.localtime()) + "::> " + message)
    # TODO: if should_save is true then save to log file
    
def colorize(message, color):
    return color + message + Fore.RESET