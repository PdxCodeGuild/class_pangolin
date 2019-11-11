#Bieschke Lab 26: tic tac toe.py

class Game():
    def __init__(self, board):
        self.board = board
        print("Welcome to Tic-Tac-Toe!")

        self.board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
                      'ctr-L': ' ', 'ctr-M': ' ', 'ctr-R': ' ',
                      'bot-L': ' ', 'bot-M': ' ', 'bot-R': ' '}

    def __repr__(self):
        print(self.board)


    def move(self, x, y, player):
        self.x = x
        self.y = y
        self.player = player

    def calc_winner(self):
        print("Calculates board conditions for victory")

    def is_full(self):
        print("Determines if there are no more possible moves")

    def game_over(self):
        print("Uses calc_winner, then is_full to determine if the game is over")
        print("This will need to run after every move")

class Player():
    def __init__(self, name, token):
        self.name = name
        self.token = token

print(Game(board[0]))