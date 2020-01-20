from nltk.tokenize import RegexpTokenizer

# tokenization separates sentences into words and punctuation
tokenizer = RegexpTokenizer(r'\w+')
filterdText=tokenizer.tokenize('This is code from a NLTK tutorial that demonstrates the tokenization process.')
print(filterdText)