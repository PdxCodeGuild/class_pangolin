import string
s = 'I $am a !string with punc&^%*tuation! am - am  am-am am—am am\'s'

translator = str.maketrans('', '', string.punctuation)
string_without_punct = s.translate(translator) # I am a string with punctuation
print(string_without_punct)
print(string.punctuation)