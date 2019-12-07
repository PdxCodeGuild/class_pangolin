'''
Lab 21: Count Words - Version 1

Purpose/goal: Write a python module to analyze a given text file containing a book for its vocabulary frequency and display the most frequent words to the user in the terminal.

    - Remember there isn't any "perfect" way to identify a word in english (acronymns, mr/ms, contractions, etc), try to find rules that work best.

    - Find a book on Project Gutenberg. - D
    
    - Download it as a UTF-8 text file. - D

    - Open the file. - D

    - Make everything lowercase - D
    
    - strip punctuation - D
    
    - split into a list of words. - D

To strip punctuation:

import string
s = 'I $am a !string with punc&^%*tuation!'
translator = str.maketrans('', '', string.punctuation)
string_without_punct = s.translate(translator) # I am a string with punctuation

    - Your dictionary will have words as keys and counts as values. If a word isn't in your dictionary yet, add it with a count of 1. If it is, increment its count. - D

Print the most frequent top 10 out with their counts. You can do that with the code below.

# word_dict is a dictionary where the key is the word and the value is the count
words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])

You'll find that the most common words aren't particularly interesting (lots of 'I's, 'the', 'and', 'he', 'she', and 'but's). To get more relevant words, remove stop words from your text.

STOPWORDS = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

'''

# open wolf_ear_the_indian.txt file / read / set contents variable /
with open('wolf_ear_the_indian.txt', 'r') as book:
    contents = book.read()
    contents = contents.lower()
    # define punctuation list
    punct = [",", ".", "?", "!", '"', ":", ";", "(", ")", "-", "/"]
    
    # create common words list
    common_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

    # strip punctuation from contents
    for x in contents:
        if x in punct:
            contents = contents.replace(x, "")

    # define words_list by splitting contents
    words_list = contents.split()

    # strip common words from words_list
    for word in words_list:
        if word in common_words:
            words_list.remove(word)

    # create word_count_dict
    word_count_dict = {}

    # count repeats / add words in words_list to dict
    for word in words_list:
        if word in word_count_dict:
            word_count_dict[word] +=1
        else:
            word_count_dict[word] = 1

    # .items() returns a list of tuples
    words = list(word_count_dict.items()) 
    # sort largest to smallest, based on count
    words.sort(key=lambda tup: tup[1], reverse=True)  
    for i in range(min(10, len(words))):  
        # print the top 10 words, or all of them, whichever is smaller
        print(words[i])
    