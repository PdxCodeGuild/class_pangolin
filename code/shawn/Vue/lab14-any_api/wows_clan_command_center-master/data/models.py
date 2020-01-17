from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Upgrade: for each upgrade slot in the game
class Upgrade(models.Model):

    # upgrade identifiers
    upgrade_wgid = models.IntegerField()
    upgrade_name = models.CharField(max_length=50)
    
    # store when upgrade added to database (in case it needs to be deleted later)
    date_created = models.DateTimeField(auto_now_add=True)

# Ship: data for each ship in the game
class Ship(models.Model):

    # ship identifiers
    ship_wgid = models.IntegerField()
    ship_name = models.CharField(max_length=50, null=True)

    # ship characteristics
    ship_class = models.CharField(max_length=2, null=True)     # options: CV, BB, CA, DD, SS
    ship_tier = models.IntegerField()
    ship_nation = models.CharField(max_length=50, null=True)
    ship_upgrades = models.ManyToManyField(Upgrade, related_name="ship_upgrades")
    ship_upgrade_slots = models.IntegerField(null=True)

    # store when ship added to database (in case it needs to be deleted later)
    date_created = models.DateTimeField(auto_now_add=True)


# Skill: commander skills
class Skill(models.Model):

    # skill characteristics
    skill_wgid = models.IntegerField()
    skill_name = models.CharField(max_length=100, null=True)
    skill_tier = models.IntegerField(null=True)
    skill_picture_url = models.URLField(null=True)

    # store when skill added to database (in case it needs to be deleted later)
    date_created = models.DateTimeField(auto_now_add=True)

# Clan: one created for each clan in the game.
class Clan(models.Model):

    # identifier
    clan_wgid = models.IntegerField()               
    clan_tag = models.CharField(max_length = 10, null=True)    # e.g. "KSD"
    clan_name = models.CharField(max_length = 50, null=True)   # e.g. "Kill Steal Denied"

    # characteristics
    clan_members_count = models.IntegerField(null=True)
    clan_realm = models.CharField(max_length = 10)
    clan_is_disbanded = models.BooleanField(null=True)

    # store when skill added to database (in case it needs to be deleted later)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.clan_tag

# Player: a Player will be created for each player in each website user's clan
# This will be helpful for storing CB specific info (ship list, stats, etc) even if they 
# are not users of the site themselves
class Player(models.Model):

    # identifier
    player_wgid = models.IntegerField()
    player_nickname = models.CharField(max_length=50, null=True)
    player_user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

    # characteristics
    player_clan = models.ForeignKey(Clan, on_delete=models.SET_NULL, null=True, related_name="roster")
    player_ships = models.ManyToManyField(Ship)
    player_clan_role = models.CharField(max_length=20, null=True)
    player_joined_at = models.IntegerField(null=True)

    # store when skill added to database (in case it needs to be deleted later)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.player_nickname

# ShipInstance: a ship owned by a specific player (extends Ship to include stats)
class ShipInstance(models.Model):

    # identifiers
    shipinstance_ship = models.ForeignKey(Ship, on_delete=models.SET_NULL, null=True, related_name="player_fleet")
    shipinstance_player = models.ForeignKey(Player, on_delete=models.CASCADE)

    # characteristics
    shipinstance_main_battery_hits = models.IntegerField(null=True)
    shipinstance_main_battery_shots = models.IntegerField(null=True)
    shipinstance_xp = models.IntegerField(null=True)
    shipinstance_battles = models.IntegerField(null=True)
    shipinstance_torpedoes_hits = models.IntegerField(null=True)
    shipinstance_torpedoes_shots = models.IntegerField(null=True)
    shipinstance_wins = models.IntegerField(null=True)
    shipinstance_losses = models.IntegerField(null=True)
    shipinstance_damage_dealt = models.IntegerField(null=True)
    shipinstance_potential_damage = models.IntegerField(null=True)
    shipinstance_spotting_damage = models.IntegerField(null=True)
    shipinstance_cb_battles = models.IntegerField(default=0)
    shipinstance_cb_wins = models.IntegerField(default=0)
    shipinstance_cb_battles_survived = models.IntegerField(default=0)

    # for db maintainence
    date_created = models.DateTimeField(auto_now_add=True) 


# # create a Player whenever a User is created
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Player.objects.create(user=instance) 

# # save changes to Player whenever User is changed
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.player.save()