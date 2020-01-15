import requests
from . import urlBuild


def getLeagueData(MeasureType="base", PerMode=None, Season="2019-20"):
    URL = urlBuild.buildURL("league")
    print(URL)
    response = requests.get(URL)
    return response.text

