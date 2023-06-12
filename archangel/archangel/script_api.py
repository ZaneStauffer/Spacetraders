# This module has function bindings for the scripts.
import json
import spacetraders.api as api
import spacetraders.models as models
import spacetraders.types as types
import logger
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
