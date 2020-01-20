import nltk

text = "This is an example of NLTK's functions that first tokenize a sentence and then tag those tokens!"
sentence = nltk.sent_tokenize(text)
for sent in sentence:
	 print(nltk.pos_tag(nltk.word_tokenize(sent)))