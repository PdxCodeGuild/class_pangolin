# Thank you for visiting https://asciiart.website/
# This ASCII pic can be found at
# https://asciiart.website/index.php?art=objects/computers

import random
import ttt_messages 
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
        ''' Takes in the Game Object and formats for diaplay the Board values '''
        return f'''\n
       ._,-,_.              _    ________    _       ______    __
       ||| |||    {self.board[0]}|{self.board[1]}|{self.board[2]}    / \  |__    __|  / \     |   _  \  |  |
       ||| |||    {self.board[3]}|{self.board[4]}|{self.board[5]}   / . \    |  |    / . \    |  |_) /  |  |
       ;|| ||:    {self.board[6]}|{self.board[7]}|{self.board[8]}  / /_\ \   |  |   / /_\ \   |     (   |  |
     ./ /| |\ \.        /  ___  \  |  |  /  ___  \  |  |\  \  |  |
     |./ :_: \.|       /__/   \__\ |__| /__/   \__\ |__| \__\ |__|\n'''
    
    @staticmethod
    def move(keyPad, player):
        ''' move(keyPad, player) Place a player's token character string at a given keypad location (top-left 0). '''
    
    def calc_winner(self):
        ''' calc_winner() What token character string has won or None if no one has. '''
        
    def is_full(self):
          ''' is_full() Returns true if the game board is full. '''
          for i in range(len(self)):
              if self[i] == ' ':
                  return False
                elif self[i] == '_':
                    return False
                else:True


    def is_game_over(self):
        ''' is_game_over() Returns true if the game board is full or a player has won. '''







