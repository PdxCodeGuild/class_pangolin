# Supporting Modules
import ttt_messages as t3msg    
import ttt_classes as t3cls

# Global Variables
board = ['_', '_', '_', '_', '_', '_', ' ', ' ', ' ']
player_1 = ''
player_2 = ''

# User messages
message_1 = "Enter a name for player 1: > "
message_2 = "Chose a token ( x or o ): > "
message_3 = "Starting from the top right position, chose a keypad location (1 - 9): > "
error_message = "Invalid input"
validation_1 = ['y', 'n']
validation_2 = ['x', 'o']

# Input Validation Function
def user_input_validation(msg, emsg, *args):
    '''This function validates user input.'''
    while True:
        user_input = input(msg).lower()
        if user_input.lower() not in args:
            print(f"\n{emsg}")
        else:
            return user_input 

# Creates an AI player 2
def create_player_2_AI(player_1):
    if player_1.__dict__['token'] == 'x':
        return t3cls.Player('Nemesis', 'o')
    else:
        return t3cls.Player('Nemesis', 'x')

# Test
print(t3cls.Game(board))

receive_player_name = input(message_1)
receive_player_token = user_input_validation(message_2, error_message, *validation_2)


player_1 = t3cls.Player(receive_player_name, receive_player_token)
player_2 = create_player_2_AI(player_1)



print('\n####################*******PLAYERS*****#########################')

print(player_1.__dict__)
print(player_2.__dict__)











# Main function
def main():
    return None

# 1) Take in player inofrmaiton name, token
# 2) Print the Empty board

# Game Loop -

# 3) Ask player 1 to move
    # - is the space available? True = allow
    # else "Location is full"
# 4) Move player 2 (Random Choice)
    # sets new value to game board per user request

# 5) run is_game_over() to determine board is full or there was a winner.
    # 5a) run calc_winner to check for win.
        # -itterate through list if / else for win 3*x or o in a row
    # 5b) Run calc to check if board full.
        # -itterate through list to check if '_' or ' 'remaining.