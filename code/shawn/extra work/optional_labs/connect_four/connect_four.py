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
    '           play(): function that plays whole game, given two player
    '           recursive_chip_checker(): recurisvely checks in all directions to find if theres a connect 4
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
        return_str += "  1   2   3   4   5   6   7  \n"

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
        '   Parameters: input position (int)        Return: index if next available chip location (int).  returns -1 if full
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

    def play_turn(self, player, input_move=''):
        '''
        '   A function for asking the user for a position, and then validating it
        '   Parameters: player, optional list of strings as input moves        Returns: none
        '''

        # if moves are passed in, use input file
        if input_move:
            
            # convert move to int and index
            input_move = int(input_move) - 1

            # play move
            self.move(player,input_move)

        # no moves passed in...play game with user input
        else:
            # get player input 
            while True:

                # get player input
                user_input = input(f"{player.name}'s turn.  Please enter a column for your {player.color} chip: ").strip()

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
  
    def is_full(self):
        '''
        '   A function for finding if all columns are full
        '   Parameters: none        Returns: boolean (True if all columns full)
        '''
        # iterate through all columns of board
        for y in range(len(self.board)):
            # iterate through all rows of board
            for x in range(len(self.board[y])):
                # if any cell is empty, update flag to False
                if self.board[y][x] == ' ':
                    return False
        
        # Return true if it iterates through board and doesn't find an empty
        return True

    def is_game_over(self, p1, p2):     # not currently used
        '''
        '   A function for checking if the game is over.  
        '   Parameters: None        Returns: boolean (true if game is over)
        '''
        # check to see if there's a winner
        if self.calc_winner(p1) or self.calc_winner(p2):
            # return True if there's a winner
            return True
        # check to see if game board is full
        if self.is_full():
            # return True if game board is full
            return True
        # return false if no winner and board not full
        return False

    def calc_winner(self, player): 
        '''
        '   This function will check to see if there's a winner
        '   Parameters: player (for getting their token color)    Return: True/False if winner
        '''
        # list for tracking results
        result_list = []

        # iterate through all cells
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                # call recursive chip checker on for each cell, in each direction
                # might not actually need to check each direction, but for clarity's sake....

                # up
                result_list.append(self.recursive_chip_checker(x,y,0,1,0,player.color))
                # up-right
                result_list.append(self.recursive_chip_checker(x,y,1,1,0,player.color))
                # right
                result_list.append(self.recursive_chip_checker(x,y,1,0,0,player.color))
                # down-right
                result_list.append(self.recursive_chip_checker(x,y,1,-1,0,player.color))
                # down
                result_list.append(self.recursive_chip_checker(x,y,0,-1,0,player.color))
                # down-left
                result_list.append(self.recursive_chip_checker(x,y,-1,-1,0,player.color))
                # left
                result_list.append(self.recursive_chip_checker(x,y,-1,0,0,player.color))
                # up-left
                result_list.append(self.recursive_chip_checker(x,y,-1,1,0,player.color))

        # return true if there is a true value in the list...else, return false
        if True in result_list:
            return True
        else:
            return False

    def recursive_chip_checker(self, curr_x, curr_y, x_dir, y_dir, count, color): 
        '''
        '   This function will (recursivel) check to see if there is a winner
        '   Parameters: x and y of current cell, x direction, y direction (-1, 0, or 1), a count for # correct chips in a row, player's color
        '   Return: True (if the input color is a winner) or false boolean
        '''

        # try to check current cell, catching index error
        try:
            # if the item at board[y][x] is the same player's chip
            if self.board[curr_y][curr_x] == color:
                # update count for the match
                count += 1
                # check to see if there is a connect 4...return true if so:
                if count == 4:
                    return True
                # else, recursively call chip checker with updated x/y coordinates
                else:
                    # update x and y based on input direction modifiers
                    curr_y += y_dir
                    curr_x += x_dir
                    # recursively call function
                    return self.recursive_chip_checker(curr_x, curr_y, x_dir, y_dir, count, color)

            # if the item at board[y][x] is an empty cell, return false:
            elif self.board[curr_y][curr_x] == ' ':
                return False

            # else, blocked by opposite player...return false
            else:
                return False

        # excepting IndexError so it doesn't recursively iterate off the board...return false
        except IndexError:
            return False

    def play(self, p1, p2):
        '''
        '   A function for containing main game, so that you can play multiple times    
        '   Parameter: players 1 and 2         Return: none
        '''
        # counter for figuring out who's turn it is
        counter = 0

        while True:
            # print game board
            print(self)

            # player 1 plays on even turns
            if counter % 2 == 0:
                self.play_turn(p1)

            # player 2 plays on odd turns
            else:
                self.play_turn(p2)

            # increment counter
            counter += 1

            # check to see if game is over (either full board or winner)
            if self.is_game_over(p1, p2):
                break

        # check to see if player 1 won
        if self.calc_winner(p1):
            print(self)
            return f"{p1.name} won!"

        # check to see if player 2 won
        elif self.calc_winner(p2):
            print(self)
            return f"{p2.name} won!"

        # else, must be tie
        return "Game board is full...players tied."

# Set up players and first game
# clear screen and logo
os.system('cls' if os.name == 'nt' else 'clear')
print("    C O N N E C T   F O U R    ")
print("===============================")
player1 = Player(input("Please enter name for red player: "), 'R')
player2 = Player(input("Please enter name for yellow player: "), 'Y')

# # -------------------------  This is version 1 -------------------------------------------#
# # open input file
# # specifying encoding as utf-8-sig due to ï»¿ that was showing up at start of string list
# with open('connect-four-moves.txt', 'r', encoding='utf-8-sig') as f:
#         moves = f.read().strip().split('\n')

# connect4 = Game()

# for version 1: using input file
# iterate through moves in the input file
# for i in range(len(moves)):
    
#     # player 1 goes on even turns
#     if i % 2 == 0:
#         c4.play_turn(p1,moves[i])
#     # player 2 goes on odd turns
#     elif i % 2 == 1:
#         c4.play_turn(p2,moves[i])

#     print(c4)
# # ---------------------------  End of version 1 -------------------------------------------#


# for version 2/3: playable
while True:
    # create new game
    connect4 = Game()
    # play whole game
    print(connect4.play(player1,player2))

    # see if user wants to play again
    while True:
        user_input = input("Play again? Enter (y) or (n): ")
        if user_input.lower() in ['n','no']:
            print("Game over.")
            exit()
        elif user_input.lower() not in ['y','yes']:
            print("Invalid input.")
        else:
            print("Starting new game.")
            break
