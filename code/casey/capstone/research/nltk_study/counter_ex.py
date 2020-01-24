from collections import Counter
import nltk

text = "Let's demonstrate NLTK's ability to tokenize, tag for part of speech and then count!"
lower_case = text.lower()
tokens = nltk.word_tokenize(lower_case)
tags = nltk.pos_tag(tokens)
counts = Counter( tag for word,  tag in tags)
print(counts)