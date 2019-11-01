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
def create_dictionary(word_list):
    ''' argument: list of words,
        return: a dictionary of word/quantity pairs '''

    # new empty dictionary that will eventually be returned
    words = {}

    # iterate through all words in input string
    for word in word_list:
        if not words.get(word):
            # if word not in dictionary, add it to dictionary with a value of 1
            words[word] = 1
        else:
            # if word is in dictionary, increment it's quantity by 1
            words[word] += 1
    
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
with open('moby_dick.txt', 'r', encoding='utf8') as b:
    book = b.read()

# get list of words
word_list = format_input(book)

# create dictionary with words as keys and quantity as the value.  
word_dict = create_dictionary(word_list)
# print(word_dict)

# get highest quantity
highest_quantity = find_highest_qty(word_dict)
# print(f'highest quantity is {highest_quantity}')

# print out highest occuring words
num_words_remaining = 10
while num_words_remaining > 0:
    num_words_remaining = print_top10_words(word_dict, highest_quantity, num_words_remaining)
    if num_words_remaining > 0:
        highest_quantity -= 1