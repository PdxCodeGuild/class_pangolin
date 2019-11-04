# Shawn Stolsig
# PDX Code Guild 
# Assignment: Intro Class Lab 8 - Guess the Number
# Date: 10/24/2019

import random

# select computer random number between 1 and 10
game_range = 10   # use this to select upper limit of range.  1 will be hardcoded as lower limit

# (
#  There are two game modes, one where user selects number and one where computer selects number.
#  Each mode will have be defined in it's own function, computerPlayer or userPlayer
# )

#################  traditional came mode with user as the player/guesser  ##############################################
def userPlayer():
    computer_number = random.randint(1,game_range)

    # uncomment for cheat mode
    # print(f"computer_number is {computer_number}")

    # game loop counter
    loop_counter = 0

    # keep track of how close previous guess was
    prev_guess_variation = 0

    # main game loop
    while loop_counter < 10:

        # get user input
        user_guess = int(input(f" please make a guess between 1 and {game_range}: "))

        # win condition
        if user_guess == computer_number:
            # handle first guess differently
            if loop_counter == 0:
                print(f"you win!  you guessed the computer's number on your first guess!")
            else:
                print(f"you win!  you guessed the computer's number after {loop_counter + 1} guesses!")
            return
        
        # message strings
        message_start = ''
        message_end = ''

        # if first guess
        if loop_counter == 0:
            message_start = "your first guess, keep going"
            prev_guess_variation = abs(user_guess - computer_number)
        else:
            message_start = 'too high! ' if user_guess > computer_number else 'too low! '
            if prev_guess_variation > abs(user_guess - computer_number):
                message_end = "getting warmer"
            elif prev_guess_variation == abs(user_guess - computer_number):
                message_end = "no improvement"
            else:
                message_end = "getting colder"
            # reset previous guess variation
            prev_guess_variation = abs(user_guess - computer_number)     

        # print message and increment counter
        print(message_start + message_end)
        loop_counter += 1

    # print out "you lose" since there have been more than loop_counter attempts
    print(f"you lose!  it took you more than {loop_counter} attempts")
    return
######################################################################################################################

#################################### Computer player mode ############################################################
def computerPlayer():
    # get input number from user
    while True:
        user_number = int(input(f"input a number for the computer to guess! between 1 and {game_range}: "))
        if user_number in range(1,game_range+1):
            break
        else:
            print("invalid input, try again")

    # game loop counter
    loop_counter = 0

    # initialize range_lower and range_upper for intelligent guessing
    range_lower = 1
    range_upper = game_range

    # main game loop
    while loop_counter < 10:

        # get computer guess input
        computer_guess = random.randint(range_lower, range_upper)
        print(f"computer guessed: {computer_guess}")

        # win condition
        if user_number == computer_guess:
            # handle first guess differently
            if loop_counter == 0:
                print(f"computer wins! computer guessed your number on first guess!")
            else:
                print(f"computer wins!  computer guessed your number after {loop_counter + 1} guesses!")
            return
        
        # if not a win:
        else:
            if computer_guess > user_number:
                print(f"too high!")
                range_upper = computer_guess
            else:
                print(f"too low!")
                range_lower = computer_guess

        # increment counter
        loop_counter += 1

    # print out "you lose" since there have been more than loop_counter attempts
    print(f"computer loses, you win!  it took computer more than {loop_counter} attempts")
    return    


######################################################################################################################


# main loop

keep_playing = True
while keep_playing:

    while True:
        # get desired game mode
        mode_select = input("input 1 to have user guess, input 2 to have computer guess: ")

        # start selected game mode
        if mode_select == '1':
            userPlayer()
            break
        elif mode_select == '2':
            computerPlayer()
            break
        else:
            print("invalid input, please try again")

    # see if user wants to play again
    if input("input anything to play again or press enter to quit "):
        pass
    else:
        keep_playing = False

print("goodbye!")