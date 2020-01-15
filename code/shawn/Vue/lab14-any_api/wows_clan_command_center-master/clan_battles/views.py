from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from .models import Battle, ClanInstance, PlayerInstance
from data.models import Clan, Ship, Player
import requests
import json

# main CB dashboard
class DashboardView(TemplateView):
    template_name = "dashboard.html"

# get last 50 alpha and bravo battles
def get_battles(request, realm):

    # resolve realm
    if realm == 'NA':
        realm_url = 'com'
    elif realm == 'EU':
        realm_url = 'eu'
    elif realm == 'SEA':
        realm_url = 'asia'
    elif realm == 'RU':
        realm_url = 'ru'

    # commenting this out until season begins, unable to test between seasons
    # payload = {
    #     'team': 1,
    # }
    # response = requests.get(f"https://clans.worldofwarships.{realm_url}/clans/wows/ladder/api/battles/", params=payload)
    # page_query = json.loads(response.text)

    with open('clan_battles/sample_data.json', 'r', encoding='utf-8') as json_file:
        page_query = json.load(json_file)    
    
    print("loaded battle json:")

    # counters to track what's added to db
    battle_added_to_db_counter = 0
    claninstance_added_to_db_counter = 0
    playerinstance_added_to_db_counter = 0

    # battles, clans, and players will be added to db using nested for loops
    for battle in page_query:
        # create Battle object
        b, battle_was_created = Battle.objects.get_or_create(
            battle_wgid = battle['id'],
            battle_map = battle['map']['name'],
            battle_realm = battle['realm'],
            battle_arena_id = battle['arena_id'],
            battle_finished_at = battle['finished_at'],
            battle_season_number = battle['season_number'],
        )
        if battle_was_created:
            battle_added_to_db_counter += 1

            # create ClanInstance objects, only if battle was created
            for team in battle['teams']:
                c, claninstance_was_created = ClanInstance.objects.get_or_create(
                    claninstance_wgid = team['id'],
                    claninstance_clan = Clan.objects.get_or_create(
                        clan_wgid=team['clan_id'],
                        clan_realm=realm
                        )[0],
                    claninstance_battle = b,
                    claninstance_team_no = battle['teams'].index(team),
                    claninstance_division = team['division'],
                    claninstance_league = team['league'],
                    claninstance_rating_delta = team['rating_delta'],
                    claninstance_result = team['result'],
                    claninstance_rating = team['team_number'],
                )
                if claninstance_was_created:
                    claninstance_added_to_db_counter += 1

                    try: 
                        # create PlayerInstance objects, only if ClanInstance was created
                        for player in team['players']:
                            p, playerinstance_was_created = PlayerInstance.objects.get_or_create(
                                playerinstance_wgid = player['spa_id'],
                                playerinstance_player = Player.objects.get_or_create(player_wgid=player['spa_id'])[0],
                                playerinstance_player_name = player['nickname'],
                                playerinstance_ship = Ship.objects.get(ship_wgid=player['vehicle_id']),
                                playerinstance_claninstance = c,
                                playerinstance_clan = Clan.objects.get(clan_wgid=player['clan_id']),
                                playerinstance_survived = player['survived'],
                            )
                            if playerinstance_was_created:
                                playerinstance_added_to_db_counter += 1
                    except Ship.DoesNotExist:
                        print("Ship not found, please update game data!")
        
        else:
            print(f"Battle not added to db.  Battle id: {b.battle_wgid}")


    # verify clan battle load was successful
    print(f"*** Results of clan battles pull: *** ")
    print(f"*** Clan: {request.user.player.player_clan.clan_tag}                     *** ")
    print(f"*** Battles pulled: {len(page_query)}            *** ")
    print(f"*** Battles added to db: {battle_added_to_db_counter}  *** ")
    print(f"*** ClanInstances added to db: {claninstance_added_to_db_counter}  *** ")
    print(f"*** PlayerInstance added to db: {playerinstance_added_to_db_counter}  *** ")

    return HttpResponseRedirect(reverse('clan_battles:dashboard'))