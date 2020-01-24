import nltk

# code to find bigrams (two words that go together)
text = "Guru99 is a totally new kind of learning experience."
Tokens = nltk.word_tokenize(text)
output = list(nltk.bigrams(Tokens))
print(output)

print("\n")

# code to find trigrams (three words that go together)
text = "Guru99 is a totally new kind of learning experience."
Tokens = nltk.word_tokenize(text)
output = list(nltk.trigrams(Tokens))
print(output)