try:
    if args == []:
        raise Exception("No arguments provided")
    _test_case = unwrap(client.fleet.get_my_ship(args[0]))
    # TODO: Return the ship dict
    print(str(_test_case))
except ResponseException as e:
    raise e