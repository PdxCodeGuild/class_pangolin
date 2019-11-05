# Shawn Stolsig
# PDX Code Guild 
# Assignment: Optional Lab - LCR Simulator
# Date: 11/4/2019

import random

# function to set up the game
def game_setup():
    ''' arguments: none
        returns: nested list of player names and chip counts '''

    # init player list
    players = []

    # get player names
    while True:
        user_input = input("Please enter player name or (done): ")
        if user_input in ['done', 'd', 'Done']:
            break
        # if not done, add a player with the user input as a name and 3 chips
        players.append([user_input, 3])

    # return list of players
    return players


# function for rolling dice
def roll_dice(player):
    ''' arguments: player list [name,chip count]
        return: tuple of amounts in (L,C,R) format '''

    # figure out how many dice to roll
    if player[1] == 0:
        return (0,0,0)          # no play since they have no dice to roll
    elif player[1] < 3:
        dice_to_roll = player[1]
    else:
        dice_to_roll = 3
    
    # use list to define what a dice looks like
    die = ['L', 'C', 'R', '.', '.', '.']

    # counters for each direction
    left = center = right = 0

    # roll dice, one at a time, with a For loop
    for i in range(dice_to_roll):
        roll = random.choice(die)
        print(f"{player[0]} rolled dice and got {roll}")
        if roll == 'L': 
            left += 1
        elif roll == 'C':
            center += 1
        elif roll == 'R':
            right += 1
        # don't catch a '.' roll...it takes no action

    # return tuple of where each chip goes
    return left,center,right

# function for a player's turn
def play_game(players):
    ''' arguments: list of player lists
        return: string of who won and an int of how many chips in the pot'''

    # pot variable will be used to track how many chips in the middle
    pot = 0

    # use a while loop to go on indefinitely until there is a winner
    while True:
        # iterate through players in player list
        for i in range(len(players)):
            # have that player roll dice
            left,center,right = roll_dice(players[i])
            # update players list based on results.  must control for index error when looking at player ot the right of the last position
            players[i][1] -= left + center + right                                          # update player count
            pot += center                                                                   # update center pot
            players[i-1][1] += left                                                         # update player to the left
            # update player to right.  wrap around to 0 index if at end of players
            if i == (len(players) - 1):
                players[0][1] += right
            else:
                players[i+1][1] += right

        # if there's a winner
            print(f"Pot is now {pot}.  Players are {players}....currently checking for winners.")
            winner = check_for_win(players)
            if winner:
                return winner,pot

# function to check for winning condition
def check_for_win(players):
    ''' arguments: players as lists [name,chip count],
        return: player list when winner, False if no winner '''

    # figure out how many total chips in play
    total_chips = 0
    for player in players:
        total_chips += player[1]

    # iterate through list and see if anyone has all of the chips
    for player in players:
        if player[1] == total_chips:
            print(f"player {player[0]} has {player[1]} chips")
            return player

    # return false if winning condition not found
    return False

# program start:

# get input/set up game:
# player names and chip counts will be stored in a nested list
players = game_setup()                                                                        ### uncomment this to inable user input of names!
# players = [['Shawn', 3], ['Hylary', 3], ['Jeff',3]]
print(f'Initial game setup: {players}')

# main game loop
while True:

    print(f'Players are: {players}')

    winner,pot = play_game(players)
    print(f'Game over!  {winner[0]} won with {winner[1]} chips remaining.  {winner[0]} wins a pot of {pot} chips!' )

    # update chip counts in case they want to play again
    winner[1] += pot
    # refill players who are out of chips
    for player in players:
        if player[1] == 0:
            player[1] = 3

    # ask the user to play again
    user_input = input("Play again? Enter (y) or (n): ")
    if user_input not in ['y','Y','Yes','yes']:
        break
