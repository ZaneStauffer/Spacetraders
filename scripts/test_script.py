try:
    if args == []:
        raise Exception("No arguments provided")
    _test_case = unwrap(client.fleet.refuel_ship(args[0]))
    print(str(_test_case))
except ResponseException as e:
    print(e.status_code)