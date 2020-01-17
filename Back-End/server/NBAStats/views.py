from django.shortcuts import render
from django.http import HttpResponse
import json
from .data_fetch import players
from .data_fetch import league 

# Create your views here.

def leagueData(request): 
    return HttpResponse(league.getLeagueData(), content_type="application/json")

def playerData(request, playerID): 
    return HttpResponse(players.getPlayerData(playerID), content_type="application/json")

