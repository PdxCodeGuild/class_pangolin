# Taylor Rebbe
# Lab_26 Tic Tac Toe
# 11/11.2019
# This ASCII pic can be found at (ATARI)
# https://asciiart.website/index.php?art=objects/computers

# Supporting Modules
import ttt_classes as t3cls
import time
import random
import os

# Global Variables
board = ['_', '_', '_', '_', '_', '_', ' ', ' ', ' ']
nemesis_board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
player_1 = ''
player_2 = ''

# User messages
message_1 = "Enter a name for player 1: > "
message_2 = "Chose a token ( x or o ): > "
message_3 = "Starting from the top right position, chose a keypad location (0 - 8): > "
error_message = "Invalid input"
validation_1 = ['y', 'n']
validation_2 = ['X', 'O']
validation_3 = range(0, 9)

# Keeps track of remaining moves for palyer 2 "Nemesis"
def nemesis_move_tally(move):
    nemesis_board[move] = '!'
    return nemesis_board

# Runs player 2 "Nemesis" and deployse a move
def nemesis_move():
    choice_list = []
    for i in range(len(nemesis_board)):
        if nemesis_board[i] != '!':
            choice_list.append(nemesis_board[i])
    return random.choice(choice_list)

# Input validation function for strings
def user_input_validation_str(msg, emsg, *args):
    '''This function validates user input.'''
    while True:
        user_input = input(msg).upper()
        if user_input not in args:
            print(f"\n{emsg}")
        else:
            return user_input

# Input validation function for intigers
def user_input_validation_int(msg, emsg, *args):
    '''This function validates user input.'''
    while True:
        user_input = int(input(msg))
        if user_input not in args:
            print(f"\n{emsg}")
        else:
            return user_input

# Creates an AI player 2
def create_player_2_AI(player_1):
    if player_1.__dict__['token'] == 'X':
        return t3cls.Player('Nemesis', 'O')
    else:
        return t3cls.Player('Nemesis', 'X')

# Test Print Game Board
os.system('cls' if os.name == 'nt' else 'clear')
ttt = t3cls.Game(board)
print(ttt)

# User input for player 1
receive_player_name = input(message_1)
receive_player_token = user_input_validation_str(message_2, error_message, *validation_2)

# Creates player 1 and 2
player_1 = t3cls.Player(receive_player_name, receive_player_token)
player_2 = create_player_2_AI(player_1)

# Clear Screen for a freshy
os.system('cls' if os.name == 'nt' else 'clear')
print(f"You're Opponent is Nemesis... Player: {player_1.name} Token: {player_1.token} prepare for certain defeat.")
time.sleep(3)

# Mani game function

# Could use input validation on the positions, and check if keypad position is already full.
def main():
    while True:
        if ttt.is_game_over(ttt.calc_winner(), ttt.is_full()) == False:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(ttt)
            player_1_move = user_input_validation_int(message_3, error_message, *validation_3)
            ttt.move(player_1_move, player_1)
            os.system('cls' if os.name == 'nt' else 'clear')
            if ttt.is_game_over(ttt.calc_winner(), ttt.is_full()) == True:
                if ttt.is_full() == True and ttt.calc_winner() == None:
                    print(ttt)
                    print('Tie Game!')
                else:
                    print(ttt)
                    print(f"Token: {ttt.calc_winner()} is the winner.")
                    break
            print(ttt)
            nemesis_move_tally(player_1_move)
            print('Nemesis is thinking')
            time.sleep(1)
            nemesis = nemesis_move()
            ttt.move(nemesis, player_2)
            if ttt.is_game_over(ttt.calc_winner(), ttt.is_full()) == True:
                if ttt.is_full() == True and ttt.calc_winner() == None:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(ttt)
                    print('Tie Game!')
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(ttt)
                    print(f"Token: {ttt.calc_winner()} is the winner.")
                    break
            nemesis_move_tally(nemesis)
        else:
            break
main()
