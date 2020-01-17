from django.urls import path 

from . import views 

urlpatterns = [
    path('league-info',views.leagueData, name='leagueData'),
    path('player-info/<int:playerID>',views.playerData, name='playerData')
]
