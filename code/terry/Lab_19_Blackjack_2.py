# Write a python program to give basic blackjack playing advice during a game by asking the player for cards.
# A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K
# Aces are worth one point in this version.
"""
Less than 17, advise to "Hit"
Greater than or equal to 17, but less than 21, advise to "Stay"
Exactly 21, advise "Blackjack!"
Over 21, advise "Already Busted"
"""

# This dictionary contains the card face as a string and the card's value as an integer.
card_opt = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,}

user_input = ""

user_hand = []

while user_input != "done":

    user_input = input("Which cards do you have? Type 'done' to stop. ")
    if user_input == "done":
        break
    elif user_input == "ace":
        user_hand.append("1")
    elif user_input == "jack" or user_input == "queen" or user_input == "king":
        user_hand.append("10")
    else:
        user_hand.append(int(user_input))

    user_hand = [int(x) if x != 0 else x for x in user_hand]

user_hand = sum(user_hand)
if user_hand < 17:
    print(f"{user_hand} You should Hit.")
elif user_hand >= 17 and user_hand < 21:
    print(f"{user_hand} You should Stay.")
elif user_hand == 21:
    print(f"{user_hand} Blackjack!")
else:
    print(f"{user_hand} Busted")