import random


with open('english.txt', 'r') as f:
    dictionary_list = list(f.read().split('\n'))
print(dictionary_list)

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