#Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards. 
#First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). 
#Then, figure out the point value of each card individually. 
#Number cards are worth their number, all face cards are worth 10. 
#At this point, assume aces are worth 1. Use the following rules to determine the advice:
#Less than 17, advise to "Hit"
#Greater than or equal to 17, but less than 21, advise to "Stay"
#Exactly 21, advise "Blackjack!"
#Over 21, advise "Already Busted"

def blackjack():
    #take user card input, upper() on all to match dictionary keys
    card1= input("What is your first card?\n").upper()
    card2= input("What is your second card?\n").upper()
    card3= input("What is your third card?\n").upper()
    #range for stay to make it easy
    stay_range = range(17,21)
    #made a dictionary of card values, reassign values from dictionary
    card_values_dict = {'A': 1, '2': 2, '3':3, '4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    card_values_dict.update(dict.fromkeys(['10','J','Q','K'], 10))
    card1_value = card_values_dict.get(card1)
    card2_value = card_values_dict.get(card2)
    card3_value = card_values_dict.get(card3)
    #print to test values are correct
    #print(card1_value, card2_value, card3_value)
    
    if card1 not in card_values_dict.keys() or card2 not in card_values_dict.keys() or card3 not in card_values_dict.keys(): # Fix the 'or's.  Causing invalid response. Truthy ors.
        print("Not a valid card.")
        return
    else: #begin evaluation
        total_value = card1_value + card2_value + card3_value #add card values to determine hand
        if total_value < 17: # lower than 17 needs to hit
            return print('HIT!')
        if total_value in stay_range: # between 17 and 20 can stay, uses stay_range variable
            return print('Stay!')
        if total_value == 21: #blackjack
            return print('Ohh baby! You got BlackJack!')
        if total_value > 21: #busted message
            return print('Busted...')
blackjack()