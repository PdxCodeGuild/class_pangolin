import string
word_pairings = {}
user_word = input("Enter a word. ").lower()
with open('jane_eyre.txt', 'r') as file:
    text = file.read()
    text = text.lower()
    translator = str.maketrans('', '', string.punctuation)
    no_punct = text.translate(translator)
    word_list = no_punct.split()
    for i in range(len(word_list)-1):
        if word_list[i] == user_word:
            word_pairing = word_list[i+1]
            if word_pairing not in word_pairings:
                word_pairings[word_pairing] = 1
            else:
                word_pairings[word_pairing] += 1
       
    print(word_pairings)
   
    word_pairings = list(word_pairings.items()) # .items() returns a list of tuples
    word_pairings.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(10, len(word_pairings))):  # print the top 10 words, or all of them, whichever is smaller
        print(word_pairings[i])


