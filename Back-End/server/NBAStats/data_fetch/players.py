## This is responsible for the Player Return
import json
import os
import time


def createPlayerData(): 
    pass
    
def getPlayerData(PlayerID):
    content = getAllData()
    playerList = content["data"]
    for x in range(len(playerList)): 
        if int(playerList[x]["PLAYER_ID"]) == PlayerID:
            print(playerList[x])
            data = json.dumps(playerList[x])
            return data

def getAllData(): 
    json_file = open('./NBAStats/data_fetch/data/player_data.json')
    json_string = json_file.read()
    json_data = json.loads(json_string)
    json_file.close()
    return json_data

def updatePlayerData(playerList): 
    with open("./NBAStats/data_fetch/data/player_data.json", "w+") as player_data:
        if os.stat("./NBAStats/data_fetch/data/player_data.json").st_size == 0:
            dataObject = {}
            dataObject["timeUpdated"] = int(time.time())
            dataObject["data"] = playerList
            json.dump(dataObject, player_data)
        else:
            data = json.loads("./NBAStats/data_fetch/data/player_data.json")
            previousTime = int(data["timeUpdated"])
            currentTime = int(time.time())
            if (currentTime-previousTime) > (24*3600):
            #24 hours is enough to update the status of each player.
            #TODO: Check the schedule of the league and update accordingly. 
                dataObject = {}
                dataObject["timeUpdated"] = currentTime   
                dataObject["data"] = playerList 
                json.dump(dataObject, player_data) 

#https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=01%2F12%2F2020&DateTo=01%2F12%2F2020&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=Totals&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2018-19&SeasonSegment=&SeasonType=Playoffs&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision=&Weight=

