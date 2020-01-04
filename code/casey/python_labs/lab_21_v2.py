'''
Lab 21: Count Words - Version 2

Purpose/goal: Count how often each unique pair of words is used, then print the top 10 most common pairs with their counts.

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