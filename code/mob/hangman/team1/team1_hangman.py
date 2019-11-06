import random
import string
import os
import you_lose

# function for opening/initializing file
def file_init(filename, word_length):
    ''' parameters: filename as a string, word_length
        return: list of strings of words over input word_length '''
    # declare empty list for list of words
    n_words_or_greater = []

    # open file using passed filename
    with open(filename, 'r') as f:
        # store file as list of strings, each string its own newline
        dictionary_list = list(f.read().split('\n'))

    # filtering words greater >= word length, appending to return list
    for i in range(len(dictionary_list)):
        if len(dictionary_list[i]) >= word_length:
            n_words_or_greater.append(dictionary_list[i])

    # returning list
    return n_words_or_greater

# function for getting target word
def get_target_word(list_of_words):
    ''' parameters: list of strings, each a potential target word
        return: a random target word '''

    target_word = random.choice(list_of_words)
    # print(f"target_word is {target_word}")        ## for cheat mode, uncomment this
    return target_word

# function for getting list of dashes based on target word
def get_dash_list(target_word):
    ''' parameters: target word as a string
        return: a list of strings (initialized as underscores) '''
    return ['_' for letter in target_word]

# function for checking if there's a win
def check_for_win(dash_list):
    ''' parameters: dash list as a list of strings
        return: true/false if game is over '''
    if "_" in dash_list:
        return False
    else:
        return True

# function to validate user input
def user_input_validation(msg, emsg, *args):
    '''This function validates user input.'''
    while True:
        user_input = input(msg).lower()
        if user_input.lower() not in args:
            print(f"\n{emsg}")
        else:
            return user_input    

# function for playing through one guess/round
def play_one_round(target_word, dash_list, letters_guessed):
    ''' parameters: target word as string, number of choices remaining as int, dash list as list of strings, and letters guessed as list of strings
        return: updated dash list, letters guessed, and num_guesses modifier as tuple '''
    
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

    # return dash list, letters guessed, and a num_guesses modifier (1 or 0) as a tuple
    return  dash_list, letters_guessed, num_guesses_mod

# function for printing to console
def display_game(target_word, dash_list, num_guesses, letters_guessed):
    ''' parameters: target word (string), dash list (list), num guesses (int), letters guessed (list)
        return: none (justs prints game) '''

    # first, clear terminal window
    os.system('cls' if os.name == 'nt' else 'clear')

    # print hangman gallows scene based on how many guesses are left
    hangman_art = [you_lose.reaper, you_lose.one, you_lose.two, you_lose.three, you_lose.four, you_lose.five, you_lose.six, you_lose.seven, you_lose.eight, you_lose.nine, you_lose.ten]
    print(hangman_art[num_guesses])

    # print out each letter in dash list seperated by white space
    for letter in dash_list:
        print(letter, end=' ')
    print()     # prints newline since we are ending each letter with just a ' '

    # print number of guesses remaining: 
    print(f"# of guesses remaining: {num_guesses}")

    # print list of already guessed letters
    print("already guessed: ", end=' ')
    for letter in letters_guessed:
        print(letter, end=', ')
    print()     # prints newline since we are ending each letter with just a ' '

    # return none
    return 

# function playing whole game (one word) of hangman
def play_hangman(word_length):
    # variables to be passed to user input validation function later
    message_1 = "Do you want to play again? "
    error_message = "Invalid input, enter (y or n) "
    validation = ['y', 'n']

    # setting up variables needed for one game of hangman
    # string that player is trying to guess
    target_word = get_target_word(file_init('english.txt', word_length))
    # list that will hold correctly guessed letters
    dash_list = get_dash_list(target_word)
    # nuber of guesses remaining
    num_guesses = 10
    # a modifier used to change number of guesses for each letter guessed
    num_guesses_mod = 0
    # a list for tracking characters guessed
    letters_guessed = []

    # continue looping while game is not yet won
    while not check_for_win(dash_list):
    
        # print out current list of underscores or correctly guessed characters
        display_game(target_word,dash_list,num_guesses,letters_guessed)

        # play one letter, update number guessed with the returned modifier
        dash_list, letters_guessed, num_guesses_mod = play_one_round(target_word,dash_list, letters_guessed)
        num_guesses -= num_guesses_mod

        # if you've run out of guesses, you lose
        if num_guesses == 0:
            display_game(target_word,dash_list,num_guesses,letters_guessed)
            print(f"You ran out of guesses! You lose! Target word was: {target_word}")
            break
        # if you've won, print out winning message
        if check_for_win(dash_list):
            print(f"You win! Target word was {target_word}")

    # see if user wants to play again
    return user_input_validation(message_1, error_message, *validation)

# main game loop
while True:
    if play_hangman(5) == 'n':
        break
    print("Playing another round.")
print("Game Over.")




