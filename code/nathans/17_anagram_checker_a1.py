# anagram_checker_a1.py


word_1 = input("Enter first word: ").lower()
word_2 = input("Enter second word ").lower()
word_1 = word_1.replace(' ', '')
word_2 = word_2.replace(' ', '')
sorted_word_1 = sorted(word_1)
sorted_word_2 = sorted(word_2)


if sorted_word_1 == sorted_word_2:
    print("The words are anagrams!")
else:
    print("Not Anagrams!")
