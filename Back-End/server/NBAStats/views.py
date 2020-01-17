from django.shortcuts import render
from django.http import HttpResponse
import json
from .data_fetch import players
from .data_fetch import league 
from .data_fetch import teams

# Create your views here.

def leagueData(request): 
    return HttpResponse(league.getLeagueData(), content_type="application/json")

def playerData(request, playerID): 
    return HttpResponse(players.getPlayerData(playerID), content_type="application/json")

def recentScoreData(request, day, month, year):
    return HttpResponse(teams.getRecentGames(day, month, year), content_type="application/json")

