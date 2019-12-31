'''
Lab 19: Blackjack Advice - Version 1

Purpose/goal: Write a python program to give basic blackjack playing advice during a game by asking the player for cards.
    
    - Ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). - D
    
    - Figure out the point value of each card individually. - D

    - Advice user on whether to hit or stay, whether they won or went bust. - D

'''

# create card_worth dict
card_worth = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 1}

# define blackjack_advice function
def blackjack_advice(x, y, z):
    sum = card_worth[x] + card_worth[y] + card_worth[z]
    # advise user based on their card worth
    if sum < 17:
        advise = f"\n{sum} Ask for another!\n"
    elif 21 > sum >= 17:
        advise = f"\n{sum} You're advised to stay.\n"
    elif sum == 21:
        advise = f"\n{sum} Blackjack! You win!\n"
    else:
        advise = f"\n{sum} You went bust.\n"
    return advise

# welcome user to blackjack advice program
print("\nWelcome to this simple Blackjack Advice program!\nTell the computer which cards you are dealt & do as advised...")

# prompt user for their cards
first_card = input("\nWhat's your first card?: ").upper()
second_card = input("\nWhat's your second card?: ").upper()  
third_card = input("\nWhat's your third card?: ").upper()

# print / call blackjack_advice function / advise user
print(blackjack_advice(first_card, second_card, third_card))
