# Shawn Stolsig
# PDX Code Guild 
# Assignment: Lab 19 - Blackjack Advice
# Date: 10/25/2019

# you could make a while loop instead of only requiring three cards
# make it a whole blackjack game by making the computer the house
# select how many decks to play with

import random

# dictionary for card values.  create two values for aces (worth 1 and 11 points)
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
def get_hand_value(cards):
    ''' function is passed a list of cards and returns a list of ints of the possible hand values '''
    pass

# function to get a card from the deck
def get_card(deck):
    ''' function will pull card from deck: gets list of cards, returns a string of the card ID'''
    # shuffle deck 
    random.shuffle(deck)

    # return/pop card off end
    return deck.pop()

# function for starting a round of 21
def deal(players, deck):
    ''' function is passed the number of players and the deck, and returns a list of lists (each nested list will be a player's hand) '''

    # declare return list of the cards after the first deal
    delt_cards = []

    # for each player, deal two cards.  this will be a nested list in delt_cards
    # using players + 1 since there will be a computer player/house in addition to user
    for i in range(0,players + 1):
        delt_cards.append( [get_card(deck), get_card(deck)]  )

    return delt_cards

# function for one player to take hits or stand
def play_hand(player_id):
    ''' function will recieve a player's id/index, and return a list of their final hand '''
    pass

# function to return advice from the dealer to the player
def get_deal_advice(hand_value):
    ''' function will recieve a hand value and return a string regarding what the player should do '''
    pass

# build the deck, based on how many decks the user wants to play with
def build_deck(num_decks):
    ''' when given a number of decks to play with, this will return a list of the cards in the deck '''

    # list of cards in deck to return
    deck_of_cards = []

    # loop based on how many decks they want
    for i in range(0,number_of_decks):
        # for each suit...
        for suit in ['H', 'D', 'S', 'C']:
            # ...push one card of each value (with the suit appended to the end)
            for value in card_values:
                deck_of_cards.append(value + suit)
    
    # return list deck_of_cards
    return deck_of_cards

# function for displaying the current deal
def display_cards(dealt_cards):
    ''' function receives a nested list of delt cards, and prints out the current cards to the screen....no return '''
    pass

# main loop
while True:

    # print start message
    print("\n ****  Welcome to Blackjack!  ****")

    # set up deck
    number_of_decks = int(input("Please input the number of decks you'd like to play with: "))
    deck = build_deck(number_of_decks)

    # get number of players/hands to play 
    number_of_players = int(input("Please input the number of hands you'd like to play: "))

    # deal first two cards to each player
    cards = deal(number_of_players, deck)

    # debugging:
    print(cards)
    print(f"length of deck is now {len(deck)}")

    # program accepts input for desired size of deck and number of hands to be played, and creates a list of cards 
    # for the deck, and creates a nested list of the cards currently delt
    # next steps are to 