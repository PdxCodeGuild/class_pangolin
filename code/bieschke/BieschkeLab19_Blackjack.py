#Bieschke Lab 19 Blackjack Advice 
'''
Gives the player 2 cards from the list, adds them, compares them to 21, and asks
if the player wants a third card, compares to 21. Compares this total to the house's
hand, and tells the player if they've beaten the house.
'''
import random

cards = {
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10
}

#can action and house be the only functions if I use *args/*kwargs? YES
#But you have to write a for loop to go through the input
def action(x, y):
    global p_sum
    global h_sum
    
    p_sum = cards[x] + cards[y]
    if p_sum < 16:
        print(f"{p_sum} Hit")
    elif 21 > p_sum >= 16:
        print(f"{p_sum} Stay")
    elif p_sum == 21:
        print(f"{p_sum} Blaaaaackjaaaaaack!")
    else:
        print(f"{p_sum} Busted!")

def action2(x, y, z):
    global p_sum
    global h_sum
    p_sum = cards[x] + cards[y] + cards[z]
    if p_sum < 16:
        print(f"{p_sum} Hit")
    elif 21 > p_sum >= 16:
        print(f"{p_sum} Stay")
    elif p_sum == 21:
        print(f"{p_sum} Blaaaaackjaaaaaack!")
    else:
        print(f"{p_sum} Busted!")

def house(a, b):
    global p_sum
    global h_sum
    
    h_sum = cards[a] + cards[b]
    if h_sum <= 16:
        pass        
    elif 21 >= h_sum >= 17 :
        print(f"House has {h_sum}")
        scoring()
    elif h_sum == 21:
        print(f"House has {h_sum} Blackjack!")
        scoring()
    else:
        print(f"{h_sum} House Busted!")
        scoring()

def house2(a, b, c):
    global p_sum
    global h_sum
    h_sum = cards[a] + cards[b] + cards[c]
    if 21 > h_sum:
        print(f"House has {h_sum}")
    elif h_sum == 21:
        print(f"House has {h_sum} Blackjack!")
    else:
        print(f"{h_sum} House Busted!")

def scoring():
    global p_sum
    global h_sum
    print(f"{p_sum} is your total.")
    print(f"{h_sum} is the House's total.")

    if 21 >= h_sum > p_sum:
        print("House wins")
    elif h_sum == p_sum:
        print("TIE!")
    elif h_sum > 21:
        print("House BUSTED!!!")
    elif p_sum > 21:
        print("BUSTED!!!")
    else:
        print("YOU WIN!!!")

#setting these as global or local variables (to scoring())
#makes their values equal to 0 at the end of the script. please advise.
p_sum = 0
h_sum = 0

print("Let's play some blackjack!") 
card1 = random.choice(list(cards.keys())).upper()
card2 = random.choice(list(cards.keys())).upper()

h_card1 = random.choice(list(cards.keys())).upper()
h_card2 = random.choice(list(cards.keys())).upper()
house(h_card1, h_card2)

h_card3 = random.choice(list(cards.keys())).upper()
house2(h_card1, h_card2, h_card3)

print(f"You have two cards: {card1} and {card2}")
action(card1, card2)
hitter = input("Do you want another card?")

if hitter == "yes":
    card3 = random.choice(list(cards.keys())).upper()
    action2(card1, card2, card3)
    scoring()
else:
    scoring()