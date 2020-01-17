from django.urls import path 

from . import views 

urlpatterns = [
    path('league-info',views.leagueData, name='leagueData')
]
