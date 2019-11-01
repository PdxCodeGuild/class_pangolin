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

    # split into a list of words
    return input_str.split()

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

    # stopwords...words that are uninteresting that we want to omit from consideration
    STOPWORDS = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't", 's']

    # iterate through words
    for word in word_dict:
        # if qty matches that word's quantity
        if word_dict[word] == qty and word not in STOPWORDS:
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

# main:

# open book
with open('test.txt', 'r', encoding='utf8') as b:
    book = b.read()

# get list of words
word_list = format_input(book)

# create dictionary with single words as keys and quantity as the value.  
single_word_dict = create_dictionary_single_words(word_list)

# create dictionary with pair words as keys and quantity as the value.  
pair_word_dict = create_dictionary_pair_words(word_list)
# print(pair_word_dict)

# get highest quantity
highest_single_quantity = find_highest_qty(single_word_dict)
highest_pair_quantity = find_highest_qty(pair_word_dict)
# print(f'highest quantity is {highest_quantity}')

# print out highest occuring single words
print(" ****  Single Words:  ****  ")
num_words_remaining = 10
while num_words_remaining > 0:
    num_words_remaining = print_top10_words(single_word_dict, highest_single_quantity, num_words_remaining)
    if num_words_remaining > 0:
        highest_single_quantity -= 1
print()

print(" ****  Pair Words:  ****  ")
# print out highest occuring double words
num_words_remaining = 10
while num_words_remaining > 0:
    num_words_remaining = print_top10_words(pair_word_dict, highest_pair_quantity, num_words_remaining)
    if num_words_remaining > 0:
        highest_pair_quantity -= 1
print()