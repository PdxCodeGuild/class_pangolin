import nltk

text = "This is a way to graphically demonstrate NLTK chunking."
tokens = nltk.word_tokenize(text)
print(tokens)
tag = nltk.pos_tag(tokens)
print(tag)
grammar = "NP: {<DT>?<JJ>*<NN>}"
cp  =nltk.RegexpParser(grammar)
result = cp.parse(tag)
print(result)
result.draw()    # It will draw the pattern graphically which can be seen in Noun Phrase chunking 