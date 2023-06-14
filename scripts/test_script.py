try:
    if args == []:
        raise Exception("No arguments provided")
    result = {}
    execute("../scripts/get_ship.py", client, args, result)
    print(result["result"])
except ResponseException as e:
    print(e.status_code)