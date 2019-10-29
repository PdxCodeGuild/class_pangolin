# Shawn Stolsig
# PDX Code Guild 
# Assignment: Lab 19 - Blackjack Advice
# Date: 10/25/2019

# things to fix:
# game only considers aces to be 1s.  figure out how to correctly populate hand values for different permutations of aces = 1 or aces = 11
# hand values are contained in a list, to accound for different permutations of ace values...game winning logic only checks first value in these lists
# maybe instead of passing hand values as a list, use optional arguments instead?

import random

# dictionary for card values
# currently aces will only be worth 1, later version should update this dicationary for both 1 and 11
card_values = {
    '2': 2,
    '3': 3,
    '4': 4, 
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
    'A': 1
}

# make deck a global list
deck = []

# function for getting hand value
def get_hand_value(cards):
    ''' function is passed a list of cards and returns a list of ints of the possible hand values '''

    # declare return list for values
    values = []

    # add up all the cards
    sum = 0
    ace_counter = 0
    for card in cards:
        # need to handle 10 different since it's key has two characters
        if card[0] == '1':
            sum += card_values['10']
        # need to handle Aces different since they can have two values
        elif card[0] == 'A':
            ace_counter += 1
            sum += card_values[card[0]]
        else:
            sum += card_values[card[0]]
    values.append(sum)

    # add code to handle aces.  duplicate all current values, and add 10 (you would only ever count one ace as 11)
    if ace_counter >= 1:
        counter = len(values) - 1   # breaking out an index here to prevent infinite loop
        while counter >= 0:
            values.append(values[counter] + 10)
            counter -= 1

    # return value of cards
    return values

# function to get a card from the deck
def get_card():
    ''' function will pull card from global deck, returns a string of the card ID'''
    global deck

    # return/pop card off end
    return_card = deck.pop()

    # check if deck is empty, quit if so
    if len(deck) == 0:
        print("Your deck wasn't large enough, you removed all the cards.  Quitting")
        exit()

    return return_card

# function for starting a round of 21
def deal(players):
    ''' function is passed the number of players and the deck, and returns a list of lists (each nested list will be a player's hand) '''

    # declare return list of the cards after the first deal
    delt_cards = []

    # for each player, deal two cards.  this will be a nested list in delt_cards
    # using players + 1 since there will be a computer player/house in addition to user
    for i in range(0,players + 1):
        delt_cards.append( [get_card(), get_card()]  )

    #delt_cards.append( ['AC', '3C'])                ####### extra player with aces every time
    return delt_cards

# function for one player to take hits or stand
def play_hand(player_id, dealt_cards):
    ''' function will recieve a player's id/index and the dealt cards, and return a list of their final hand '''
    
    # if dealer is playing (player_id == 0)
    if player_id == 0: 
        # get value of hand
        hand_value_list = get_hand_value(dealt_cards[player_id])

        # print cards and value of cards
        print(f"\nDealer's hand is: ", end = " ")
        print(f"{dealt_cards[player_id]} with value(s) of {hand_value_list}")

        # print dealer's advice
        dealer_action = get_deal_advice(hand_value_list)
        print(f"Dealer will {dealer_action}")
        
        # continue to loop while not given input of 'stay' or 'hold' 
        while dealer_action not in ['stay', 'bust', 'blackjack!']:
            dealt_cards[player_id].append(get_card())
            hand_value_list = get_hand_value(dealt_cards[player_id])
            print(f"Dealer hit and now has {dealt_cards[player_id]} with value(s) of {hand_value_list}")
            dealer_action = get_deal_advice(hand_value_list)          
            print(f"Dealer will now {dealer_action}")

    # else if player is playing (player_id != 0)
    else: 
        # get value of hand
        hand_value_list = get_hand_value(dealt_cards[player_id])

        # print cards and value of cards
        print(f"\nPlaying Hand {player_id}: ", end = " ")
        print(f"{dealt_cards[player_id]} with value(s) of {hand_value_list}")

        # print dealer's advice
        print(f"Dealer says: {get_deal_advice(hand_value_list)}")

        # get user's input on next action
        user_choice = input("Tell dealer what to do: ")
        
        # continue to loop while not given input of 'stay' or 'hold' 
        while user_choice not in ['stay', 'Stay', 's', 'hold', 'Hold', 'h', 'bust', 'stand']:
            dealt_cards[player_id].append(get_card())
            hand_value_list = get_hand_value(dealt_cards[player_id])
            print(f"{dealt_cards[player_id]} with value(s) of {hand_value_list}")
            print(f"Dealer says: {get_deal_advice(hand_value_list)}")
            if get_deal_advice(hand_value_list) == 'bust':
                break
            else:
                user_choice = input("Now what? ")

# function to return advice from the dealer to the player
def get_deal_advice(hand_value):
    ''' function will recieve a list of hand value and return a string regarding what the player should do '''



    # if only one potential value in hand (ie, no aces)
    if get_best_value(hand_value) < 17:
        return 'hit!'
    elif get_best_value(hand_value) >= 17 and get_best_value(hand_value) < 21:
        return 'stay'
    elif get_best_value(hand_value) == 21:
        return 'blackjack!'
    else:
        return 'bust'

# build the deck, based on how many decks the user wants to play with
def build_deck(num_decks):
    ''' when given a number of decks to play with, this will build global variable deck '''
    # use global deck variable
    global deck


    # loop based on how many decks they want
    for i in range(0,number_of_decks):
        # for each suit...
        for suit in ['H', 'D', 'S', 'C']:
            # ...push one card of each value (with the suit appended to the end)
            for value in card_values:
                deck.append(value + suit)
    
    # shuffle deck 
    random.shuffle(deck)

# function for displaying the current deal
def display_cards(dealt_cards):
    ''' function receives a nested list of delt cards, and prints out the current cards to the screen....no return '''

    # show dealer's cards
    print(f"           Dealer is showing {dealt_cards[0][0]}")

    # show each player's hand
    for card in range(1,len(dealt_cards)):
        # print(f"dealt_cards[card] is {dealt_cards[card]}")
        print(f"Hand {card}: {dealt_cards[card]}", end = "   ")
    print()

# function for printing winners
def print_winning_hands(dealt_cards):
    # dealth_cards iss a nested list, index 0 is dealer's hand, other index represent the other hands

    # case: dealer busted
    if get_best_value(get_hand_value(dealt_cards[0])) > 21:
        print("Dealer busted!  Checking player hands...")
        for i in range(1,len(dealt_cards)):
            if get_best_value(get_hand_value(dealt_cards[i])) <= 21:
                print(f"Hand {i} not busted...beats dealer!")
            elif get_best_value(get_hand_value(dealt_cards[i])) > 21:
                print(f"Hand {i} busted...loses to dealer!")
        print()
    
    # if dealer did not bust:
    else:
        print("Dealer did not bust, checking player hands...")
        for i in range(1,len(dealt_cards)):
            # case: player busts
            if get_best_value(get_hand_value(dealt_cards[i])) > 21:
                print(f"Hand {i} busted...loses to dealer!")
            # case: player wins
            elif get_best_value(get_hand_value(dealt_cards[i])) > get_best_value(get_hand_value(dealt_cards[0])):
                print(f"Hand {i} higher than dealer's...beats dealer!")                
            # case: player loses
            elif get_best_value(get_hand_value(dealt_cards[i])) < get_best_value(get_hand_value(dealt_cards[0])):
                print(f"Hand {i} lower than dealer's...loses to dealer!") 
            # case: player ties/pushes with dealer
            else: 
                print(f"Hand {i} is the same as the dealers....push") 
        print()   

# function for scrubbing bust values from list of values and returning highest value
def get_best_value(hand_values):
    ''' function takes a list of potential hand values and returns an int of the best value '''

    # if only one value and it's a bust, return the bust value
    if len(hand_values) == 1 and hand_values[0] > 21:
        return hand_values[0]

    # declare return value
    return_value = 0

    # find the highest non-bust value
    for value in hand_values: 
        if value > return_value and value < 22:
            return_value = value
    
    # return best value
    return return_value

# main loop
while True:

    # print start message
    print("\n ********  Welcome to Blackjack!  ********")

    # set up deck
    number_of_decks = int(input("Please input the number of decks you'd like to play with: "))
    #number_of_decks = 1
    build_deck(number_of_decks)

    # get number of players/hands to play 
    number_of_players = int(input("Please input the number of hands you'd like to play: "))
    # number_of_players = 2

    # deal first two cards to each player
    cards = deal(number_of_players)

    # print first deal
    display_cards(cards)

    # play each hand
    for player in range(1,number_of_players+1):
        play_hand(player, cards)

    # play dealer hand
    play_hand(0,cards)

    # print off which hands won
    print_winning_hands(cards)

    # Play again?
    if not input("Press enter to quit or input anything to play again: "):
        break

print("Game is ending.")