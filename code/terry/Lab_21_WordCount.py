# python module to analyze a given text file containing a book for its vocabulary frequency and display the most
# frequent words to the user

import string

dic_of_words = {}

with open('pg6422.txt', 'r') as file:
    lines = file.read().lower()

translator = str.maketrans('', '', string.punctuation)
string_without_punct = lines.translate(translator)
list_of_words = string_without_punct.split()
# print(list_of_words)

for w in list_of_words:
    if w in dic_of_words:
        num = dic_of_words[w]
        num += 1
        dic_of_words.update({w: num})
    else:
        dic_of_words[w] = 1

# dic_of_words[i]
print(dic_of_words)
# print(words)
