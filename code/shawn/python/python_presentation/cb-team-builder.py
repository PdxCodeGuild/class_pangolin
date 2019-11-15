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
from tkinter import *                   # for GUI
from tkinter import ttk                 # for themed widgets
from tkinter import messagebox
from itertools import permutations      # for finding all possible permutations of input players
# =====================    CLASSES  ============================= #
class Clan:
    '''
    '   This class will hold all information related to a clan (mainly the roster and preferred ship lineup)
    '   Attributes: A roster of players (list of Player objects)
    '               A list of ships (the header of the input spreadsheet)
    '   Methods: get_player - Get a player object from the clan's roster given a username string
    '            generate_lineup - the main player lineup algorithm
    '            get_list_of_players_owning_ship - get a list of players in the clan who own a specific ship
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
        lineup_id = 0
        for perm in player_perms:
            lineup_id += 1
            player_perm_list.append(Lineup(perm, self, lineup_id))
        total_perm_count = lineup_id
        
        # iterate through Lineups and find the one with the highest score
        bad_perm_count = 0

        # iterate through from end of list to front so that bad lineups can be removed without causing index errors
        for i in range(len(player_perm_list)-1,-1,-1):
            # if the current lineup is invalid (score is -inf)
            if player_perm_list[i].score == -math.inf:
                # update the bad lineup count
                bad_perm_count += 1
                # pop this element from the list
                player_perm_list.pop(i)

        # sort the remaining lineups by score
        player_perm_list.sort(key=lambda x: x.score, reverse=True)

        # some print messages about stats
        print(f"{len(player_perm_list)} permutations were checked: {bad_perm_count} were invalid and {total_perm_count-bad_perm_count} were evaluated and compared against each other")

        # check to see if there is no a valid lineup
        if len(player_perm_list) == 0:
            return False, bad_perm_count, total_perm_count
        
        # return sorted best to worst list of lineups, the total bad lineups that were thrown out, and the total permutations generated
        return player_perm_list, bad_perm_count, total_perm_count
    
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
                    for j in range(self.target_ship_lineup.count(ship)):    # append that ship name to the return list as many times as the ship appears in our target lineup
                        return_list.append(ship)

        # return the return lis
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



            # append dictionary to ship list if the ship is unlocked
            if 'Y' in input_list[i]:
                # Ship specific attributes
                is_ship_available = True        # do they have the ship in port, ready to play? 
                leg_mod = False                 # do they have legendary module for that ship?
                player_pref = False             # does the player prefer to play this ship?
                admiral_strong_pref = False     # does an admiral strongly prefer the player plays this ship?
                admiral_weak_pref = False       # does an admiral weakly prefer the player plays this ship?
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
                
                self.ships[header_list[i]] = {  'is_ship_available': is_ship_available,
                                                'legendary': leg_mod, 
                                                'player_preferred': player_pref, 
                                                'admiral_strong_preferred': admiral_strong_pref,
                                                'admiral_weak_preferred': admiral_weak_pref,
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
    # mod_has_ship = 0.3
    mod_admiral_strong_preferred = 0.5
    mod_admiral_weak_preferred = 0.1
    mod_player_preferred = 0.1
    mod_is_alpha = 0.1
    mod_is_main_class = 0.5
    # (modifiers not yet used):
    mod_stat_PR = 1
    mod_stat_WR = 1
    mod_stat_AVG_DMG = 1
    mod_needs_wins = 1

    def __init__(self, input_player_list, clan, lineup_id):
        ''' Parameters: list of Player objects and clan object (so that the target ship lineup can be retrieved) '''

        # store lineup id
        self.id = lineup_id

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
                if combo[0].ships[combo[1]]['admiral_strong_preferred']:
                    points += Lineup.const_points * Lineup.mod_admiral_strong_preferred
                # add points if they are admiral preferred ship
                if combo[0].ships[combo[1]]['admiral_weak_preferred']:
                    points += Lineup.const_points * Lineup.mod_admiral_weak_preferred
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

class Interface:
    '''
    '   This is an interface class to managing information in the Tkinter Gui
    '''
    def __init__(self, root, clan, image):
        '''constructor'''

        # set some basic properties of GUI window
        root.title("WoWs Clan Battle Team Builder")

        # tell Tkinter to resize root frame with the window
        # root.columnconfigure(0,weight=1)                        
        # root.rowconfigure(0,weight=1)
        root.resizable(False, False)

        # setting up all grid framework that will hold all contents of main window
        self.main_frame = ttk.Frame(root).grid(column=0, row=0, sticky=(N,W,E,S))

        # add some padding to each widget
        for child in root.winfo_children(): child.grid_configure(padx=5, pady=5)

        # add label widgets
        # list labels that won't be changed
        ttk.Label(self.main_frame, text="Clan Roster").grid(column=1, row=1)
        ttk.Label(self.main_frame, text="Selected Players").grid(column=3, row=1)
        ttk.Label(self.main_frame, text="Possible Lineups").grid(column=1, row=15)
        ttk.Label(self.main_frame, text="Selected Lineup").grid(column=3, row=15)
        ttk.Label(self.main_frame, image=image).grid(column=4, row=4)
        ttk.Label(self.main_frame, text="   Ship Composition:  ").grid(column=4, row=6)        

        # list labels that will be changed
        # bottom status bar
        self.label_status = ttk.Label(self.main_frame, text=" ")
        self.label_status.grid(column=1, row=28, columnspan=4)
        self.player_count = ttk.Label(self.main_frame, text=" ")     
        # target ship list at the right
        self.update_target_ship_list(clan)                                           

        # add treeviews and pack for listing players/lineups
        self.tree_clan_players = ttk.Treeview(self.main_frame, show='tree')
        self.tree_clan_players.grid(column=1, row=2, rowspan=12)
        self.tree_selected_players = ttk.Treeview(self.main_frame, show='tree')
        self.tree_selected_players.grid(column=3, row=2, rowspan=12)
        self.tree_possible_lineups = ttk.Treeview(self.main_frame, show='tree', selectmode="browse")
        self.tree_possible_lineups.grid(column=1, row=16, rowspan=12)
        self.tree_selected_lineup = ttk.Treeview(self.main_frame, show='tree', selectmode="none")
        self.tree_selected_lineup.grid(column=3, row=16, rowspan=12)

        # add buttons and pack to grid
        self.button_add = ttk.Button(self.main_frame, text="Add", command=self.select_players)
        self.button_add.grid(column=2, row=6)
        self.error_label = ttk.Label(self.main_frame, text="Already selected!")
        self.button_remove = ttk.Button(self.main_frame, text="Remove", command=self.remove_players)
        self.button_remove.grid(column=2, row=7)
        self.button_clear = ttk.Button(self.main_frame, text="Clear", command=self.clear_players)
        self.button_clear.grid(column=2, row=8)
        self.button_generate_lineups = ttk.Button(self.main_frame, text="Generate Lineups", command=self.start_algorithm, state=DISABLED)
        self.button_generate_lineups.grid(column=2, row=14)
        self.button_team_comp = ttk.Button(self.main_frame, text="Update Ship Composition", command=self.update_ship_comp, state=DISABLED)
        self.button_team_comp.grid(column=4, row=20, rowspan=3)

        # add info to lists
        for player in clan.roster:
            self.tree_clan_players.insert('', 'end', player.username_wg, text=player.username_wg)

        # store clan to be used for start_algorithm method
        self.stored_clan = clan

    def select_players(self):
        '''
        '   When button_add is pressed, call this fuction to move players to selected list
        '
        '''
        # using try to catch if player has already been added...can't add same player treeview twice
        try:
            # get selection from left treeview
            selection = self.tree_clan_players.selection()
            # for each player in selection
            for player in selection:
                # add player to selected tree view
                self.tree_selected_players.insert('','end', player, text=player)

            # clear 'already selected" error message bhy forgetting the pack
            self.error_label.grid_forget()

            # update player count
            self.player_count.configure(text=f"Player Count: {len(self.tree_selected_players.get_children())}")
            self.player_count.grid(column=3, row=14, sticky=N)

            # enable button if enough players are selected
            if len(self.tree_selected_players.get_children()) == len(self.stored_clan.target_ship_lineup):
                self.button_generate_lineups.configure(state = 'normal')
            else:
                self.button_generate_lineups.configure(state = DISABLED)

        # show/pack error message if player already selected
        except TclError:
            # error is shown by packing error message into grid (already created label in init)
            self.error_label.grid(column=2, row=4)

    def remove_players(self):
        '''
        '   When button_remove is pressed, call this fuction to remove players to selected list
        '
        '''
        selection = self.tree_selected_players.selection()
        for player in selection:
            self.tree_selected_players.delete(player)
        
        # update player count
        self.player_count.configure(text=f"Player Count: {len(self.tree_selected_players.get_children())}")
        self.player_count.grid(column=3, row=14, sticky=N)             

        # enable button if enough players are selected
        if len(self.tree_selected_players.get_children()) == len(self.stored_clan.target_ship_lineup):
            self.button_generate_lineups.configure(state = 'normal')
        else:
            self.button_generate_lineups.configure(state = DISABLED)

    def clear_players(self):
        '''
        '   When button_clear is pressed, call this fuction to clear players from selected list
        '
        '''
        # clear all trees, hide the player count
        self.tree_possible_lineups.delete(*self.tree_possible_lineups.get_children())
        self.tree_selected_lineup.delete(*self.tree_selected_lineup.get_children())
        self.tree_selected_players.delete(*self.tree_selected_players.get_children())
        self.player_count.grid_forget()
        # disable generate button
        self.button_generate_lineups.configure(state=DISABLED)

    def update_target_ship_list(self,clan):
        '''
        '   A function for updating the target ship lineup
        '
        '''
        for i in range(len(clan.target_ship_lineup)):
            ttk.Label(self.main_frame, text=f"{i+1}. {clan.target_ship_lineup[i]}").grid(column=4, row=(6+1+i))          

    def start_algorithm(self):

        # reset/remove items from possible and selected lineup trees
        self.tree_possible_lineups.delete(*self.tree_possible_lineups.get_children())
        self.tree_selected_lineup.delete(*self.tree_selected_lineup.get_children())

        # get list of player objects
        player_obj_list = []
        for player in self.tree_selected_players.get_children():
            player_obj_list.append(self.stored_clan.get_player(player))
        print(f"playe_obj list is {player_obj_list}")

        # call generate lineups
        self.generated_lineups, bad_perm_count, total_perm_count = self.stored_clan.generate_lineup(player_obj_list,len(player_obj_list))

        try:
            # put lineups into tree_possible_lineups
            for lineup in self.generated_lineups:
                self.tree_possible_lineups.insert('', 'end', lineup.id, text=f"Lineup ID: {lineup.id}  Score: {lineup.score}")      
        except TypeError:
            # if no valid lineups, show error message
            if not self.generated_lineups:
                messagebox.showerror("Lineup Error", "Those players cannot form the desired ship composition!  Please select different players.")
      
        # update status bar
        self.label_status.configure(text=f"{total_perm_count} total permutations with {bad_perm_count} invalid lineups.\n Showing {total_perm_count-bad_perm_count} valid lineups in best to worst order.")

        # bind an event so that you can display a lineup when it's selected in tree_possible_lineups
        self.tree_possible_lineups.bind("<<TreeviewSelect>>",self.on_possible_lineup_click)

    def on_possible_lineup_click(self,virtual_event):

        # reset/remove items from tree_selected_lineup
        self.tree_selected_lineup.delete(*self.tree_selected_lineup.get_children())

        # get lineup ID
        this_lineup_id = int(self.tree_possible_lineups.selection()[0])
        # retrieve lineup object
        for lineup in self.generated_lineups:
            if int(lineup.id) == this_lineup_id:
                this_lineup_obj = lineup

        # print(f"Lineup retrieved: {this_lineup_obj}")

        # print lineup to tree selected lineup
        for combo in this_lineup_obj.player_and_ship_list:
            self.tree_selected_lineup.insert('', 'end', combo[0], text=f"{combo[1]}:     {combo[0]}")           

    def update_ship_comp(self):
        print('update ship comp')
        
# =====================    END OF CLASSES  ======================= # 


# =====================   Non-class FUNCTIONS  =========================== #

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

# # uncomment below when basic UI ready
# # 2D list of strings from Google Sheets
try:
    sheets_output = get_sheets_data(clan_info_spreadsheet_ID, range_name)             
except:
    print("Error reaching Google Sheets, exiting. ")
    exit()

# # create Clan object using output from sheets
clan = Clan(sheets_output)                                                        
# # test player inputs
short_player_list_test = [clan.get_player('manbear67'), clan.get_player('SWOdaddy'), clan.get_player('ItsAGameThing')]
actual_player_list = [clan.get_player('_Switch'), clan.get_player('br4in6'), clan.get_player('Kage_Acheron'), clan.get_player('Maelon'), clan.get_player('McRendel1ten'), clan.get_player('Sh1Zuk0'), clan.get_player('tehDugong'), clan.get_player('Ztulc')]
oversize_player_list = [clan.get_player('manbear67'), clan.get_player('SWOdaddy'), clan.get_player('_Switch'), clan.get_player('br4in6'), clan.get_player('Kage_Acheron'), clan.get_player('Maelon'), clan.get_player('McRendel1ten'), clan.get_player('Sh1Zuk0'), clan.get_player('tehDugong'), clan.get_player('Ztulc')]
supersize_player_list = [   clan.get_player('manbear67'), clan.get_player('SWOdaddy'), clan.get_player('_Switch'), clan.get_player('br4in6'), clan.get_player('Kage_Acheron'), clan.get_player('Maelon'), clan.get_player('McRendel1ten'), clan.get_player('Sh1Zuk0'), clan.get_player('tehDugong'), clan.get_player('Ztulc'),clan.get_player('4_TRIDENT_4'),clan.get_player('Acqua_Reale'),clan.get_player('Admiral_Calamari'),clan.get_player('Admiral_Gloval'),clan.get_player('Feuerja'),clan.get_player('kalman81')]

# set up GUI
root = Tk()

# open image for right side
image = PhotoImage(file='wows_icon.png')

# create instance of interface

gui = Interface(root, clan, image)

root.mainloop()
