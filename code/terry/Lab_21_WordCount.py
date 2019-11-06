# python module to analyze a given text file containing a book for its vocabulary frequency and display the most
# frequent words to the user

import string

dic_of_words = {}

with open('pg6422.txt', 'r') as file:
    lines = file.read().lower()

translator = str.maketrans('', '', string.punctuation)
string_without_punct = lines.translate(translator)
#print(string_without_punct)

for i in range(len(string_without_punct)):
    dic_of_words[i]
print(dic_of_words)
