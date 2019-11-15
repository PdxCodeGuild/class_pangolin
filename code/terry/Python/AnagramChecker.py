# Anagram Checker
# Purpose: To see if two words are anagrams of each other.

def transformWords(word_one, word_two):
    # Looks for spaces in the words, if so, removes the space
    word_one = word_one.replace(" ", "")
    word_two = word_two.replace(" ", "")
    wordOne = list(word_one)
    wordTwo = list(word_two)
    return wordOne, wordTwo


wordOne = []
wordTwo = []
# Asks the user for input and sets the words to lowercase
word_one = input("Type the first word: ").lower()
word_two = input("Type the second word: ").lower()

transformWords(word_one, word_two)

wordOne.sort()
wordTwo.sort()

if wordOne == wordTwo:
    print("\nYes, these two are anagrams.")
else:
    print("\nNo, these two are not anagrams.")
