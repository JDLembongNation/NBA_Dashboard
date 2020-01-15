## This is responsible for the Player Return
import json

def createPlayerData(): 
    pass
        # with open("data/player_data.json") as d: 
        #     file = d.read()

def updatePlayerData(playerList): 
    with open("./NBAStats/data_fetch/data/player_data.json", "w") as player_data:
        dataObject = {}
        dataObject["data"] = playerList
        json.dump(dataObject, player_data)

#https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=01%2F12%2F2020&DateTo=01%2F12%2F2020&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=Totals&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2018-19&SeasonSegment=&SeasonType=Playoffs&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision=&Weight=

