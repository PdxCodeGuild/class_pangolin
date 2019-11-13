'''
Remove words lab 21
written by Rhornberger
last updated nov 5 2019
'''
import string
# download and open a txt file
with open('the_phantom.txt', 'r', encoding= 'UTF-8') as phantom:
    contents = phantom.read()
    # make everything lowercase
    contents = contents.lower()
    # strip punctuation
    translator = str.maketrans('', '', string.punctuation)
    contents_with_no_punct = contents.translate(translator)
    
    # split into a list of words
    words = contents_with_no_punct.split()
    
    # bring in stop words
    stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't", "said", "one", "like", "know", "would", "us"]
    #remove stopwords
    stopwords = set(stopwords)
    for i in reversed(range(len(words))):
        if words[i] in stopwords:
            words.pop(i)
    
    # add words to a dict with count
    phantom_dict = {}
    for word in words:
        if word in phantom_dict:
            phantom_dict[word] += 1
        else:
            phantom_dict[word] = 1
    
    # find the most used 10 words in a list
    phantom = list(phantom_dict.items()) # .items() returns a list of tuples
    phantom.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(10, len(phantom))):  # print the top 10 words, or all of them, whichever is smaller
        print(phantom[i])



