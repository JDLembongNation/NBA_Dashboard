import json 
import os 
import requests
from . import urlBuild

def getStandings(): 
    pass

def getTeamHistory(): 
    pass

def getTeamVSHistory(): 
    pass

def getRecentGames(day, month, year): 
    URL = urlBuild.buildGamesURL(day, month, year)
    print(URL)
    response = requests.get(URL)
    #Add to GameData here. 
    print(response)
    return response
