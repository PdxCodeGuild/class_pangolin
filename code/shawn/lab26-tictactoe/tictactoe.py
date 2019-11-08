# Shawn Stolsig
# PDX Code Guild 
# Assignment: Lab 26 - Tic-Tac-Toe
# Date: 11/7/2019

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

    def move(self,x,y,player):
        '''
        '   This function places a player's token at the given x,y position
        '   Parameters: x and y coordinates (as ints), player's token (as string)   Returns: none
        '''
        self.board[y][x] = player.token

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

# set up game
player_one = Player('Shawn', 'X')
player_two = Player('Jeff', 'O')
game_board = Game()
print(game_board.board)
print(game_board)
game_board.move(0,0,player_two)
game_board.move(1,1,player_two)
game_board.move(2,2,player_two)
game_board.move(1,2,player_one)
print(game_board)
print(game_board.board)
print(game_board.calc_winner())

