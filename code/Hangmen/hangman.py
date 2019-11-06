'''Write a program to play hangman. Write a function load_words(path) which read the text from the 
file and return a list of strings which are greater than 5 letters. 
Randomly pick a word from the list. Allow the user 10 gueses.  Keep track of the letters guessed. '''

import random
import os
import string
import re

filename = "english.txt"
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), filename), 'r') as file:
    words = file.read()
words = words.split('\n')



word_list = []
def load_words():
    '''Iterating through a txt file to create a list of all words with punctuation removed
    that are more than five letters or more in length. '''
    for i in range(len(words)):
        if len(words[i]) >= 5 and "'" not in words[i]:
            word_list.append(words[i])
    
    
    #print(word_list)
    return word_list
def game_loop():
    '''Game loop that tracks attempts made, processes the answer word against user guesses and returns
    a new list of underscores with a correct guess replacing the respective underscore.  '''
    counter = 10
    nice_try = []
    while counter > 0:
        user_guess = input(f'{"".join(blanks)}\n{counter} guesses left.\nAlready Guessed:{nice_try}\nGuess a letter>').lower()
        if len(user_guess) > 1 or user_guess not in string.ascii_letters:
            print("Not a valid guess.")
            pass
        else:
            for i in range(len(answer)):
                if user_guess == answer[i]:
                    blanks[i] = answer[i]
                    #counter += 1
                else:
                    pass
            nice_try.append(user_guess)        
            for i in nice_try:
                if i in answer:                
                    nice_try.remove(i)
            counter = 10 - len(nice_try)
            #if counter > 10:
             #   counter = 10
            if ''.join(blanks) == answer:
                print("You saved a criminal\n")
                print(f"The word was {answer}")
                break
            if counter == 0:
                print("You lost, a criminal dies. ")
    return nice_try, blanks

load_words()
answer = random.choice(word_list)
blanks = ['_ ']* len(answer)
game_loop()





