from spacetraders.models import GetSystemWaypointsResponse200
from spacetraders.types import Response
import json
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
    _wp_res: Response[GetSystemWaypointsResponse200] = client.systems.get_system_waypoints(args[0]) # Get the system's waypoints
    waypoints = _wp_res.parsed.data # Get the waypoints from the response
    result = [wp for wp in waypoints] # Convert waypoints to list
except ResponseException as e:
    raise e
# try and use model to get waypoints