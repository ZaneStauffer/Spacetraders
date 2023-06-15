from spacetraders import AuthenticatedClient
from spacetraders.models import GetMyAgentResponse200, GetMyShipsResponse200
from spacetraders.types import Response

import sys
import os
import json
from dotenv import load_dotenv

import executor
import logger
from cli import Session

def main():
    logger.log("INITIALIZING NEUROMORPHIC CORE...")
    # temp token lol (add to config file later))
    logger.log("Instantiating Seraph translation virtue...")
    logger.log("ARCHANGEL.RAZIEL: Greetings, user. I am now instatiating the client credentials.")
    # if .env file is not found, create it
    if not os.path.isfile(".env"):
        logger.log("ARCHANGEL.RAZIEL: No .env file found. Creating one now...", should_save=True)
        _usr_token = input("ARCHANGEL.RAZIEL: Please enter your spacetraders API token: ")
        # check if token is valid
        client = AuthenticatedClient(base_url="https://api.spacetraders.io/v2", token=_usr_token)
        
        if client.agents.get_my_agent().status_code != 200: # If token is invalid
            logger.log("ARCHANGEL.RAZIEL: Invalid token. Please try again.")
            sys.exit(1)
        
        try:
            ENV_PATH = os.path.join(os.path.dirname(__file__), ".env")
            with open(ENV_PATH, "w") as f: # create .env file
                f.write("TOKEN="+_usr_token)
                logger.log("ARCHANGEL.RAZIEL: I have created the .env file.", should_save=True)
        except Exception as e: # If token is invalid
            logger.log("ARCHANGEL.RAZIEL: Invalid token. Please try again.")
            sys.exit(1)
    
    load_dotenv()
    client = AuthenticatedClient(base_url="https://api.spacetraders.io/v2", token=os.getenv("TOKEN"))
    
    # get agent data
    response: Response[GetMyAgentResponse200] = client.agents.get_my_agent()
    # dict
    _res_dict = json.loads(response.content)
    _ships_dict = json.loads(client.fleet.get_my_ships().content)["data"]
    _names_list = list()
    for d in _ships_dict:
        for key, value in d.items():
            if key == "symbol":
                # value is the ship symbol
                _names_list.append(value)

    logger.log(
        """ARCHANGEL.RAZIEL: Your client credentials have been instantiated. Here is your data summary:

        Symbol: {0}
        Credits: {1}
        Faction: {2}
        Headquarters: {3}
        Ships: 
            {4}
        """.format(
            _res_dict["data"]["symbol"],
            _res_dict["data"]["credits"],
            _res_dict["data"]["startingFaction"],
            _res_dict["data"]["headquarters"],
            str(_names_list) if len(_names_list) > 0 else "No ships in fleet."
            ),
        should_save=True
    )

    usr_session = Session(client)
    usr_session.start()

if __name__ == "__main__":
    main()

