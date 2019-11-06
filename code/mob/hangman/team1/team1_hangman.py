

import random

# function for opening/initializing file
def file_init(filename, word_length):
    ''' parameters: filename as a string, word_length
        return: list of strings of words over input word_length '''

    return

# function for getting target word
def get_target_word(list_of_words):
    ''' parameters: list of strings, each a potential target word
        return: a random target word '''

    return

# function for getting list of dashes based on target word
def get_dash_list(target_word):
    ''' parameters: target word as a string
        return: a list of strings (initialized as underscores) '''

    return

# function for playing through one guess/round
def play_one_round(target_word, num_of_choices, dash_list, letters_guessed):
    ''' parameters: target word as string, number of choices remaining as int, dash list as list of strings, and letters guessed as list of strings
        return: updated dash list and letters guessed '''
    
    return

# function for checking if there's a win
def check_for_win(dash_list):
    ''' parameters: dash list as a list of strings
        return: true/false if game is over '''

    return


# dash_list  is list of either dashes or correct letters guessed
# target_word is string of the word the player is trying to guess
# num_guesses is an int (starting at 10) of how many guesses remain
# letters_guessed is a list of letters of both correct and incorrect letters that have been guessed