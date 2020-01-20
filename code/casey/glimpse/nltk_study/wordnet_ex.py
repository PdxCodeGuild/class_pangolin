from nltk.corpus import wordnet

# code for finding synonyms and antonyms
synonyms = []
antonyms = []

for syn in wordnet.synsets("active"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
                antonyms.append(l.antonyms()[0].name())

print(set(synonyms))
print(set(antonyms))