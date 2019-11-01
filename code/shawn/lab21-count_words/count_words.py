# Shawn Stolsig
# PDX Code Guild 
# Assignment: Lab 21: Count Words
# Date: 10/31/2019

import string

# function for cleaning input string (removes newlines, punctuation, uppercase, special characters)
def format_input(input_str):
    ''' argument: unformated input string
        return: list of words split on white space '''
    # strip punctuation
    translator = str.maketrans('', '', string.punctuation)
    string_without_punct = input_str.translate(translator) # I am a string with punctuation
    input_str = string_without_punct

    # make everything lower case
    input_str = input_str.lower()
    # get rid of newlines
    input_str = input_str.replace('\n',' ')

    # turn string into list
    input_list = input_str.split()

    # remove stopwords.  also remove 'gutenbergtm' to cleanup input files
    STOPWORDS = ['gutenbergtm', 'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't", 's', 'the']
    for i in range(len(input_list)-1, -1, -1):
        if input_list[i] in STOPWORDS:  
            input_list.pop(i)
    
    # split into a list of words
    return input_list

# function for creating dictionary from word list
def create_dictionary_single_words(word_list):
    ''' argument: list of words,
        return: a dictionary of word/quantity pairs '''

    # new empty dictionary that will eventually be returned
    words = {}

    # iterate through all words in input string
    for i in range(len(word_list)):

        # for clarity's sake, set word equal to current element in word_list
        word = word_list[i]

        # for each word in word_list
        if word in words and i != len(word_list):
            # if word in dictionary, increment its quantity
            words[word] += 1
        else:
            # else word is not in dictionary, create/intialize it with value of 1
            words[word] = 1
    
    # return dictionary
    return words

# function for creating dictionary of word pairs
def create_dictionary_pair_words(word_list):
    ''' argument: list of words,
        return: a dictionary of word/quantity pairs '''

    # new empty dictionary that will eventually be returned
    words = {}

    # iterate through all words in input string
    for i in range(len(word_list)):

        # for clarity's sake, set word equal to current element in word_list
        word = word_list[i]

        # if you've reached end of word_list, wrap around and set next_word to index 0
        if i == (len(word_list) - 1):
            next_word = word_list[0]
        # else for every other word, next_word is index + 1
        else:
            next_word = word_list[i+1]

        # for each word in word_list
        if words.get(word + " " + next_word):
            # if word in dictionary, increment its quantity
            words[word + " " + next_word] += 1
        else:
            # else word is not in dictionary, create/intialize it with value of 1
            words[word + " " + next_word] = 1
    
    # return dictionary
    return words

# function for creating dictionary of word pairs
def create_dictionary_pair_words_enhanced(word_list):
    ''' argument: list of words,
        return: a dictionary of word/quantity pairs '''


    # Data structure:
    # word_dict = {
    #     'word_name' = { 'quantity' = int, next_words = {
    #                                                    'word_name' = int_qty
    #                                                    } 
    #     }
    # }

    # new empty dictionary that will eventually be returned
    words = {}

    # iterate through all words in input string
    for i in range(len(word_list)):

        # for clarity's sake, set word equal to current element in word_list
        word = word_list[i]

        # if you've reached end of word_list, wrap around and set next_word to index 0
        if i == (len(word_list) - 1):
            next_word = word_list[0]
        # else for every other word, next_word is index + 1
        else:
            next_word = word_list[i+1]

        # for each word in word_list
        if word in words:
            # if word in dictionary, increment its quantity
            words[word]['quantity'] += 1
            if next_word in words[word]['next_words']:
                words[word]['next_words'][next_word] += 1
            else:
                words[word]['next_words'][next_word] = 1               
        else:
            # else word is not in dictionary, create/intialize it with value of 1
            words[word] = { 'quantity': 1, 'next_words':  { next_word: 1}}

    # return dictionary
    return words

# function for finding highest quantity of word
def find_highest_qty(word_dict):
    ''' argument: dictionary of word/quantity pairs
        returns: int representing the highest quantity word '''
    
    # declare variable to track max
    max = 0

    # iterate through words
    for key in word_dict:
        if word_dict[key] > max:
            max = word_dict[key]
    
    return max

# print words with this quantity
def print_top10_words(word_dict, qty, num_words_remaining):
    ''' arguments: word diction with word/quantity pairs
        returns: int of how many times it ran '''

    # iterate through words
    for word in word_dict:
        # if qty matches that word's quantity
        if word_dict[word] == qty:
            # print out word
            print(f"{word} appears {word_dict[word]} times")
            # decrement num_words_remaining
            num_words_remaining -= 1
        # if num_words_remaining equals 0
        if num_words_remaining == 0:
            return num_words_remaining
    
    # still words remaining, return how many
    # print(f'returning...num words remaining is {num_words_remaining}')
    return num_words_remaining

# return which word comes most frequently afterwards
def get_common_next_word(word_dict, word):
    ''' arguments: enhanced pair word dictionary and input word string
        return: which word is most common to come next '''

    # get highest quantity word
    most_common_quantity = find_highest_qty(word_dict[word]['next_words'])

    # get most common word using most_common_quantity, the first time it appears
    for next_word in word_dict[word]['next_words']:
        if word_dict[word]['next_words'][next_word] == most_common_quantity:
            return next_word

    # return most common next word
    return "error can't find most common word"


# main:

# open book
with open('moby_dick.txt', 'r', encoding='utf8') as b:
    book = b.read()

# get list of words
word_list = format_input(book)

# create dictionary with single words as keys and quantity as the value.  
single_word_dict = create_dictionary_single_words(word_list)

# create dictionary with pair words as keys and quantity as the value.  
# using "enhanced" pair word nomenclature for everything related to version 3
pair_word_dict = create_dictionary_pair_words(word_list)
enhanced_pair_word_dict = create_dictionary_pair_words_enhanced(word_list)

# get highest quantity
highest_single_quantity = find_highest_qty(single_word_dict)
highest_pair_quantity = find_highest_qty(pair_word_dict)
# print(f'highest quantity is {highest_quantity}')

# print out highest occuring single words
print(" ****  Single Words:  ****  ")

# find out how many characters to print
if len(single_word_dict.items()) > 10:
    num_words_remaining = 10    # how many pairs to print
else:
    num_words_remaining = len(single_word_dict.items())

while num_words_remaining > 0:
    num_words_remaining = print_top10_words(single_word_dict, highest_single_quantity, num_words_remaining)
    if num_words_remaining > 0:
        highest_single_quantity -= 1
print()

print(" ****  Pair Words:  ****  ")
# print out highest occuring double words

# find out how many characters to print
if len(pair_word_dict.items()) > 10:
    num_words_remaining = 10    # how many pairs to print
else:
    num_words_remaining = len(pair_word_dict.items())
 
while num_words_remaining > 0: 
    num_words_remaining = print_top10_words(pair_word_dict, highest_pair_quantity, num_words_remaining)
    if num_words_remaining > 0:
        highest_pair_quantity -= 1
print()


# create REPL for checking which word most frequently follows input word
while True:
    user_input = input("Press enter for next mode, or type in a word to figure out which word most frequently follows it: ")
    # quit if user doesn't input anything
    if not user_input:
        print('Going to sentence generation mode\n\n')
        break
    # find most common word to appear after if user enters a word that is in the input
    elif user_input in enhanced_pair_word_dict:
        print(f" The most common word to appear after '{user_input}': {get_common_next_word(enhanced_pair_word_dict,user_input)}")
    # handle if user inputs a word that doesn't appear in the original input
    else:
        print("That word doesn't appear in the input file.")

# auto generate a sentence
while True:
    sentence_length = input("How long of sentence would you like to generate?  Enter 0 or press Enter to quit: ")

    # quit if user doesn't input anything
    if sentence_length in ['0', 'done', 'exit', 'quit', '']:
        print('exiting program')
        break

    else:
        # get starting string
        starting_word = input("What word would you like to start with? ")
        generated_sentence = starting_word.lower()
        prev_word = starting_word.lower()

        sentence_length = int(sentence_length)

        # iterate user_input number of times
        while sentence_length > 0:
            prev_word = get_common_next_word(enhanced_pair_word_dict,prev_word)
            generated_sentence += ' ' + prev_word
            sentence_length -= 1
        generated_sentence += "."
        generated_sentence = generated_sentence.capitalize()

        print(f'Your generated sentence is:')
        print(generated_sentence)