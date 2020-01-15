from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from .config import api_key
from .models import Upgrade, Ship, Skill, Clan, Player
from data.models import ShipInstance
import requests
import json

# Create your views here.
def update_game_data(request, realm):
    print("Updating game data...")

    # resolve realm
    if realm == 'NA':
        realm_url = 'com'
    elif realm == 'EU':
        realm_url = 'eu'
    elif realm == 'SEA':
        realm_url = 'asia'

    update_ships(realm_url)
    update_skills(realm_url)
    update_clans()

    return HttpResponseRedirect(reverse('clan_battles:dashboard'))
    
class SettingsView(TemplateView):
    template_name = 'settings.html'


# functions for updating different parts of the game
def update_ships(realm_url):
    # ------------------ get all ship data:-----------------------
    ship_data = {}
    # API will return status of "error" when you request an empty page and "ok" otherwise.  Use status as flag for while loop
    status = "ok"
    page_num = 1
    # loop until invalid page is requested
    while status == "ok":
        payload = {
            'application_id': api_key,
            'fields': 'name,type,tier,nation,upgrades,mod_slots',
            'page_no': page_num
        }
        response = requests.get(f"https://api.worldofwarships.{realm_url}/wows/encyclopedia/ships/", params=payload)
        page_query = json.loads(response.text)

        # add each ship to master ship data dictionary
        if page_query['status'] == "ok":
            for ship in page_query['data']:
                ship_data[ship] = page_query['data'][ship] 

        # update loop variables
        page_num += 1
        status = page_query['status']

    # MAKE THIS SO IT UPDATES SHIP DATA INSTEAD OF CREATING NEW SHIPS

    # add ships to DB
    added_to_db_counter = 0
    for ship in ship_data:
        s, was_created = Ship.objects.get_or_create(
            ship_wgid=ship,
            ship_tier=ship_data[ship]['tier']
        )
        s.ship_name=ship_data[ship]['name']
        s.ship_class=ship_data[ship]['type']
        s.ship_nation=ship_data[ship]['nation']
        s.ship_upgrade_slots=ship_data[ship]['mod_slots']
        # function for updating ship upgrades
        s.save()

        if was_created:
            added_to_db_counter += 1

    # verify ship load was successful
    print(f'{len(ship_data)} ships loaded from WG API, {page_num-1} pages.  {added_to_db_counter} new DB additions')

def update_skills(realm_url):
    # ------------------ get all skill data:-----------------------
    payload = {
        'application_id': api_key,
        'fields': 'name,tier,icon',
    }
    response = requests.get(f"https://api.worldofwarships.{realm_url}/wows/encyclopedia/crewskills/", params=payload)
    page_query = json.loads(response.text)

    # add skills to DB
    added_to_db_counter = 0
    for skill in page_query['data']:
        s, was_created = Skill.objects.get_or_create(
            skill_wgid=skill,
        )
        s.skill_name=page_query['data'][skill]['name']
        s.skill_tier=page_query['data'][skill]['tier']
        s.skill_picture_url=page_query['data'][skill]['icon']
        s.save()

        if was_created:
            added_to_db_counter += 1

    # verify skill load was successful
    print(f'{len(page_query["data"])} skills loaded from WG API, {added_to_db_counter} new DB additions')

# update clan information for clans in DB 
def update_clans():
    
    # get all clans in db (these are loaded from when users are created or from CB results)
    clan_list_queryset = Clan.objects.values_list('clan_wgid')

    # convert to list of strings (instead of list of typle querysets)
    clan_list = []
    for clan in clan_list_queryset:
        clan_list.append(str(clan[0]))

    # query clans on each realm, passing the leftovers the next region
    non_updated_clans = update_clan_list_with_realm(clan_list, 'com')
    non_updated_clans = update_clan_list_with_realm(non_updated_clans, 'eu')
    non_updated_clans = update_clan_list_with_realm(non_updated_clans, 'ru')
    non_updated_clans = update_clan_list_with_realm(non_updated_clans, 'asia')
    print(f'Could not update clans: {non_updated_clans}')

    # status message
    print(f"{len(clan_list_queryset)-len(non_updated_clans)} clans updated.  {len(non_updated_clans)} not found")

def update_clan_list_with_realm(clan_list, realm_url):

    # return if input clan list is empty
    if not clan_list:
        return []

    # create payloads.  API can take up to 100 clan IDs at once
    payload_list = []
    payload_string = ''
    i = len(clan_list) - 1
    count = 0
    while i >= 0:
        count += 1
        payload_string += f'{clan_list[i]},'
        if count % 100 == 0:
            payload_list.append(payload_string)
            payload_string = ''
        i -= 1

    # payload_list is a list of up to 100 clan ids in each string
    payload_list.append(payload_string)

    # make API call for each list of <=100 clans
    non_realm_clans = []
    for payload_string in payload_list: 
        print(f"payload_string {payload_string}")
        payload = {
            'application_id': api_key,
            'clan_id': payload_string,
        }
        response = requests.get(f"https://api.worldofwarships.{realm_url}/wows/clans/info/", params=payload)
        page_query = json.loads(response.text)

        # loop through all clans
        try: 
            for clan in page_query['data']:
                # clans in the region will be not null
                if page_query['data'][clan]:
                    c, was_created = Clan.objects.get_or_create(clan_wgid=page_query['data'][clan]['clan_id'], clan_realm='NA')
                    c.clan_name = page_query['data'][clan]['name']
                    c.clan_tag = page_query['data'][clan]['tag']
                    c.clan_members_count = page_query['data'][clan]['members_count']
                    c.clan_is_disbanded = page_query['data'][clan]['is_clan_disbanded']
                    c.save()
                # clans not in region will be null
                else:
                    print(f"non-realm clan: {clan}")
                    non_realm_clans.append(clan)
        except: 
            return clan_list

    print(f'returning from checking {realm_url} clans.  Non_realm_clans is {non_realm_clans}')
    return non_realm_clans

# For updating the signed in user's Clan (and clan's Player, including their ships) info
def update_user_clan(request, realm):
    # status message
    print(f"Updating {request.user.username}'s clan information...'")

    # resolve realm
    if realm == 'NA':
        realm_url = 'com'
    elif realm == 'EU':
        realm_url = 'eu'
    elif realm == 'SEA':
        realm_url = 'asia'

    # ------------------ create players for logged in user's clan:-----------------------
    # get all players in user's clan
    players_clan = request.user.player.player_clan.clan_wgid
    payload = {
        'application_id': api_key,
        'clan_id': players_clan,
        'fields': 'members_ids',
    }
    response = requests.get(f"https://api.worldofwarships.{realm_url}/wows/clans/info/", params=payload)
    page_query = json.loads(response.text)
    player_list = page_query['data'][str(players_clan)]['members_ids']
    
    #status message
    print(f"Total players in {request.user.player.player_clan.clan_tag}: {len(player_list)}")
    
    # turn player_list into a payload
    player_list_payload = ''
    for player in player_list:
        player_list_payload += f'{player},'

    # get clan details for all players, mainly their roles.  all of the clan's players will be sent at once in the payload
    payload = {
        'application_id': api_key,
        'account_id': player_list_payload,
    }
    response = requests.get(f"https://api.worldofwarships.{realm_url}/wows/clans/accountinfo/", params=payload)
    page_query = json.loads(response.text)

    # for each player, create a Player object (if it doesn't already exist).  Update all Players, either way. 
    player_count = 0
    count_added_to_db = 0
    invalid_ship_list = []
    for player in page_query['data']:
        player_count += 1
        p, was_created = Player.objects.get_or_create(player_wgid = int(player))
        invalid_ship_list += update_player_info(player_count, realm_url, p, players_clan, page_query['data'][player])
        
        if was_created:
            count_added_to_db += 1

    # status message
    print(f"Players added to db: {count_added_to_db}")
    print("Completed updating user's clan information")
    print(f"The following ships not found in encyclopedia: {list(dict.fromkeys(invalid_ship_list))}")

    return HttpResponseRedirect(reverse('clan:dashboard'))

def update_player_info(player_count, realm_url, p, players_clan, player):
   
    # player object p is passed in
    p.player_clan = Clan.objects.get(clan_wgid=players_clan)
    p.player_nickname = player['account_name']
    p.player_clan_role = player['role']
    p.player_joined_at = player['joined_at']

    # update ships
    payload = {
        'application_id': api_key,
        'account_id': p.player_wgid,
    }
    response = requests.get(f"https://api.worldofwarships.{realm_url}/wows/ships/stats/", params=payload)
    page_query = json.loads(response.text)

    added_to_db_counter = 0
    ship_list = page_query['data'][str(p.player_wgid)]
    invalid_ship_list = []
    for ship in ship_list:
        try:
            s, was_created = ShipInstance.objects.get_or_create(
                shipinstance_player = p,
                shipinstance_ship = Ship.objects.get(ship_wgid=ship['ship_id'])
                )
            update_ship_stats(realm_url, s, ship)
            p.player_ships.add(s.shipinstance_ship)
            if was_created:
                added_to_db_counter += 1
        except Ship.DoesNotExist:
            invalid_ship_list.append(ship['ship_id'])


    print(f"{player_count}. Finished loading player ships. Player {p.player_wgid} has {len(page_query['data'][str(p.player_wgid)])} ships. {added_to_db_counter} are new and were added to db.")
    p.save()
    return invalid_ship_list

# this function will update all ship stats for a given player, except for CB battles/wins/losses
def update_ship_stats(realm_url, s, ship):

    s.shipinstance_main_battery_hits = ship['pvp']['main_battery']['hits']
    s.shipinstance_main_battery_shots = ship['pvp']['main_battery']['shots']
    s.shipinstance_xp = ship['pvp']['xp']
    s.shipinstance_battles = ship['pvp']['battles']
    s.shipinstance_torpedoes_hits = ship['pvp']['torpedoes']['hits']
    s.shipinstance_torpedoes_shots = ship['pvp']['torpedoes']['shots']
    s.shipinstance_wins = ship['pvp']['wins']
    s.shipinstance_losses = ship['pvp']['losses']
    s.shipinstance_damage_dealt = ship['pvp']['damage_dealt']
    s.shipinstance_potential_damage = ship['pvp']['max_total_agro']
    s.shipinstance_spotting_damage = ship['pvp']['damage_scouting']
    s.save()