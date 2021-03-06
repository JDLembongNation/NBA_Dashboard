from datetime import date 
def buildURL(dataType, season="2018-19", conference=None, measureType="Base", perMode="Totals"):
    if(dataType == "player"): 
        print("Not completed yet")
    elif(dataType == "league"): 
        #Ignore Colleges for now
        URL = "https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference="
        if(conference is not None):
            URL+= conference
        #Again, ignore the following parameters for now. 
        URL+="&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType="
        URL+= measureType
        URL+="&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode="
        URL+=perMode
        URL+= "&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season="
        URL+=season
        URL+="&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision=&Weight="
        return URL

#Requires separate method since dealing with different provider than other get requests.
#https://stats.nba.com/stats/scoreboardV2?DayOffset=0&LeagueID=00&gameDate=01/15/2020
def buildGamesURL(day, month, year):
    URL = "https://stats.nba.com/stats/scoreboardV2?DayOffset=0&LeagueID=00&gameDate="
    URL+=str(month) + "/"
    URL+=str(day) + "/"
    URL+=str(year)
    return URL
    


