# Write a python program to give basic blackjack playing advice during a game by asking the player for cards.
# A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K
# Aces are worth one point in this version.
"""
Less than 17, advise to "Hit"
Greater than or equal to 17, but less than 21, advise to "Stay"
Exactly 21, advise "Blackjack!"
Over 21, advise "Already Busted"
"""


# This function's job is to determine if the input is done, ace, jack, queen or king and if so, return a value to user_hand.
def findUserHand():
    if user_input == "done":
        return False
    elif user_input == "ace":
        return user_hand.append("1")
    elif user_input == "jack" or user_input == "queen" or user_input == "king":
        return user_hand.append("10")
    else:
        return user_hand.append(int(user_input))


# This function's job is to determine if the user should Hit, Stay, has a Blackjack, or Busted based on the value in
# int().
def printUserHand():
    if user_hand < 17:
        return f"{user_hand} You should Hit."
    elif user_hand >= 17 and user_hand < 21:
        return f"{user_hand} You should Stay."
    elif user_hand == 21:
        return f"{user_hand} Blackjack!"
    else:
        return f"{user_hand} Busted"


# Sets the input to a blank string
user_input = ""
# Sets the hand list to a blank list
user_hand = []
# A while loop is used to ask the user about which cards they have in their hand.
# Calls the findUserHand function, converts the list of strings to integers
# Sums the list of integers and calls the printUserHand function to determine the results.
while user_input != "done":
    user_input = input("Which cards do you have? Type 'done' to stop. ")
    findUserHand()
    user_hand = [int(x) if x != 0 else x for x in user_hand]
user_hand = sum(user_hand)
print(printUserHand())