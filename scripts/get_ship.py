"""Returns the ship given by the ship's symbol. Raises a ResponseException if the response code is not 200 (OK).
    
    Usage:
        run get_ship.py <symbol>
    
    Args:
        symbol (Str): The symbol of the ship to get.
        
    Returns:
        result (dict): Dict of the ship's data.
"""
# we need to pass this docstring to the cli
# it can be accessed with the __doc__ attribute of the global scope of this script

try:
    if args == []:
        raise Exception("No arguments provided")
    result = unwrap(client.fleet.get_my_ship(args[0])) # Get the ship with the given id
except ResponseException as e:
    raise e