# Shawn Stolsig
# PDX Code Guild 
# Assignment: Intro Class Lab 8 - Guess the Number
# Date: 10/24/2019

import random

# select computer random number between 1 and 10
game_range = 10   # use this to select upper limit of range.  1 will be hardcoded as lower limit
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
    user_guess = int(input(f"please select number between 1 and {game_range}: "))

    # win condition
    if user_guess == computer_number:
        # handle first guess differently
        if loop_counter == 0:
            print(f"you win!  you guessed the computer's number on your first guess!")
        else:
            print(f"you win!  you guessed the computer's number after {loop_counter + 1} guesses!")
        exit()
    
    # if not a win:
    # if first attempt, initialize previous_guess_variation
    if loop_counter == 0:
        prev_guess_variation = abs(user_guess - computer_number)
        print("that was your first guess!  keep going...")
        # print(f"loop: {loop_counter} prev_guess_variation: {prev_guess_variation}")

    #if not first attempt, give the user "hotter or colder"
    else:
        if prev_guess_variation > abs(user_guess - computer_number):
            print("getting warmer!")
        elif prev_guess_variation == abs(user_guess - computer_number):
            print("no improvement :(")
        else:
            print("getting colder")
        # reset previous guess variation
        prev_guess_variation = abs(user_guess - computer_number)

    # increment counter
    loop_counter += 1

# print out "you lose" since there have been more than loop_counter attempts
print(f"you lose!  it took you more than {loop_counter} attempts")