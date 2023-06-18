"""
Prints the ship's data given its symbol.

Usage: 
    run display_ship.py <symbol>

Args:
    symbol (Str): The symbol of the ship to display.

Raises:
    ResponseException(status_code, message): If response status code is not 200 (OK).
"""
# SYMBOL

try:
    if args == []:
        raise Exception("No arguments provided")
    result = unwrap(client.fleet.get_my_ship(args[0])) # Get the ship with the given id
    print(result)
except ResponseException as e:
    raise e