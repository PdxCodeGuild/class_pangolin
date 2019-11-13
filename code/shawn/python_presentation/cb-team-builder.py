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
import math                             # for using INF in Lineup scoring system
from itertools import permutations     # for finding all possible permutations of input players
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

    def generate_lineup(self, player_list, team_size):
        '''
        '   This is the main algorithm for generating the best lineup.  One important note is that this algorithm
        '   is reliant on having a player list that is exactly as long as the target ship lineup
        '   Parameters: a list of player objects
        '   Returns: a Lineup object
        '''

        #   Here's how the algorithm will work:
        #   1. Generate all possible permutations of n players.  Each permutation is stored as a type Lineup
        #       a. In the Lineup ___init__ function, a score for the Lineup will be generated
        #       b. The score will then be used to decide which Lineup is best
        #       c. If a player is paired with a ship that is not in their port, then that lineup will be given a score of -INF
        #   2. Each lineup is stored in a list
        #   3. Iterate through the list and find the highest scoring Lineup
        #   4. If the highest scoring Lineup is -INF, then there is no valid lineup and it will err

        # Get list of permutations
        player_perms = list(permutations(player_list,team_size))
        
        # Iterate through permutations and create lineups
        player_perm_list = []
        for perm in player_perms:
            player_perm_list.append(Lineup(perm, self))

        # iterate through Lineups and find the one with the highest score
        best_score = -math.inf
        best_lineup = ''
        bad_perm_count = 0
        for lineup in player_perm_list:
            if lineup.score > best_score:
                best_score = lineup.score
                best_lineup = lineup
            if lineup.score == -math.inf:
                bad_perm_count += 1
            else:
                # print(f"evalutaing {lineup}")
                pass
        
        # some print messages about stats
        print(f"{len(player_perm_list)} permutations were checked: {bad_perm_count} were invalid and {len(player_perm_list)-bad_perm_count} were evaluated and compared against each other")

        # check to see if there is no a valid lineup
        if best_score == -math.inf:
            return False
        
        # return best lineup
        return best_lineup
    
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

    # constant variables for all Lineups
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

    def __init__(self, input_player_list, clan):
        ''' Parameters: list of Player objects and clan object (so that the target ship lineup can be retrieved) '''

        # player/ship nexted list
        self.player_and_ship_list = []

        # combine player and ship list into one list of lists
        for i in range(len(input_player_list)):
            self.player_and_ship_list.append( [input_player_list[i], clan.target_ship_lineup[i]] )

        # initialize points for this player/ship combo
        points = 0

        # calculate the Lineup's score
        for combo in self.player_and_ship_list:

            # if the ship is not in that player's list of ships, set points to -inf and skip the rest
            if combo[1] not in combo[0].ships.keys():
                points = -math.inf
            else:
                # add points if they are admiral preferred ship
                if combo[0].ships[combo[1]]['admiral_preferred']:
                    points += Lineup.const_points * Lineup.mod_admiral_preferred
                    
                # add points if alpha team player
                if combo[0].is_alpha_team:
                    points += Lineup.const_points * Lineup.mod_is_alpha

                # add points if player preferred ship
                if combo[0].ships[combo[1]]['player_preferred']:
                    points += Lineup.const_points * Lineup.mod_player_preferred           

                # add points if player doesn't main that class
                # add points if they don't need wins
                # add points if they have bad ship stats

        # set score equal to points
        self.score = points


    def __repr__(self):
        ''' Parameters: none Returns: string with each player/ship seperated on newlines '''
        return_string = ''
        for i in range(len(self.player_and_ship_list)):
            return_string += f'({self.player_and_ship_list[i][0]}, {self.player_and_ship_list[i][1]}) '
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
team_size = 8

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
short_player_list_test = [clan.get_player('manbear67'), clan.get_player('SWOdaddy'), clan.get_player('ItsAGameThing')]
actual_player_list = [clan.get_player('_Switch'), clan.get_player('br4in6'), clan.get_player('Kage_Acheron'), clan.get_player('Maelon'), clan.get_player('McRendel1ten'), clan.get_player('Sh1Zuk0'), clan.get_player('tehDugong'), clan.get_player('Ztulc')]
oversize_player_list = [clan.get_player('manbear67'), clan.get_player('SWOdaddy'), clan.get_player('_Switch'), clan.get_player('br4in6'), clan.get_player('Kage_Acheron'), clan.get_player('Maelon'), clan.get_player('McRendel1ten'), clan.get_player('Sh1Zuk0'), clan.get_player('tehDugong'), clan.get_player('Ztulc')]
supersize_player_list = [   clan.get_player('manbear67'), 
                            clan.get_player('SWOdaddy'), 
                            clan.get_player('_Switch'), 
                            clan.get_player('br4in6'), 
                            clan.get_player('Kage_Acheron'), 
                            clan.get_player('Maelon'), 
                            clan.get_player('McRendel1ten'), 
                            clan.get_player('Sh1Zuk0'), 
                            clan.get_player('tehDugong'), 
                            clan.get_player('Ztulc'),
                            clan.get_player('4_TRIDENT_4'),
                            clan.get_player('Acqua_Reale'),
                            clan.get_player('Admiral_Calamari'),
                            clan.get_player('Admiral_Gloval'),
                            clan.get_player('Feuerja'),
                            clan.get_player('kalman81')
                            ]
# print(clan.generate_lineup(test_player_list))
print(clan.generate_lineup(actual_player_list, team_size))