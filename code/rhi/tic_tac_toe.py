'''
Tic tac toe lab
written by Rhornberger
last updated nov 10th 2019
'''
# set the board
import os
os.system('cls')
class Board():
    def __init__(self):
        self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    
    def display(self):
        print(' %c | %c | %c' % (self.board[1], self.board[2], self.board[3]))
        print('-----------')
        print(' %c | %c | %c' % (self.board[4], self.board[5], self.board[6]))
        print('-----------')
        print(' %c | %c | %c' % (self.board[7], self.board[8], self.board[9]))
    
    def update_cell(self, cell_num, player):
        if self.board[cell_num] == ' ':
            self.board[cell_num] = player
        else:
            return "You have tried to take over a space already occupied by a token so you lose your turn as a penalty"
    def winner_winner(self, player):
        row1 = [self.board[1], self.board[2], self.board[3]]
        row2 = [self.board[4], self.board[5], self.board[6]]
        row3 = [self.board[7], self.board[8], self.board[9]]
        col1 = [self.board[1], self.board[4], self.board[7]]
        col2 = [self.board[2], self.board[5], self.board[8]]
        col3 = [self.board[3], self.board[6], self.board[9]]
        diag1 = [self.board[1], self.board[5], self.board[9]]
        diag2 = [self.board[3], self.board[5], self.board[7]]
        for comb in (row1, row2, row3, col1, col2, col3, diag1, diag2):
            if comb == [player, player, player]:
                return True
            if comb == [player, player, player]:
                return True
            return False
    def tie_board(self):
        full_cell = 0
        for cell in self.board:
            if cell != ' ':
                full_cell += 1
        if full_cell == 9:
            return True
        else:
            return False
    def play_again(self):
        self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

b1 = Board()
class Player():
    def __init__(self, name, token):
        self.name = name
        self.token = token
   
    def __repr__(self):
        return f"({self.token}): {self.name}"

name_list = []
token_list = ['X', 'O']

# player_list = {}
print('Whoever becomes player 1 will have the X token.')
player_name = input('What is the name of player 1?: ').lower()
name_list.append(player_name)
player2_name = input('What is the name of player 2?: ').lower()
name_list.append(player2_name)

for num in range(2):
    c1 = Player(name=name_list[num], token=token_list[num])    


# functions to run game
def introduction():
    print('Welcome to the Game of Tic Tac Toe!')
    print('Be careful, if you try to take over a space already occupied by a token you will lose your turn as a penalty!')
def start_game():
    #clear screen
    os.system('cls')
    #display board
    b1.display()

# run the game
while True:
    start_game()
    introduction()
    
    
    # get input for player x
    x_input = int(input(f'\nX: {name_list[0]}) Please choose a cell to place your token. 1 - 9: '))
    # update the cell they chose to populate thier token
    b1.update_cell(x_input, 'X')
    start_game()
    introduction()
    # check for x win
    if b1.winner_winner('X'):
        print('Winner, Winner, Chicken Dinner! X wins!')
        play_again = input('Would you like to play again? Please enter "y" for yes and "n" for no: ').lower()
        if play_again == 'y':
            b1.play_again()
            continue
        else:
            break
    # check for a tie
    if b1.tie_board():
        print('The game is a tie!')
        play_again = input('Would you like to play again? Please enter "y" for yes and "n" for no: ').lower()
        if play_again == 'y':
            b1.play_again()
            continue
        else:
            break
    # get input for player O
    o_input = int(input(f'\nO: {name_list[1]}) Please choose a cell to place your token. 1 - 9: '))
    
    # update the cell they chose to populate thier token
    b1.update_cell(o_input, 'O')
    #check for an O win
    if b1.winner_winner('O'):
        print('Winner, Winner, Chicken Dinner! O wins!')
        play_again = input('Would you like to play again? Please enter "y" for yes and "n" for no: ').lower()
        if play_again == 'y':
            b1.play_again()
            continue
        else:
            break
    # check for a tie
    if b1.tie_board():
        print('The game is a tie!')
        play_again = input('Would you like to play again? Please enter "y" for yes and "n" for no: ').lower()
        if play_again == 'y':
            b1.play_again()
            continue
        else:
            break