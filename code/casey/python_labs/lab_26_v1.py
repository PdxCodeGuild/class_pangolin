'''
Lab 26: Tic-Tac-Toe - Version 1

Tic Tac Toe is a game. Players take turns placing tokens (a 'O' or 'X') into a 3x3 grid. Whoever gets three in a row first wins.

Purpose/goal: Write a Player class and Game class to model Tic Tac Toe, and a function main that models gameplay taking in user inputs through REPL.

'''

# The Game class has the following properties:
class Game:

# board = your representation of the board
    def __init__(self, board):
        board = [[" ", "|", " ", "|", " "], [" ", "|", " ", "|", " "], [" ", "|", " ", "|", " "]]