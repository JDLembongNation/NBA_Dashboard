from django.shortcuts import render
from django.http import HttpResponse
import json
from .data_fetch import players
from .data_fetch import league 

# Create your views here.

def index(request): 
    return HttpResponse(league.getLeagueData(), content_type="application/json")

