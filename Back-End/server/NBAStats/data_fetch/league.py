import requests
import json
from . import urlBuild
from . import players


def getLeagueData(MeasureType="base", PerMode=None, Season="2019-20"):
    URL = urlBuild.buildURL("league")
    print(URL)
    response = requests.get(URL)
    #Change below condition to every 24 hours.
    if(True):
        processPlayerInformation(response.text)
    return response.text
 
def processPlayerInformation(response): 
    playerList = []
    responseObject = json.loads(response) 
    for player in range(len(responseObject.get("resultSets")[0].get("rowSet"))):
        data = '{"'
        for attribute in range(len(responseObject.get("resultSets")[0].get("headers"))):
            data+=responseObject.get("resultSets")[0].get("headers")[attribute]
            data+='":"'
            data+=str(responseObject.get("resultSets")[0].get("rowSet")[player][attribute])
            data+='",'
        data+='}'
        playerList.append(data)
    print(len(playerList))
    players.updatePlayerData(playerList)
    
 