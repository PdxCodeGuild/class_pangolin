from django.db import models
from data.models import Clan, Ship, Player
# from profiles.models import Profile


# Battle: a particular clan battle that was played
class Battle(models.Model):

    # identifiers
    battle_wgid = models.IntegerField()

    # characteristics
    battle_map = models.CharField(max_length=50)
    battle_realm = models.CharField(max_length=10)
    battle_arena_id = models.IntegerField()
    battle_finished_at = models.DateTimeField()
    battle_season_number = models.IntegerField()

    # date created (for potential future DB maintenance)
    date_created = models.DateTimeField(auto_now_add=True)

# A clan's participation in a clan battle
class ClanInstance(models.Model):

    # identifier
    claninstance_wgid = models.IntegerField()

    # characteristics 
    claninstance_clan = models.ForeignKey(Clan, on_delete=models.SET_NULL, null=True)      # if clan is deleted, keep the ClanInstance for data purposes
    claninstance_battle = models.ForeignKey(Battle, on_delete=models.SET_NULL, null=True)   # if battle is deleted, keep the ClanInstance for data purposes
    claninstance_team_no = models.IntegerField()        # two teams per clan battle, so this will be with 0 or 1.  team 0 will be player's (who first pulled the data) clan
    claninstance_division = models.IntegerField()       
    claninstance_league = models.IntegerField()
    claninstance_rating = models.IntegerField()         # 1 is alpha, 2 is bravo
    claninstance_rating_delta = models.IntegerField()
    claninstance_result = models.CharField(max_length=10)

    # date created (for potential future DB maintenance)
    date_created = models.DateTimeField(auto_now_add=True)

# A player's participation in a clan battle
class PlayerInstance(models.Model):

    # identifiers
    playerinstance_wgid = models.IntegerField()
    playerinstance_player_name = models.CharField(max_length=100)

    # characteristics
    playerinstance_player = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True)
    playerinstance_ship = models.ForeignKey(Ship, on_delete=models.SET_NULL, null=True)                 # if ship is deleted, keep this PlayerInstance for data purposes              
    playerinstance_claninstance = models.ForeignKey(ClanInstance, on_delete=models.SET_NULL, null=True) # if battle is deleted, delete the PlayerInstance
    playerinstance_clan = models.ForeignKey(Clan, on_delete=models.SET_NULL, null=True)              # if player's profile deleted, keep this PlayerInstance for data purposes              
    playerinstance_survived = models.BooleanField()
    
    # date created (for potential future DB maintenance)
    date_created = models.DateTimeField(auto_now_add=True)
