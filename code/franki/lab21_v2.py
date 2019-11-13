import string
word_pairs = {}
with open('jane_eyre.txt', 'r') as file:
    text = file.read()
    text = text.lower()
    translator = str.maketrans('', '', string.punctuation)
    no_punct = text.translate(translator)
    word_list = no_punct.split()
    stop_words = ['gutenberg', 'project', 'gutenbergtm', 'i', 'of', 'the', 'is', 'am', 'are', 'was', 'in', 'my', 'and', 'to', 'me', 'from', 'a', 'an', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', "can't", 'will', 'just', "don't", 'should', "should've", 'now', 'more', "ain't", 'aren', "aren't", "couldn't", 'didn', "didn't", 'doesn', "doesn't", "hadn't", "hasn't", "haven't", "isn't", "mightn't", "must", "mustn't", "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", "wouldn't", "would", "said", "like", "could", "one", "mr", "some", "mrs", "miss", "yet", "still", "well", "shall", "go", "can"] 
    for i in range(len(word_list)-1):
        word_pair = []
        if word_list[i] in stop_words: 
            pass
        elif word_list[i + 1] in stop_words:
            pass
        else:
            word_pair.append(word_list[i])
            word_pair.append(word_list[i+1])
            word_pair = ' '.join(word_pair)
            if word_pair not in word_pairs:
                word_pairs[word_pair] = 1
            elif word_pair in word_pairs:
                word_pairs[word_pair] += 1
    print(word_pairs)
   
    word_pairs = list(word_pairs.items()) # .items() returns a list of tuples
    word_pairs.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(10, len(word_pairs))):  # print the top 10 words, or all of them, whichever is smaller
        print(word_pairs[i])


