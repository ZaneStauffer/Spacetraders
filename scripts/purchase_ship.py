"""Purchases a ship at a shipyard. 
    
    Usage:
        run purchase_ship.py ship_type shipyard_symbol
    Args:
        ship_type (str): The type of ship to purchase from the shipyard (e.g. SHIP_MINING_DRONE)
        shipyard_symbol (str): The symbol of the shipyard to purchase from.
    Returns:
        ship (dict): The purchased ship if purchase is successful
    Raises:
      ResponseException(status_code, message)
"""
