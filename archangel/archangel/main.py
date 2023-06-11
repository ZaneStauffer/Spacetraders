from spacetraders import AuthenticatedClient
from spacetraders.models import GetMyAgentResponse200, GetMyShipsResponse200
from spacetraders.types import Response

import sys
import os
import json
from pprint import pprint

import executor
import logger
from cli import Session

def main():
    logger.log("INITIALIZING NEUROMORPHIC CORE...")
    # temp token lol (add to config file later)
    TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGlmaWVyIjoiQVJDSEFOR0VMLTAxIiwidmVyc2lvbiI6InYyIiwicmVzZXRfZGF0ZSI6IjIwMjMtMDYtMTAiLCJpYXQiOjE2ODY0MzI2MTYsInN1YiI6ImFnZW50LXRva2VuIn0.pyNY00OyI7d75u75w3JUUJxuVip9BCWYX8My-lVodkdSVS0gbGUgB6ZkBIRtyDtVWolArUIhksz-pWDZHZ-8nOybA9GfMi_KtVeO58yPUVlMqfWUhqw5IkZ67jG39PE1RmDy6_W39GUN0ejPveTH5L_sjXavIQmR5SrzU4XQOuV2bAWzYQHbS-jNX86AVCa5NDBe69aorZV9n77P8J2FHdDALBwjETGIInl5okLkY5-1cfp7gaS3XkkamPmfxvT7kkxy3st4hc9mcWm3St8O6xES2k4YoIHO100Y5QsnrhMAf9KV99V0I3xUoRU6exYT_YolsopbnEMxXwI0-uFJ4g"
    logger.log("Instantiating Seraph translation virtue...")
    logger.log("ARCHANGEL.RAZIEL: Greetings, user. I am now instatiating the client credentials.")
    client = AuthenticatedClient(base_url="https://api.spacetraders.io/v2", token=TOKEN)
    
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

    
    # try:
    #     if(len(sys.argv) > 1): # If file path is provided, execute it
    #         script_path = "../scripts/" + sys.argv[1]
    #         executor.execute(script_path, client)
    #     else:
    #         # Open CLI if no file path is provided
    #         while True:
    #             try:
    #                 script_path = "../scripts/" + input("[SCRIPT]> ")
    #                 executor.execute(script_path, client) # Prompt user for script path
    #             except OSError as e:
    #                 logger.log("ARCHANGEL.RAZIEL: {0}".format(str(e)), should_save=True)
    # except Exception as e:
    #     logger.log("ARCHANGEL.RAZIEL: {0}".format(str(e)), should_save=True)
    #     exit(1)

if __name__ == "__main__":
    # TODO: pass client to executor and use it in the script
    main()

