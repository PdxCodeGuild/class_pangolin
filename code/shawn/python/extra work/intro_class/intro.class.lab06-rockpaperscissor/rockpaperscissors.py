# Shawn Stolsig
# PDX Code Guild 
# Assignment: Intro Class Lab 6 - Rock, Paper, Scissors
# Date: 10/22/2019



# Rock-Paper-Scissors

# The computer will ask the user for their choice (rock, paper, scissors)
# The computer will randomly choose rock, paper or scissors
# Determine who won and tell the user
# Let's list all the cases:

# rock vs rock (tie)
# rock vs paper
# rock vs scissors
# paper vs rock
# paper vs paper
# paper vs scissors
# scissors vs rock
# scissors vs paper
# scissors vs scissors
# Advanced Version 1
# Catch all tie conditions using a single if conditional.
# Advanced Version 2
# Ask the user if they want to play again, using a while loop.
# Advanced Version 3
# Use a dictionary where each key is one of the choices, and the value associated with the key is a list containing the two other choices.

import random 

print("************************")
print("* Rock Paper Scissors! *")
print("************************")

# use dictionary to define choices
# key is the choice, value[0] is what beats it, value[1] is what it beats
# using tuples for each one since n = 0 indicates what beats it, n = 1 indicates what you beat
choices = {
    'rock': ('paper', 'scissors'),
    'paper': ('scissors', 'rock'),
    'scissors': ('rock', 'paper')
}

# generate random int from 0 to 2 for computer's choice, return as string 'rock', 'paper', or 'scissors'
def generateComputerAnswer():
    randCompChoice = random.randint(0,2)

    if randCompChoice == 0:
        print("Computer chooses rock")
        return 'rock'
    elif randCompChoice == 1:
        print("Computer chooses paper")
        return 'paper'
    elif randCompChoice == 2:
        print("Computer chooses scissors")
        return 'scissors'
    else:
        print("invalid computer choice")
        exit()

# get user's choice
def getUserChoice():
    return input("please type in your choice: " )
    
# compare choices
def findWinner(user, comp):
    # check for tie
    if user == comp:
        return "Tie!"
    
    # check for win
    elif choices[user][1] == comp:
        return "You win!"

    # check for loss
    elif choices[user][0] == comp :
        return 'Computer wins!'

    # edge case
    else:
        print('No combination found...exiting')
        exit()

playAgain = True

# game loop
while playAgain:
    # main game
    print(findWinner(getUserChoice(), generateComputerAnswer()))

    # figure out if user wants to play again
    userWantsToPlayAgain = input("Play again? Please input \"yes\" or \"no\" ")
    if(userWantsToPlayAgain == 'yes'):
        print("Game on!")
        playAgain = True
    elif(userWantsToPlayAgain == 'no'):
        print("Game over...")
        playAgain = False
    else:
        print("You didn't follow directions, play again!")
        playAgain = True
