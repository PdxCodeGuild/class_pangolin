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

# function for getting hand value
def get_hand_value(hand):
    ''' parameters: list of cards (representing a player's hand)
        return: list of ints of the possible hand values '''

    # declare return list for values
    values = []

    # add up all the cards
    sum = 0

    # a counter for the number of aces in the hand
    ace_counter = 0

    # iterate through each card in the hand
    for card in hand:
        # need to handle 10 different since it's key has two characters
        if card[0] == '1':
            # look up value of a 10 card from dictionary 
            sum += card_values['10']
        # need to handle Aces different since they can have two values
        elif card[0] == 'A':
            # increment ace counter
            ace_counter += 1
            # look up value of card (an ace) from dictionary
            sum += card_values[card[0]]
        # if not an ace or a 10
        else:
            # look up value of card from dictionary
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
    ''' arguments: (none, pulls from global variable deck) 
        return: a string of the card IDs '''
    
    # access the global variable, deck 
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
    ''' argument: int representing number of players
        returns: list nested with lists, each nested list is a player's hand) '''

    # declare return list of the cards after the first deal
    delt_cards = []

    # for each player, deal two cards.  this will be a nested list in delt_cards
    # using players + 1 since there will be a computer player/house in addition to user
    for i in range(0,players + 1):
        delt_cards.append( [get_card(), get_card()]  )

    #delt_cards.append( ['AC', '3C'])                ####### extra player with aces every time
    return delt_cards

# function for one player to take hits or stand
def play_hand(player_id):
    ''' arguments: player's id/index 
        return: none '''
    
    # if dealer is playing (player_id == 0)
    if player_id == 0: 
        # get value of hand
        hand_value_list = get_hand_value(the_deal[player_id])

        # print cards and value of cards
        print(f"\nDealer's hand is: ", end = " ")
        print(f"{the_deal[player_id]} with value(s) of {hand_value_list}")

        # print dealer's advice
        dealer_action = get_deal_advice(hand_value_list)
        print(f"Dealer will {dealer_action}")
        
        # continue to loop while not given input of 'stay' or 'hold' 
        while dealer_action not in ['stay', 'bust', 'blackjack!']:
            the_deal[player_id].append(get_card())
            hand_value_list = get_hand_value(the_deal[player_id])
            print(f"Dealer hit and now has {the_deal[player_id]} with value(s) of {hand_value_list}")
            dealer_action = get_deal_advice(hand_value_list)          
            print(f"Dealer will now {dealer_action}")

    # else if player is playing (player_id != 0)
    else: 
        # get value of hand
        hand_value_list = get_hand_value(the_deal[player_id])

        # print cards and value of cards
        print(f"\nPlaying Hand {player_id}: ", end = " ")
        print(f"{the_deal[player_id]} with value(s) of {hand_value_list}")

        # print dealer's advice
        dealer_advice = get_deal_advice(hand_value_list)
        if dealer_advice == 'blackjack!':
            print("Congrats on blackjack! You win now.") 
        else:
            print(f"Dealer says: {dealer_advice}")

            # get user's input on next action
            user_choice = input("Tell dealer what to do: ")
            
            # continue to loop while not given input of 'stay' or 'hold' 
            while user_choice not in ['stay', 'Stay', 's', 'hold', 'Hold', 'h', 'bust', 'stand']:
                the_deal[player_id].append(get_card())
                hand_value_list = get_hand_value(the_deal[player_id])
                print(f"{the_deal[player_id]} with value(s) of {hand_value_list}")

                # get dealer advice
                dealer_advice = get_deal_advice(hand_value_list)
                print(f"Dealer says: {dealer_advice}")
                if dealer_advice == 'bust':
                    print("Sorry, you busted.  You lose now.")
                    break
                else:
                    user_choice = input("Now what? ")

# function to return advice from the dealer to the player
def get_deal_advice(hand_value):
    ''' argument: a list of hand values
        returns: a string regarding what the player should do '''

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
    ''' arguments: number of decks to play with
        return: none(this will build global variable deck) '''

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
def display_cards():
    ''' arguments: nested list of delt cards
        returns: none (prints out cards) '''
   
    # access global deal variable
    global the_deal

    # show dealer's cards
    print(f"           Dealer is showing {the_deal[0][0]}")

    # show each player's hand
    for card in range(1,len(the_deal)):
        # print(f"dealt_cards[card] is {dealt_cards[card]}")
        print(f"Hand {card}: {the_deal[card]}", end = "   ")
    print()

# function for printing winners
def print_winning_hands():
    ''' arguments: none
        returns: none (prints the results of the hand, who beats/loses to the dealer '''

    # dealt_cards is a nested list, with index 0 is dealer's hand, remaining indicies represent the other hands

    # case: dealer busted
    if get_best_value(get_hand_value(the_deal[0])) > 21:
        print("Dealer busted!  Checking player hands...")
        for i in range(1,len(the_deal)):
            if get_best_value(get_hand_value(the_deal[i])) <= 21:
                print(f"Hand {i} not busted...beats dealer!")
            elif get_best_value(get_hand_value(the_deal[i])) > 21:
                print(f"Hand {i} busted...loses to dealer!")
        print()
    
    # if dealer did not bust:
    else:
        print("Dealer did not bust, checking player hands...")
        for i in range(1,len(the_deal)):
            # case: player busts
            if get_best_value(get_hand_value(the_deal[i])) > 21:
                print(f"Hand {i} busted...loses to dealer!")
            # case: player wins
            elif get_best_value(get_hand_value(the_deal[i])) > get_best_value(get_hand_value(the_deal[0])):
                print(f"Hand {i} higher than dealer's...beats dealer!")                
            # case: player loses
            elif get_best_value(get_hand_value(the_deal[i])) < get_best_value(get_hand_value(the_deal[0])):
                print(f"Hand {i} lower than dealer's...loses to dealer!") 
            # case: player ties/pushes with dealer
            else: 
                print(f"Hand {i} is the same as the dealers....push") 
        print()   

# function for scrubbing bust values from list of values and returning highest value
def get_best_value(hand_values):
    ''' arguments: takes a list of potential hand values
        return: int of the best value in the hand '''

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


# global variables
deck = []               # main deck of un-dealt cards (list of strings)
the_deal = []           # the delt cards (nested list, inside is a list of each player's hands)


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
    the_deal = deal(number_of_players)

    # print first deal
    display_cards()

    # play each hand
    for player in range(1,number_of_players+1):
        play_hand(player)

    # play dealer hand
    play_hand(0)

    # print off which hands won
    print_winning_hands()

    # Play again?
    if not input("Press enter to quit or input anything to play again: "):
        break

print("Game is ending.")