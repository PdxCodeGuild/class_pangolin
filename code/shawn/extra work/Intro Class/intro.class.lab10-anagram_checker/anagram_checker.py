# Shawn Stolsig
# PDX Code Guild 
# Assignment: Intro Class Lab 10 - Anagram Checker
# Date: 10/25/2019

import string # for getting punctuation

# function for getting input from user
def getInput():
    ''' function will return list of words input by user '''

    # declare return list variable
    input_list = []

    # while true
    while True:
        # ask for input
        input_word = input("Please input word(s) or 'done': ")
        # check if done
        if input_word.startswith('done'):
            # return input list when done
            return input_list
        # else append to return list
        input_list.append(input_word)

# function for cleaning up input (making lowercase and removing spaces)
def cleanInput(word):
    ''' function will take in a string, remove spaces, remove punctuation,  make lowercase, and sorted characters
        then return one string of sorted lowercase words'''

    # make string lowercase
    word = word.lower()

    # remove spaces
    word = word.replace(" ", "")

    # remove punctuation
    newstring = ''
    for letter in word:
        if letter not in string.punctuation:
            newstring += letter

    # sort word
    string_list = list(newstring)
    string_list.sort()
    return_string = ''.join(string_list)

    # return cleaned word
    return return_string

# function for checking if two words are anagrams
def checkWords(words):
    ''' function takes a list of words and returns a bool if they are anagrams or not '''


    # clean input
    clean_string_list = []
    for word in words:
        clean_string_list.append(cleanInput(word))

    # iterate through each word in words and check to see if it is equal to the first word
    are_anagrams = True
    for word in clean_string_list:
        if word != clean_string_list[0]:
            are_anagrams = False

    return are_anagrams

# main:
while True:

    # let user know if words are anagrams
    if checkWords(getInput()): 
        print("Words are anagrams!")
    else:
        print("Words are not anagrams")

    # check more anagrams?
    if input("press enter to quit or input anything to check new words "):
        pass
    else:
        break

# exit statement
print("program quitting")