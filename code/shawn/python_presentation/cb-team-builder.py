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

        # order the ships in preferred lineup based on which are rarest in the clan

        # iterate through preferred ship lineup list, rarest ship first
            # get list of players who have that ship
            # iterate through list of players who have the ship
                # assign each player a score for that ship, based on following factors:
                    # how many other ships remaining in the copy of target lineup they have
                        # if they have none, then slot them in current ship
                    # are they admiral preferred
                    # are they alpha team
                    # are they player preferred
                    # does player main that class
                    # stats 
            # order the player list by score
            # pop off the Player from player_list with the highest score, add them to the to-be-returned Lineup
            # pop off that ship from the copy of the target ship lineup

    @staticmethod
    def get_dict_players_with_ships(player_list, ship_list):
        '''
        '   This function will help figure out how "rare" each ship is, based on the input Players
        '   Static method since it's a helper function for ship rosters and ship lineups
        '   Parameters: list of Player objects, list of ships (as strings)
        '   Return: a dictionary of ship: number of players with ship 
        '''
        # declare empty return dictionary
        return_dict = {}

        # iterate through ships:
        for ship in ship_list:
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
                        # increment counter
                        counter += 1
                # add that ship to dictionary as a key with the number of players as the value
                return_dict[ship] = counter
            
        # return return dict
        return return_dict


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
        self.main_ship_class = ''               # what is their main class of ship (carrier-CV, battleship-BB, cruiser-CA, destroyer-DD, submarine-SS)
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
    def __init__(self, player_list, ship_list):
        ''' Parameters: list of Player objects and list of ships '''
        
        # a lineup "score" for algorithm purposes
        self.score = 0

        # player/ship nexted list
        self.player_and_ship_list = []

        # combine player and ship list into one list of tuples
        for i in range(len(player_list)):
            self.player_and_ship_list.append( [player_list[i].username_wg, ship_list[i]] )

    def __repr__(self):
        ''' Parameters: none Returns: string with each player/ship seperated on newlines '''
        return_string = ''
        for i in range(len(self.player_and_ship_list)):
            return_string += f'({self.player_and_ship_list[i][0]}, {self.player_and_ship_list[i][1]})\n'
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

test_lineup = Lineup(test_player_list, clan.target_ship_lineup)
print(Clan.get_dict_players_with_ships(test_player_list, clan.target_ship_lineup))