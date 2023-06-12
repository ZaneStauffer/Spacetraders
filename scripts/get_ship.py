try:
    if args == []:
        raise Exception("No arguments provided")
    result = unwrap(client.fleet.get_my_ship(args[0])) # Get the ship with the given id
except ResponseException as e:
    raise e