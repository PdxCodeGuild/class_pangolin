#Lab21 version 1
#11/2/2019, Wiley Rummel

#Write a python module to analyze a given text file containing a book for its vocabulary frequency 
#and display the most frequent words to the user in the terminal. 
#Remember there isn't any "perfect" way to identify a word in english (acronymns, mr/ms, contractions, etc), 
#try to find rules that work best.

#import the book, open, and create an object variable to work with (contents)
import os, string, re
file_name = 'Little_Women.txt'
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name), 'r') as book:
    contents = book.read()


#word_regex = re.compile(r'^[a-zA-Z']+') maybe try a regex? Would this break cor contractions?

#strip the contents of the book into a string without punctuation.  
translator = str.maketrans('','', string.punctuation)
contents_no_punct = contents.translate(translator).lower()

#define a function that will analyze the contents of the book
#this function will add a key for each new word, and increment the count for previously recognized words


def word_count(contents_no_punct):
    '''This is a function to analyze a list of strings, and return a dictionary
    where the keys are the words in the list and the values are their frequency of use.'''
    word_dict = {}
    contents_no_punct_list = contents_no_punct.split()
    stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've",
     "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 
     "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 
     'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 
     'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 
     'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 
     'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after',
     'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again',
     'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both',
     'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same',
     'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 
     'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', 
     "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 
     'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', 
     "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't",'dont','wont','shouldnt',
     'couldnt','isnt','said','one','two','like','go','im','much']
    for i in contents_no_punct_list:
        if i in stopwords:
            pass
        elif i in word_dict:
            word_dict[i] += 1
        else:
            word_dict[i] = 1
    return word_dict
#word_count(contents_no_punct)

words = list(word_count(contents_no_punct).items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])

