# Taylor Rebbe
# Lab_26 Tic Tac Toe
# 11/11.2019
# This ASCII pic can be found at (ATARI)
# https://asciiart.website/index.php?art=objects/computers

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
    
    def move(self, keyPad, Player):
        ''' move(keyPad, player) Place a player's token character string at a given keypad location (top-left 0). '''
        if self.board[keyPad] == ' ' or self.board[keyPad] == '_':
            self.board[keyPad] = Player.token
            return self.board
        else:
            return False

    def calc_winner(self):
        ''' calc_winner() What token character string has won or None if no one has. '''

        def x_check(self):
            ''' Helper to build x list for win check '''
            x_list = []
            for i in range(len(self.board)):
                if self.board[i] == 'X':
                    x_list.append(i)
                    continue
            if winner(x_list) != None:
                return 'X'

        def o_check(self):
            ''' Helper to build o list for win check '''
            o_list = []
            for i in range(len(self.board)):
                if self.board[i] == 'O':
                    o_list.append(i)
                    continue
            if winner(o_list) != None:
                return 'O'

        def winner(check):
            ''' Function to check if the winnning definitions are a subset of the build lists 'x_check() and o_check' '''
            winning_definitions = [[0, 1, 2], [0, 4, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [3, 4, 5], [6, 7, 8]]
            for i in range(len(winning_definitions)):
                if set(winning_definitions[i]).issubset(check):
                    return True

        # Calls helper methods which check for winning values for x or o    
        if x_check(self) == 'X':
            return 'X'
        if o_check(self) == 'O':
            return 'O'

    def is_full(self):
        ''' is_full() Returns true if the game board is full. '''
        for i in range(len(self.board)):
            if self.board[i] == ' ' or self.board[i] == '_':
                return False
        else:
            return True
        
    def is_game_over(self, calcwinner, isfull):
        ''' is_game_over() Returns true if the game board is full or a player has won. '''
        if calcwinner != None:
            return True
        elif isfull == True:
            return True
        else:
            return False







