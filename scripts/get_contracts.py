"""Returns the the agent's contracts.
    
    Usage:
        run get_contracts.py
        
    Returns:
        result (dict): Dict of the agent's contracts.
"""
#FIXME: Return contract model
try:
    result = unwrap(client.contracts.get_contracts()) # Get the agent's contracts
except ResponseException as e:
    raise e