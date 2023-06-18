"""
Given a system symbol, return a list of the system's waypoints.

Args:
    symbol (str): The symbol of the system to get the waypoints of.

Returns:
    waypoints (list): List of the system's waypoints.

Raises:
    ResponseException(status_code, message): If response status code is not 200 (OK).
"""
try:
    if args == []:
        raise Exception("No arguments provided. Please provide the system symbol.")
    result = unwrap(client.systems.get_system_waypoints(args[0])) # Get the system's waypoints
except ResponseException as e:
    raise e
