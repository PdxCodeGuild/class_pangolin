import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import FreqDist
from nltk.collocations import *
from nltk.corpus import stopwords
from nltk.corpus import gutenberg
import string
import random

def main(input):
        print(input.name)
        print(f"Average Sentence Length: {input.av_sent_len()}")
        print(f"Lexical Diversity: {input.lex_diversity()}%")
        print(f"Instance of 'to': {input.count_to()}%")
        print (f"Most common words: {input.freq_dist()}")
        # print(f"Trigrams: {input.collocate()}")

class Text:
    def __init__(self, file, name):
        f = open(file)
        punct = ['.', ',', '?', ':', ';', '/', '(', ')', '-', '--', '"', "'", '“', '”', '’', '!', "''", "``", "'s", '_', "n't", "'ll"]
        self.name = name
        self.text = f.read().lower()
        self.sents = sent_tokenize(self.text)
        self.with_punct = word_tokenize(self.text)
        self.tokens = [token for token in self.with_punct if not token in punct]

    def freq_dist(self):
        stop_words = set(stopwords.words('english'))
        filtered = [w for w in self.tokens if not w in stop_words] 
        fdist = FreqDist(filtered)
        top_10 = fdist.most_common(10)
        word_list= []
        for word, count in top_10:
            word_list.append(word) 
        return word_list

    def av_sent_len(self):
        num_sent = len(self.sents)
        num_words = len(self.tokens)
        return round(num_words / num_sent, 2)
        

    def lex_diversity(self):
        tokens_list = []
        while len(tokens_list) < 1000:
            tokens_list.append(random.choice(self.tokens))
        return round((len(set(tokens_list))/10), 2)
    
    def count_to(self):
        tagged_words = nltk.pos_tag(self.tokens)
        to_counter = 0   
        for word, tag in tagged_words:
            if (tag == 'TO'):
                to_counter += 1 
        return round((to_counter/len(self.tokens))*100, 2)
    
    def tag_words(self):
        tagged = nltk.pos_tag(self.tokens)
        tag_fd = nltk.FreqDist(tag for (word, tag) in tagged)
        return tag_fd.most_common()
    
    # def collocate(self):
    #     tokens = word_tokenize(self.text)
    #     trigram_measures = nltk.collocations.TrigramAssocMeasures()
    #     finder = BigramCollocationFinder.from_words(tokens)
    #     scored = finder.score_ngrams(trigram_measures.raw_freq)
    #     set(trigram for trigram, score in scored) == set(nltk.trigrams(tokens))
    #     return sorted(finder.nbest(trigram_measures.raw_freq, 10))
        

text1 = Text('christmas_carol.txt', "A Christmas Carol")
text2 = Text('tom_sawyer.txt', "Tom Sawyer")
main(text1)
main(text2)