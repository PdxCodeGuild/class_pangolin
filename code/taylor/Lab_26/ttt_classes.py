import random 
'''
Tic Tac Toe is a game. Players take turns placing tokens (a 'O' or 'X') into a 3x3 grid. Whoever gets three in a row first wins.

You will write a Player class and Game class to model Tic Tac Toe, and a function main that models gameplay taking in user inputs through REPL.

The Player class has the following properties:

name = player name
token = 'X' or 'O'
The Game class has the following properties:

board = your representation of the board
You can represent the board however you like, such as a 2D list, tuples, or dictionary.

The Game class has the following methods:

__repr__() Returns a pretty string representation of the game board '''

class Player:
    def __init__(self, name, token):
      self.name = name
      self.token = token

class Game:
    def __init__(self, board):
        self.board = board

    def __repr__(self):
        print('Hello')
    
    @staticmethod
    def move(x, y, player):
        ''' move(x, y, player) Place a player's token character string at a given coordinate (top-left is 0, 0), x is horizontal position, y is vertical position. '''
    
    def calc_winner(self):
        ''' calc_winner() What token character string has won or None if no one has. '''
        
    def is_full(self):
        ''' is_full() Returns true if the game board is full. '''
    def is_game_over(self):
        ''' is_game_over() Returns true if the game board is full or a player has won. '''







