class Player:
    '''
    '   This class will represent each member of a clans roster.  
    '   Attributes: Dictionary of each ship they have in port
    '   Methods: 
    '
    '''
    def __init__(self, header_list, input_list):
        ''' 
        '   The init function for setting up a player
        '   Parameters: list of strings (their line on the Google sheet)       
        '   Returns: none (sets up their lists of ships and some other attributes)
        '''

        # username (two...one for discord, one for Wargaming)
        self.username_wg = input_list[0]

        # clan join date
        self.join_date = input_list[1]

        # ship roster, list of dictionaries as a dict
        self.ships = {}
        
        # iterate through header_list after the username/join date columns (iterate through each ship)
        for i in range(2,len(header_list)):

            # booleans for legendary mod and if ship is preferred (by both player and admiral)
            leg_mod = False
            player_pref = False
            admiral_pref = False

            # check to see if they have legendary mod 
            if 'mod' in input_list[i]:
                leg_mod = True
            # check to see if this ship is preferred for them
            if '*' in input_list[i]:
                player_pref = True

            # append dictionary to ship list
            self.ships[header_list[i]] = {'legendary': leg_mod, 'player_preferred': player_pref, 'admiral_preferred': admiral_pref}

        # UNUSED ATTRIBUTES....for future development:
        # what type of ship that player mains...submarine, destroyer, cruiser, battleship, carrier
        self.username_discord = ''     
        self.main = ''

    def __repr__(self):
        return f'{self.username_wg} with {len(self.ships)} ships'