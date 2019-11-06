import random

dictionary_list = []
n_words_or_greater = []

# function for opening/initializing file
def file_init(filename, word_length):
    ''' parameters: filename as a string, word_length
        return: list of strings of words over input word_length '''

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
    return target_word

print(type(get_target_word(file_init('english.txt', 5))))
