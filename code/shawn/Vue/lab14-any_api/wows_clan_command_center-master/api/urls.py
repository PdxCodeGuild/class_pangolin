from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('players', views.PlayerViewSet, basename='players')
router.register('ships', views.ShipsViewset, basename='ships') 
router.register('user_clan_roster', views.UserClanRosterViewset, basename='user-clan-roster') 
router.register('user_ships', views.UserShipsViewset, basename='user-ships') 

urlpatterns = router.urls
