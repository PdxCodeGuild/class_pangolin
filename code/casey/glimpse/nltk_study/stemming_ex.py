from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

# determines the root word
e_words= ["wait", "waiting", "waited", "waits"]
ps =PorterStemmer()
for w in e_words:
    rootWord=ps.stem(w)
    print(rootWord)
print("\n")    

sentences = "I have learned so much from this tutorial that is intended to help me learn. I'm learning a lot!"
words = word_tokenize(sentences)
ps = PorterStemmer()
for w in words:
	rootWord=ps.stem(w)
	print(rootWord)