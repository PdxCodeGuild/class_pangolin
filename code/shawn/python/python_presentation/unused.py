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
        ordered_ship_list = self.get_ordered_rare_ship_list(player_list)
        for lineup_ship in ordered_ship_list:

            # create an empty list for players who have this ship
            players_with_lineup_ship = []

            # iterate through list of players who have the ship
            for player in self.get_list_players_owning_ship(lineup_ship, player_list):
                print(f"lineup_ship is {lineup_ship} and player is {player}")                       ## debugging ##
 
                # initialize points for this player/ship combo
                points = 0

                # first, see if this player can only play this ship
                counter = 0
                for ship in self.target_ship_lineup:
                    if ship in player.ships.keys():
                        counter += 1

                # if counter is 1, then slot them into that ship
                if counter == 1:
                    print(f"{player} can only play {lineup_ship}...must slot him into this role")
                    points = -math.inf           


                # # figure out how many other other ships in the lineup current player has
                # # using points:
                # ship_count = 0
                # for ship in player.ships:
                #     if ship in self.target_ship_lineup:
                #         ship_count += 1
                # # give player points for each ship he has
                # points += ship_count * const_points * mod_has_ship

                # should there be a way of doing this without points?  

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