"""
Prints the ship's data given its symbol.

Usage: 
    run display_ship.py <symbol>

Args:
    symbol (Str): The symbol of the ship to display.

Raises:
    ResponseException(status_code, message): If response status code is not 200 (OK).
"""
# this is disgusting. i have no words
# i'm sorry
# i'm so sorry

def main():
    import datetime
    from colorama import Fore, Back, Style
    
    def get_frame_bar(ship, length):
        _frame_result = {}
        _frame_args = [
            ship["frame"]["condition"],
            100,
            length
        ]
        execute("../scripts/format_bar.py", client, _frame_args, _frame_result)
        return _frame_result["result"]

    def get_fuel_bar(ship, length):
        _fuel_result = {}
        _fuel_args = [
            ship["fuel"]["current"],
            ship["fuel"]["capacity"],
            length
        ] # Args for format_bar.py: [current, capacity, length]
        execute("../scripts/format_bar.py", client, _fuel_args, _fuel_result)
        return _fuel_result["result"]

    def get_cargo_bar(ship, length):
        _cargo_result = {}
        _cargo_args = [
            ship["cargo"]["units"],
            ship["cargo"]["capacity"],
            length
        ] # Args for format_bar.py: [current, capacity, length]
        execute("../scripts/format_bar.py", client, _cargo_args, _cargo_result)
        return _cargo_result["result"]

    def get_crew_bar(ship, length):
        _crew_result = {}
        _crew_args = [
            ship["crew"]["current"],
            ship["crew"]["capacity"],
            length
        ] # Args for format_bar.py: [current, capacity, length]
        execute("../scripts/format_bar.py", client, _crew_args, _crew_result)
        return _crew_result["result"]

    def get_morale_bar(ship, length):
        _morale_result = {}
        _morale_args = [
            ship["crew"]["morale"],
            100,
            length
        ] # Args for format_bar.py: [current, capacity, length]
        execute("../scripts/format_bar.py", client, _morale_args, _morale_result)
        return _morale_result["result"]

    # TODO: test this with ship that has cargo
    def format_inventory_list(ship):
        _inventory_list = ""
        for item in ship["cargo"]["inventory"]:
            _inventory_list += "> x{0} {1}: {2}\n\t    ".format(
                item["units"],
                item["name"],
                item["description"]
            )
        return _inventory_list

    def colorize(string, color):
        return color + string + Style.RESET_ALL

    def color_header(string, foreground_color, background_color=Back.LIGHTBLACK_EX):
        # do not use colorize
        return foreground_color + background_color + string + Style.RESET_ALL
    
    def get_reactor_bar(ship, length):
        _reactor_result = {}
        _reactor_args = [
            ship["reactor"]["condition"],
            100,
            length
        ]
        execute("../scripts/format_bar.py", client, _reactor_args, _reactor_result)
        return _reactor_result["result"]
    
    def get_engine_bar(ship, length):
        _engine_result = {}
        _engine_args = [
            ship["engine"]["condition"],
            100,
            length
        ]
        execute("../scripts/format_bar.py", client, _engine_args, _engine_result)
        return _engine_result["result"]
    
    # list items must be tabbed in one level
    def format_module_list(ship):
        _module_list = ""
        for module in ship["modules"]:
            has_capacity = True if "capacity" in module.keys() else False
            has_range = True if "range" in module.keys() else False
            capacity_string = " [{0} CAPACITY]".format(module["capacity"]) if has_capacity else ""
            range_string = " [{0} RANGE]".format(module["range"]) if has_range else ""
            _module_list += "> {0}: {1}{2}{3}\n\t    ".format(
                colorize(module["name"], Fore.WHITE),
                module["description"],
                colorize(capacity_string, Fore.YELLOW),
                colorize(range_string, Fore.YELLOW)
            )
        return _module_list
    
    def format_mount_list(ship):
        _mount_list = ""
        for mount in ship["mounts"]:
            has_deposits = True if "deposits" in mount.keys() else False
            has_strength = True if "strength" in mount.keys() else False
            deposits_string = str(mount["deposits"]) if has_deposits else ""
            strength_string = " [{0} STRENGTH]".format(mount["strength"]) if has_strength else ""
            _mount_list += "> {0}: {1}{2}{3}\n\t    ".format(
                colorize(mount["name"], Fore.WHITE),
                mount["description"],
                colorize(deposits_string, Fore.YELLOW),
                colorize(strength_string, Fore.YELLOW)
            )
        return _mount_list

    # END FUNCTION DEFINITIONS
    
    try:
        if args == []:
            raise Exception("No arguments provided")
        ship = unwrap(client.fleet.get_my_ship(args[0])) # Get the ship with the given id
        STATUS_VERBS = {
            "IN_TRANSIT":"In transit from",
            "IN_ORBIT":"Orbiting",
            "DOCKED":"Docked at",
            "DRIFT":"Drifting from",
            "STEALTH":"Stealth cruising from",
            "CRUISE":"Crusing from",
            "BURN":"Burning from"
        }
        # Get the ship's status
        flight_verb = ""
        ship_status = ship["nav"]["status"]
        if ship_status == "IN_TRANSIT":
            flight_verb = STATUS_VERBS[
                ship["nav"]["flightMode"]
            ]
        else: # If ship isnt in transit
            flight_verb = STATUS_VERBS[ship_status]

        result = '''
        {name} {faction} {role}

        {ROUTE_HEADER}
            > {flight_verb} {depart_type} {departure} TO {destination_type} {destination}
            > {departure_time} -> {arrival_time} ({time_remaining})
            > {FUEL_SUBHEADER} {fuel_bar}

        {CARGO_HEADER} {cargo_bar}
            {inventory_list}
        {CREW_HEADER} {crew_bar}
            > {MORALE_SUBHEADER} {rotation} {morale_bar}
            > {WAGE_SUBHEADER} {wage} PER CREWMEMBER [{wage_total} total]

        {FRAME_HEADER} {frame_name}
            {frame_description}
            > {CONDITION_SUBHEADER} {frame_bar}
        
        {REACTOR_HEADER} {reactor_name}
            {reactor_description}
            > {REACTOR_CONDITION_SUBHEADER} {reactor_bar}
            > {REACTOR_OUTPUT_SUBHEADER} {reactor_output}

        {ENGINE_HEADER} {engine_name}
            {engine_description}
            > {ENGINE_CONDITION_SUBHEADER} {engine_bar}
            > {ENGINE_SPEED_SUBHEADER} {engine_speed}

        {MODULES_HEADER} {modules_filled}
            {module_list}

        {MOUNTS_HEADER} {mounts_filled}
            {mount_list}
        '''.format(
            # TITLE
            name=color_header(ship["symbol"], Fore.WHITE),
            faction=colorize(ship["registration"]["factionSymbol"], Fore.WHITE),
            role=colorize(ship["registration"]["role"], Fore.WHITE),
            # HEADERS
            ROUTE_HEADER=color_header("<:: ROUTE ::>", Fore.LIGHTGREEN_EX),
            CARGO_HEADER=color_header("<:: CARGO ::>", Fore.LIGHTYELLOW_EX),
            CREW_HEADER=color_header("<:: CREW ::>", Fore.WHITE),
            FRAME_HEADER=color_header("<:: FRAME ::>", Fore.LIGHTGREEN_EX),
            REACTOR_HEADER=color_header("<:: REACTOR ::>", Fore.LIGHTYELLOW_EX),
            ENGINE_HEADER=color_header("<:: ENGINE ::>", Fore.RED),
            MODULES_HEADER=color_header("<:: MODULES ::>", Fore.LIGHTGREEN_EX),
            MOUNTS_HEADER=color_header("<:: MOUNTS ::>", Fore.LIGHTYELLOW_EX),
            # SUBHEADERS
            FUEL_SUBHEADER=color_header("FUEL:", Fore.RED),
            MORALE_SUBHEADER=color_header("MORALE:", Fore.WHITE),
            WAGE_SUBHEADER=color_header("WAGE:", Fore.WHITE),
            CONDITION_SUBHEADER=color_header("CONDITION:", Fore.LIGHTGREEN_EX),
            REACTOR_CONDITION_SUBHEADER=color_header("CONDITION:", Fore.LIGHTYELLOW_EX),
            REACTOR_OUTPUT_SUBHEADER=color_header("OUTPUT:", Fore.LIGHTYELLOW_EX),
            ENGINE_CONDITION_SUBHEADER=color_header("CONDITION:", Fore.RED),
            ENGINE_SPEED_SUBHEADER=color_header("SPEED:", Fore.RED),
            # ROUTE
            flight_verb=flight_verb,
            depart_type=colorize(ship["nav"]["route"]["departure"]["type"], Fore.WHITE),
            departure=colorize(ship["nav"]["route"]["departure"]["symbol"], Fore.WHITE),
            destination_type=colorize(ship["nav"]["route"]["destination"]["type"], Fore.WHITE),
            destination=colorize(ship["nav"]["route"]["destination"]["symbol"], Fore.WHITE),
            fuel_bar=get_fuel_bar(ship, 30),
            departure_time = ship["nav"]["route"]["departureTime"],
            arrival_time=ship["nav"]["route"]["arrival"],
            time_remaining="todo",
            # CARGO
            cargo_bar=colorize(get_cargo_bar(ship, 30), Fore.LIGHTYELLOW_EX),
            inventory_list=format_inventory_list(ship),
            # CREW
            crew_bar=colorize(get_crew_bar(ship, 30), Fore.WHITE),
            rotation=ship["crew"]["rotation"],
            morale_bar=get_morale_bar(ship, 20),
            wage=ship["crew"]["wages"],
            wage_total=ship["crew"]["wages"] * ship["crew"]["current"],
            # FRAME
            frame_name=colorize(ship["frame"]["name"].split(" ")[1].upper(), Fore.WHITE),
            frame_description=ship["frame"]["description"],
            frame_bar=get_frame_bar(ship, 20),
            # REACTOR
            reactor_name=colorize(ship["reactor"]["name"].replace("_", " ").upper(), Fore.WHITE),
            reactor_description=ship["reactor"]["description"],
            reactor_bar=get_reactor_bar(ship, 20),
            reactor_output=ship["reactor"]["powerOutput"],
            # ENGINE
            engine_name=colorize(ship["engine"]["name"].replace("_", " ").upper(), Fore.WHITE),
            engine_description=ship["engine"]["description"],
            engine_bar=get_engine_bar(ship, 20),
            engine_speed=ship["engine"]["speed"],
            # MODULES
            modules_filled=colorize("[{}/{} Slots]".format(len(ship["modules"]), ship["frame"]["moduleSlots"]), Fore.LIGHTGREEN_EX),
            module_list=format_module_list(ship),
            # MOUNTS
            mounts_filled=colorize("[{}/{} Slots]".format(len(ship["mounts"]), ship["frame"]["mountingPoints"]), Fore.LIGHTYELLOW_EX),
            mount_list=format_mount_list(ship)
        )
        print(result)
    except ResponseException as e:
        raise e
    
main()
# We set result to None so it wont print when ran from CLI
result = None