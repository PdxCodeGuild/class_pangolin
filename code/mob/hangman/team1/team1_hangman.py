

import random
import string

# function for opening/initializing file
def file_init(filename, word_length):
    ''' parameters: filename as a string, word_length
        return: list of strings of words over input word_length '''

    n_words_or_greater = []

    with open(filename, 'r') as f:
        dictionary_list = list(f.read().split('\n'))
    for i in range(len(dictionary_list)):
        if len(dictionary_list[i]) >= word_length:
            n_words_or_greater.append(dictionary_list[i])

    return n_words_or_greater

# function for getting target word
def get_target_word(list_of_words):
    ''' parameters: list of strings, each a potential target word
        return: a random target word '''

    target_word = random.choice(list_of_words)
    print(f"target_word is {target_word}")
    return target_word

# function for getting list of dashes based on target word
def get_dash_list(target_word):
    ''' parameters: target word as a string
        return: a list of strings (initialized as underscores) '''
    return ['_' for letter in target_word]

# function for playing through one guess/round
def play_one_round(target_word, dash_list, letters_guessed):
    ''' parameters: target word as string, number of choices remaining as int, dash list as list of strings, and letters guessed as list of strings
        return: updated dash list and letters guessed '''
    
    # get input
    while True:
        user_input = input("Guess a letter: ")

        # check if input has already been guessed
        if user_input in letters_guessed:
            print(f"You already guessed {user_input}!")
        
        # check that input is a letter
        elif user_input in string.ascii_letters and len(user_input) == 1:
            # make the input lower case
            user_input = user_input.lower()
            # break from input for loop
            break

        # else, bad input message
        else:
            print(f"{user_input} is not valid input...must be a single letter")

    # declare modifier for num_guesses
    num_guesses_mod = 1

    # iterate through target word indexes
    for i in range(len(target_word)):
        # if input character equals target_word[i]
        if user_input == target_word[i]:
            # set dash_list[i] equal to input char
            num_guesses_mod = 0
            dash_list[i] = user_input

    # add input letter to letters guessed
    letters_guessed.append(user_input)


    # return dash list and letters guessed as a tuple
    return  dash_list, letters_guessed, num_guesses_mod

# function for checking if there's a win
def check_for_win(dash_list):
    ''' parameters: dash list as a list of strings
        return: true/false if game is over '''
    if "_" in dash_list:
        return False
    else:
        return True    


# dash_list  is list of either dashes or correct letters guessed
# target_word is string of the word the player is trying to guess
# num_guesses is an int (starting at 10) of how many guesses remain
# letters_guessed is a list of letters of both correct and incorrect letters that have been guessed




# main 
target_word = get_target_word(file_init('english.txt', 5))
dash_list = get_dash_list(target_word)
num_guesses = 10
num_guesses_mod = 0
letters_guessed = []

print(dash_list)

while not check_for_win(dash_list):


    dash_list, letters_guessed, num_guesses_mod = play_one_round(target_word,dash_list, letters_guessed)
    print(dash_list)
    print(f"already guessed: {letters_guessed}")

    num_guesses -= num_guesses_mod
    print(f"# guessed remaining: {num_guesses}")
    if num_guesses == 0:
        print("You ran out of guesses!")
        break
