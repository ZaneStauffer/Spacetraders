# This module has function bindings for the scripts.
import json
import spacetraders.api as api
import spacetraders.models as models
import spacetraders.types as types
import logger
import executor
from errors import *
# Converts a response object to a python dict
# Automatically raises an exception according to response code
# this can be called with unwrap(response) instead of json.loads(response.content)["data"]
# -> dict
def unwrap(response):
    """Converts a spacetrader API response to a python dict.
    
    Usage:
        ship_dict = unwrap(client.fleet.get_my_ship("ship"))
    
    Args:
        response (Response): The response from the spacetraders API.
        
    Returns:
        result (dict): Dict of the response's contents.
        
    Raises:
        ResponseException(status_code, message): If response status code is not 200 (OK).
    """
    if response.status_code != 200: # If response code is not 200
        raise ResponseException(response.status_code, response.content) # Raise exception
    return json.loads(response.content)["data"] # Return response as dict

# need a macro for automatically getting the return value of a script
#what we do now:
# result = {}
# execute("../scripts/get_ship.py", ["ship"], result)
# print(result["result"])
#what we want to do:
# print(execute("../scripts/get_ship.py", ["ship"]))
# -> dict

# run("../scripts/get_ship.py", ["ship"] ) -> dict
def run(script_path, client, *args): # *args is a list of arguments
    ''' Executes a script and returns the result as a dict.
    Args:
        script_path (str): The path to the script to execute.
        args (list): The arguments to pass to the script.
    Returns:
        result (dict): The result of the script.  
    '''
    try:
        BASE_PATH = "../scripts/" # The base path of the script folder
        scr_result = {} # The result of the script
        executor.execute(BASE_PATH + script_path, client, list(args), scr_result) # Execute the script
        return scr_result["result"] # Return the result
    except Exception as e:
        raise ScriptException(e) # Raise exception as ScriptException