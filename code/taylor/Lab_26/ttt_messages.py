# Tic Tac Toe User Messages and Display




''' Win Definition '''

# if [0,1,2] = X or O
# if [0,4,8] = X or O
# if [0,3,6] = X or O
# if [1,4,7] = X or O
# if [2,5,8] = X or O
# if [3,4,5] = X or O
# if [6,7,8] = X or O

message_1 = "Enter a name for player 1: > "
message_2 = "Chose a token (X or O): > "
message_3 = "Starting from the top right position, chose a keypad location (1 - 9): > "
error_message = "Invalid input"
validation_1 = ['y', 'n']
validation_2 = ['x', 'o']

def user_input_validation(msg, emsg, *args):
    '''This function validates user input.'''
    while True:
        user_input = input(msg).lower()
        if user_input.lower() not in args:
            print(f"\n{emsg}")
        else:
            return user_input 

            