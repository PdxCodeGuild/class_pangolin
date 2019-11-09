# Shawn Stolsig
# PDX Code Guild
# Assignment: Optional Lab - Connect Four
# Date: 11/8/2019

import os

class Player:
    '''
    '   A class to represent each player
    '   Attributes: name and color
    '''
    def __init__(self,input_name,input_color):
        ''' The init function for Player class.  parameter: player name (string) and color (single char string) '''

        self.name = input_name
        self.color = input_color

class Game:
    '''
    '   A connect four game object.
    '   Attributes: game board (7x6 2D nested list) 
    '   Methods:
    '           get_height(position) returns int of how many pieces occupy a column
    '           move(player,position) adds a player token to a column after figuring out the current height of the column
    '           calc_winner(): returns True if four in a row are found
    '           is_full(): returns true if all board positions are occupied
    '           is_game_over(): returns true if the game is over (a winnder is found or the board is full)
    '           play_turn(): function that plays one turn
    '''

    def __init__(self):
        ''' The init function for the Game class.  Parameters: none  '''

        # the game board, a nested 2D list.  initialize each to ' '
        self.board = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]

    def __repr__(self):
        ''' function will print out game board '''
        
        # define return string
        return_str = ''

        # clear screen and logo
        os.system('cls' if os.name == 'nt' else 'clear')
        return_str = "   C O N N E C T   F O U R     \n"
        return_str += "=============================\n\n"

        # print game board
        return_str += "-----------------------------\n"
        for y in range(6):
            return_str += f"| {self.board[y][0]} | {self.board[y][1]} | {self.board[y][2]} | {self.board[y][3]} | {self.board[y][4]} | {self.board[y][5]} | {self.board[y][6]} |\n" 
            return_str += "-----------------------------\n"

        # return return string
        return return_str

    def get_height(self, position):
        '''
        '   A function that will return height of input position
        '   Parameters: input position (int)        Return: index if next available chip location (int)
        '''

        # iterate vertically through column, starting from bottom 
        for i in range(len(self.board)-1,-1,-1):
            # check to see if location is empty
            if self.board[i][position] == ' ':
                return i

        # return -1 if there is no available chip locations
        return -1

    def move(self, player, position):
        '''
        '   A function for placing a chip in a column of connect 4 game board
        '   Parameters: Player object and position (as int)     Returns: none (just updates game board)
        '''
        # get location where to place chip
        row = self.get_height(position)

        # update game board with appropriate chip color
        self.board[row][position] = player.color

    def play_turn(self, player):
        '''
        '   A function for asking the user for a position, and then validating it
        '   Parameters: player        Returns: none
        '''

        # get player input 
        while True:

            # get player input
            user_input = input(f"{player.name}'s turn.  Please enter a column for your chip: ").strip()

            # make sure input is between 1 and 7
            if len(user_input) == 1 and user_input in '1234567':

                # convert to int and into an index
                user_col = int(user_input) - 1     

                # check if column is not full
                if self.get_height(user_col) != -1:
                    break   
                # else column is full
                else:
                    print(f"Column {user_input} is full...please pick another column.")
            # print bad input message
            else: 
                print("Bad input...please enter a column between one and seven.")

        # update game board
        self.move(player,user_col)

p1 = Player("Shawn", 'R')
p2 = Player("Jeff", 'Y')
c4 = Game()

print(c4)
while True:
    c4.play_turn(p1)
    print(c4)
    c4.play_turn(p2)
    print(c4)