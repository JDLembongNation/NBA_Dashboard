## This is responsible for the Player Return
import requests

def createPlayerData(): 
    with open("data/player_data.json") as d: 
        file = d.read()

def fetchPlayerData(playerID): 
    
    return True

#https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=01%2F12%2F2020&DateTo=01%2F12%2F2020&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=Totals&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2018-19&SeasonSegment=&SeasonType=Playoffs&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision=&Weight=
