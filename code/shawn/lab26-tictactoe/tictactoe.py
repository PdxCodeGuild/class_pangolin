# Shawn Stolsig
# PDX Code Guild 
# Assignment: Lab 26 - Tic-Tac-Toe
# Date: 11/7/2019

import re   # inporting regular expression for handling x,y input for each turn
import os   # for clearing terminal when displaying game board

class Player:
    '''
    '   The Player class is used to represent name and token ('X' or 'O') for each player
    '   Attributes: name (string) token (string)   
    '   Methods: none
    '''
    
    def __init__(self,player_name,symbol):
        '''
        '   The __init__ function for the Player class.  
        '   Parameters: player's name (string) and symbol to represent them on the game board (string)
        '''
        self.name = player_name
        self.token = symbol

class Game:
    '''
    '   The Game class will hold all the info/actions needed for a game of tic tac toe
    '   Attributes: board (nested list of strings representation of the board), two Players 
    '   Methods: 
    '        __repr__() to return a visual representation of the board
    '       move(x,y,player) to place a player token at a given board location
    '       calc_winner() to figure out who/if a player has won
    '       is_full() to return True when game board is full and there's a tie
    '       is_game_over() returns True if game is over (either a win or a tie)     
    '       play_turn() will play one round with the input player
    '       get_valid_xy_coord() will prompt user for input and only return a valided x,y pair
    '''

    def __init__(self):
        '''
        '   __init__ function for Game class
        '   Parameters: none
        '''

        self.board = [[' ',' ',' '],
                      [' ',' ',' '],
                      [' ',' ',' ']]
        ''' Nested lists representing the board '''

        # self.player_one = p1
        # self.player_two = p2
        # ''' Two Player variables for holding the two player's names/symbols '''

    def __repr__(self):
        ''' 
        '   Function will return a pretty visual representation of the game board
        '   Parameters: none        Returns: string of game board
        '''
        # clear terminal before printing game board
        os.system('cls' if os.name == 'nt' else 'clear')

        # print logo
        print("***********************************")
        print("*********** tic tac toe ***********")
        print("***********************************")

        # init empty return string
        return_string = ''
        # iterate through board 2D list
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                # if the x value is in the middle, add | around the character to represent the vertical lines
                if x == 1:
                    return_string += '| ' + self.board[y][x] + ' |'
                # if the x value is not in the middle, omit the | character
                else:
                    return_string += ' ' + self.board[y][x] + ' '
            # add a newline between rows
            return_string += '\n'

        # return the return string
        return return_string

    def move(self,x,y,player_token):
        '''
        '   This function places a player's token at the given x,y position
        '   Parameters: x and y coordinates (as ints), player's token (as string)   Returns: none
        '''
        self.board[y][x] = player_token

    def calc_winner(self):
        '''
        '   Function will determine who (if anyone) has won
        '   Parameters: non     Return: player token of who won, or None if nobody won
        '''

        for symbol in ['X','O']:
            # to figure out if who one, we will check the verticals, horizontals, and then diagonals
            if self.board[0][0] == symbol and self.board[0][1] == symbol and self.board[0][2] == symbol:
                return symbol
            elif  self.board[1][0] == symbol and self.board[1][1] == symbol and self.board[1][2] == symbol:
                return symbol
            elif  self.board[2][0] == symbol and self.board[2][1] == symbol and self.board[2][2] == symbol:
                return symbol

            elif  self.board[0][0] == symbol and self.board[1][0] == symbol and self.board[2][0] == symbol:
                return symbol
            elif  self.board[0][1] == symbol and self.board[1][1] == symbol and self.board[2][1] == symbol:
                return symbol
            elif  self.board[0][2] == symbol and self.board[1][2] == symbol and self.board[2][2] == symbol:
                return symbol

            elif  self.board[0][0] == symbol and self.board[1][1] == symbol and self.board[2][2] == symbol:
                return symbol
            elif  self.board[0][2] == symbol and self.board[1][1] == symbol and self.board[2][0] == symbol:
                return symbol

    def is_full(self):
        '''
        '   Function to check if game board is full
        '   Parameters: none        Returns: boolean, True if game board is full
        '''

        # iterate through everything in the game board, if a blank is found return False
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                if self.board[x][y] == ' ':
                    return False

        # if iteration through the game board didn't find any empty locaitons, return True...board is full
        return True

    def is_game_over(self):
        '''
        '   Function to figure out if game has finished (in either a tie or someone wins)
        '   Parameters: none        Returns: bool (True if game is over)
        '''
        # if a winner is caluculated or board is full
        if self.calc_winner() or self.is_full():
            return True
        return False

    def play_turn(self, player):
        '''
        '   A function for playing a turn of tic tac toe
        '   Parameters: Player object      Return: none
        '''
        # print out who's turn
        print(f"{player.name}'s turn ({player.token}):")

        # get user validated user input
        x,y = self.get_valid_xy_coord()

        # update game board with input
        self.move(x,y,player.token)
            
    def get_valid_xy_coord(self):
        '''
        '   A function for getting validated x,y input
        '   Parameters: none            Returns: (x,y) int tuple that has been validated 
        '''
        # get x,y input
        while True:
            user_input = input("Please input x,y coordinates: ")

            # remove all whitespace
            user_input = user_input.replace(' ', '')

            # regex for x,y input
            regex = r"^[0-2]{1},[0-2]{1}$"

            # if a valid input
            if re.match(regex, user_input):
                x_input = int(user_input[0])         # takes first digit
                y_input = int(user_input[2])         # takes digit after comma
                
                # check to see if that place on game board is taken
                if self.board[y_input][x_input] == ' ':
                    # only return if that space is unoccupied.  must be ints so that they can be used as indexes
                    return x_input,y_input
                
                # print error message if space is taken
                else:
                    print(f"{x_input},{y_input} is already taken!")
            
            # if improper formatting, print error message
            else:
                print("Bad input.  Must be two comma-separated numbers, each between 0 and 2 (inclusive). ")

def game_init():
    '''
    '   A function for setting up a game of tic tac toe.
    '   Parameters: none    Returns: a tuple with three objects: Game, Player1, and Player2
    '''

    # clear terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    # print logo
    print("***********************************")
    print("*********** tic tac toe ***********")
    print("***********************************")

    # get user input
    user_name_1 = input("Enter player 1 name: ")
    user_name_2 = input("Enter player 2 name: ")

    # create player objects
    player1 = Player(user_name_1, 'X')
    player2 = Player(user_name_2, 'O')

    # create game board
    game_board = Game()

    # return tuple game, player1, player2
    return game_board, player1, player2

# main loop
while True:

    # initialize game and print empty game board
    game_board, player1, player2 = game_init()
    print(game_board)

    # counter for determining who's turn it is
    counter = 1

    # play turns
    while not game_board.is_game_over():
        # figure out who's turn it is
        if counter % 2 == 1:
            game_board.play_turn(player1)       # player one plays one odd counter numbers
        elif counter % 2 == 0:
            game_board.play_turn(player2)       # player two plays on even counter numbers
        
        # update counter
        counter += 1
        # print game board
        print(game_board)

    # check for winning condition
    if game_board.calc_winner():
        print(f"Player {game_board.calc_winner()} wins!")
    elif game_board.is_full():
        print(f"The board is full...{player1.name} ties {player2.name}")

    # ask if play again
    user_input = input("Play again? Please enter (y) or (n): ")
    if user_input == 'n':
        print("Game over.")
        break