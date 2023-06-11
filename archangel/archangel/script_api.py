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
    if response.status_code != 200: # If response code is not 200
        raise ResponseException(response.status_code, response.content) # Raise exception
    return json.loads(response.content)["data"] # Return response as dict
