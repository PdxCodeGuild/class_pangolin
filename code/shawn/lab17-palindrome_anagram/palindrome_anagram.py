# Shawn Stolsig
# PDX Code Guild 
# Assignment: Lab 19 - Palindrome/Anagram checker
# Date: 10/28/2019

# a palindrome is a word that is equal to the reverse of itself

# def function for checking if input is palindrome
def is_palindrom(input_str):
    ''' function takes an input string and returns true/false if it's a palindrome '''
    return input_str == input_str[-1::-1]

# define function for checking if input strings are anagrams
def are_anagrams(words):
    ''' function takes in a list of input strings and returns true/false if they are anagrams '''

    # declare new, corrected list of words
    prepped_words = []
    string_to_push = ''

    for word in words:
        # convert to lowercase
        string_to_push = word.lower()
        # sort letters in word
        string_to_push = ''.join(sorted(list(string_to_push)))
        # strip spaces from font
        string_to_push = string_to_push.strip()
        # push string onto new list of words
        prepped_words.append(string_to_push)

    # check to see if they are equal
    is_anagrams = True
    for word in prepped_words:
        if word != prepped_words[0]:
            is_anagrams = False
    
    # return bool
    return is_anagrams

# main
while True:

    # get mode 
    user_mode = input("Please input 'p' for palindrome mode or 'a' for anagram mode.  Press enter to quit: ")

    # to quit
    if not user_mode:
        print("quitting")
        break

    # to enter anagram mode
    elif user_mode == 'a':
        # get input
        words = []
        while True:
            user_word = input("What word(s) to check? Input 'done' to stop: ")  
            if user_word == 'done': 
                    break
            words.append(user_word)      
        
        # print if words are anagrams or not
        if are_anagrams(words): 
            print(f"{words} are anagrams")
        else:
            print(f"{words} are not anagrams")

    # to enter palindrom mode
    elif user_mode == 'p':
        user_word = input("What word to check? ")

        # print if words are anagrams or not
        if is_palindrom(user_word): 
            print(f"{user_word} is a palindrome")
        else:
            print(f"{user_word} is not a palindrome")

    # to handle bad input
    else:
        print("invalid selection, try again")
