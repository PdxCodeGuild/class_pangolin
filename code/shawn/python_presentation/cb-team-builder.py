# Shawn Stolsig
# PDX Code Guild 
# Assignment: Python Section Presentation
# Date: 11/11/2019

# These imports required for Google Sheets API
from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Other imports

# =====================    CLASSES  ============================= #
class Clan:
    '''
    '   This class will hold all information related to a clan (mainly the roster and preferred ship lineup)
    '   Attributes: A roster of Player objects
    '   Methods:
    '           
    '
    '''

    def __init__(self, input_data):
        ''' the init function for a Roster type '''

        # pull header from file:
        self.header = input_data[1]

        # roster is list of Player objects
        self.roster = []

        # the desired ship lineup, as a list of strings
        self.target_ship_lineup = ['Kremlin', 'Yamato', 'Smolensk', 'Moskva', 'Des Moines', 'Kleber', 'Kleber', 'Gearing']
        self.master_target_ship_lineup = self.target_ship_lineup.copy()

        # try to retrieve all of the data from input file
        try:
            # iterate through rows after header, add Player objects to roster
            for i in range(2,len(input_data)):
                self.roster.append(Player(self.header,input_data[i])) 
        # handle any index errors
        except:
            print("Issue with input data, see Clan __init__ method")

    def get_player(self, name):
        '''
        '   A function for retrieving player object of given input username
        '   Parameters: WG username (string)        
        '   Returns: Player object
        '''
        for i in range(len(self.roster)):
            if self.roster[i].username_wg == name:
                return self.roster[i]

    def generate_lineup(self, player_list):
        '''
        '   This is the main algorithm for generating the best lineup.  One important note is that this algorithm
        '   is reliant on having a player list that is exactly as long as the target ship lineup
        '   Parameters: a list of player objects
        '   Returns: a Lineup object
        '''
        # total point constant.  the more points a player gets for a ship, the less likely to be slotted
        const_points = 100
        # modifiers per factor considered when slotting players into ships.  eventually, these should be user adjustable
        mod_has_ship = 0.3
        mod_admiral_preferred = 0.1
        mod_player_preferred = 0.1
        mod_is_alpha = 0.1
        mod_is_main_class = 0.5
        # (modifiers not yet used):
        mod_stat_PR = 1
        mod_stat_WR = 1
        mod_stat_AVG_DMG = 1
        mod_needs_wins = 1

        # two lists and a variable that will later be sent to create Linup object
        lineup_player_list = []
        lineup_ship_list = []
        lineup_score = 0

        #   Here's how the algorithm will work:
        #   1. We'll first figure out the order of rarity of the ships in the target lineup
        #   2. Then, we will get a list of strings of each ship name in the team composition, 
        #      with length equal to the number of ships in our target team composition, 
        #      ordered from most to least rare
        #   3. We'll iterate through this of ships, selecting a player for each ship
        #   4. For each ship, we will itereate through all players who have the ship available to play
        #   5. We'll give players "points" for each thing that we care about as we are building our team.
        #      Most heavily weighted will be availability of other in-composition ships that a player can use.  
        #      Then we will assign points for all of our other factors (are they an "alpha" player, are they 
        #      preferred by an admiral, do they have good stats in that ship, etc etc)
        #   6. Each player/point combo per ship will be appended to a list, which is then sorted by lowest to highest points
        #   7. The player for that ship with the least number of points is slotted to play that ship.  
        #   8. Both that player and the ship they were slotted into are removed from further consideration
        #   9. Algorithm loops, removing each player/ship slotting until all players have been slotted


        # iterate through target ship lineup list, rarest ship first
        for lineup_ship in self.get_ordered_rare_ship_list(player_list):

            # create an empty list for players who have this ship
            players_with_lineup_ship = []

            # iterate through list of players who have the ship
            for player in self.get_list_players_owning_ship(lineup_ship, player_list):
                print(f"lineup_ship is {lineup_ship} and player is {player}")                       ## debugging ##

                # initialize points for this player/ship combo
                points = 0

                # figure out how many other other ships in the lineup current player has
                ship_count = 0
                for ship in player.ships:
                    if ship in self.target_ship_lineup:
                        ship_count += 1
                # give player points for each ship he has
                points += ship_count * const_points * mod_has_ship

                # add points if they are not admiral preferred
                if not player.ships[lineup_ship]['admiral_preferred']:
                    points += const_points * mod_admiral_preferred
                    
                # add points if not alpha team
                if not player.is_alpha_team:
                    points += const_points * mod_is_alpha

                # add points if not player preferred
                if not player.ships[lineup_ship]['player_preferred']:
                    points += const_points * mod_player_preferred           

                # add points if player doesn't main that class
                # add points if they don't need wins
                # add points if they have bad ship stats

                # add player and points to a temporary list
                players_with_lineup_ship.append( [player.username_wg, points])

            # sort the player list by points, lowest comes first
            players_with_lineup_ship.sort(key=lambda x:x[1])        # this sorts based on the [1] index of nested elements         
            print(f"players/scores for {lineup_ship} are {players_with_lineup_ship}")       ## debugging ##

            # get the selected player for this combo (all we have now is their name)
            player_obj_selected = self.get_player(players_with_lineup_ship[0][0])

            # remove the Player from player_list with the lowest points
            player_list.remove(player_obj_selected)

            # remove ship from the copy of the target ship lineup
            self.target_ship_lineup.remove(lineup_ship)

            # add data to lineup lists/score.  these will be used to create the Lineup object later.
            lineup_player_list.append(player_obj_selected)
            lineup_ship_list.append(lineup_ship)
            lineup_score += players_with_lineup_ship[0][1]

        # reset target_ship_lineup so that it can be used again
        self.target_ship_lineup = self.master_target_ship_lineup.copy()

        # return new Lineup object
        return Lineup(lineup_player_list, lineup_ship_list, lineup_score)

    def get_dict_players_with_ships(self, player_list):
        '''
        '   This function will help figure out how "rare" each ship is, based on the input Players
        '   Parameters: list of Player objects, list of ships (as strings)
        '   Return: a dictionary of ship: number of players with ship 
        '''
        # declare empty return dictionary
        return_dict = {}

        # iterate through ships in target lineup:
        for ship in self.target_ship_lineup:
            # if ship is already in dictionary, skip
            if ship in return_dict.keys():
                pass
            # else if ship is not in dictionary
            else: 
                # init counter to 0
                counter = 0
                # iterate through players
                for player in player_list:
                    # check to see if player has that ship
                    if ship in player.ships.keys():
                        # increment counter if ship is there
                        counter += 1
                # add that ship to dictionary as a key with the number of players as the value
                return_dict[ship] = counter
            
        # return return dict
        return return_dict

    def get_ordered_rare_ship_list(self, player_list):
        ''' 
        '   This method will provide a list of ships (with duplicates) in order of rarity
        '   Parameters: Player list, ship list (strings)
        '   Returns: list of ship strings in order of most to least rare
        '''
        # get dict using class helper method
        # this dict has keys of ships in the lineup and values of how many players in the player list have that ship
        ship_dict = self.get_dict_players_with_ships(player_list)

        # set up empty return list
        return_list = []

        # this block of code creates a list of strings equal to the target ship lineup, 
        # with each element being a ship that is needed in the lineup, in order of least to most rare
        for i in range(min(ship_dict.values()), max(ship_dict.values())+1):     # iterate through ship rarirty from the most rare ship to least rare ship
            for ship in ship_dict:                                              # iterate through all ships in dict
                if ship_dict[ship] == i:                                        # if current ship is the rare one we are looking for
                    for count in range(self.target_ship_lineup.count(ship)):    # append that ship name to the return list as many times as the ship appears in our target lineup
                        return_list.append(ship)

        # return the return lis
        return return_list

    def get_list_players_owning_ship(self, ship_name, player_list):
        '''
        '   This function will return a list of players in a given list who own a ship
        '   Parameters: ship_name (string) and list of Player objects
        '   Return: list of Player objects who own the ship
        '''
        # setup return list of players
        return_list = []
        # interate through players in player list
        for player in player_list:
            if ship_name in player.ships.keys():
                return_list.append(player)
        
        # return return list
        return return_list

class Player:
    '''
    '   This class will represent each member of a clans roster.  
    '   Attributes: username_wg (string)
    '               username_discord (string)
    '               join_date (string), 
    '               ships (nested dict)
    '               is_active (boolean)
    '               is_alpha_team (boolean)
    '               overall_PR (int)
    '               overall_WR (float)
    '               overall_avg_damage (int)
    '               main_ship_class (string)
    '               
    '   Methods: __repr__
    '
    '''
    def __init__(self, header_list, input_list):
        ''' 
        '   The init function for setting up a player
        '   Parameters: list of strings (their line on the Google sheet)       
        '   Returns: none (sets up their lists of ships and some other attributes)
        '''

        # ATTRIBUTES
        self.username_wg = input_list[0]        # Username within Wargaming database
        self.username_discord = ''              # Username within Discord
        self.join_date = input_list[1]          # clan join date
        self.is_active = True                   # is player an active player
        self.is_alpha_team = True               # is the player a "core" or Alpha team player, as decided by clan admirals?
        # self.main_ship_class = ''               # what is their main class of ship (carrier-CV, battleship-BB, cruiser-CA, destroyer-DD, submarine-SS)
        self.overall_PR = 1500                  # Overall Personal Rating
        self.overall_WR = .6                    # Overall Win Rate
        self.overall_avg_damage = 90,000        # Overall Avg Damage
        self.ships = {}                         # ship roster, list of dictionaries as a dict
           
        # iterate through header_list after the username/join date columns (iterate through each ship)
        for i in range(2,len(header_list)):

            # Ship specific attributes
            leg_mod = False                 # do they have legendary module for that ship?
            player_pref = False             # does the player prefer to play this ship?
            admiral_pref = False            # does an admiral prefer the player plays this ship?
            ship_PR = 2000                  # Ship-specific Personal Rating
            ship_WR  = .5                   # Ship-specific Win rate
            ship_avg_damage = 100,000       # Ship-specific Avg damage

            # check to see if they have legendary mod 
            if 'mod' in input_list[i]:
                leg_mod = True
            # check to see if this ship is preferred for them
            if '*' in input_list[i]:
                player_pref = True
            # check player's PR rating with ship
            # CODE HERE to get and update PR, WR, and avg damage....json from Wargaming?

            # append dictionary to ship list
            if 'Y' in input_list[i]:
                self.ships[header_list[i]] = {  'legendary': leg_mod, 
                                                'player_preferred': player_pref, 
                                                'admiral_preferred': admiral_pref,
                                                'ship_PR': ship_PR,
                                                'ship_WR': ship_WR,
                                                'ship_avg_damage': ship_avg_damage
                                                }


    def __repr__(self):
        return self.username_wg


class Lineup:
    '''
    '   This object will be use to hold a certain lineup of ships.  It will also have many of 
    '   the methods needed for generating lineups.
    '
    '''
    def __init__(self, player_list, ship_list, input_score):
        ''' Parameters: list of Player objects and list of ships, also a "score" to help measure quality of lineup '''
        
        # a lineup "score" for algorithm purposes
        self.score = input_score

        # player/ship nexted list
        self.player_and_ship_list = []

        # combine player and ship list into one list of lists
        for i in range(len(player_list)):
            self.player_and_ship_list.append( [player_list[i].username_wg, ship_list[i]] )

    def __repr__(self):
        ''' Parameters: none Returns: string with each player/ship seperated on newlines '''
        return_string = ''
        for i in range(len(self.player_and_ship_list)):
            return_string += f'({self.player_and_ship_list[i][0]}, {self.player_and_ship_list[i][1]})\n'
        return_string += f"Linup score is {self.score}"
        return return_string
# =====================    END OF CLASSES  ======================= # 


# =====================    FUNCTIONS  ============================= #

def get_sheets_data(spreadsheets_id, range_name):
    '''
    '   This function handles the authentication and retrieval of data from a Google Sheet
    '   Parameters: The spreadsheet id and the range of data to pull    Return: 2D nested list of rows/cols
    '''

    # If modifying these scopes, delete the file token.pickle.  (not sure what this is for)
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'secrets.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=spreadsheets_id,
                                range=range_name).execute()
    values = result.get('values', [])

    # if unable to find the sheet
    if not values:
        return 'No data found.'
    # if able to find values, return them 
    else:
        return values

# =====================    END OF FUNCTIONS  ============================= #


# ============================    MAIN  ================================== #
# The ID and range of the test  spreadsheet.
clan_info_spreadsheet_ID = '14oxx0qpWg7VWhRyYIVP6uv5YL40BQI15APGDOwsdZdQ'
range_name = 'KSD Tier 10'

# for seeing if the Google Sheets API get works
# print(get_sheets_data(clan_info_spreadsheet_ID, range_name))

# 2D list of strings from Google Sheets
sheets_output = get_sheets_data(clan_info_spreadsheet_ID, range_name)

# create Clan object using output from sheets
clan = Clan(sheets_output)

##
## TESTING BELOW
##

# test Player list.  This will eventually be given to program by discord bot or by a GUI/app
test_player_list = [clan.get_player('manbear67'), clan.get_player('SWOdaddy'), clan.get_player('NotYou_2'), clan.get_player('McRendel1ten'), clan.get_player('Treegrin'), clan.get_player('br4in6'), clan.get_player('Buckeyefan21x'), clan.get_player('Maelon')]

print(clan.generate_lineup(test_player_list))