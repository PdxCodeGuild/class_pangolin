'''
Lab 17: Palindrome and Anagram - Version 1

Purpose/goal: Write a palindrome and anagram checker.

Palindrome:

    - Write a function that reverses user's potential palindrome - D

    - Write a function check_palindrome which takes a string, and returns True if the string's a palindrome, or False if it's not - D

Anagram:

    - Write another function check_anagram that takes two strings as parameters and returns True if they're anagrams of eachother, False if they're not. - D
    
The procedure for comparing the two strings is:

    - Convert each word to lower case (lower) - D
    
    - Remove all the spaces from each word (replace) - D
    
    - Sort the letters of each word (sorted) - D 

    - Check if the two are equal - D

'''

def reverse(a):
    return a [::-1]

def check_palindrome(b):
    if b == pot_pal:
        print(f"Yes, '{user_word}' is a palindrome!")
    else:
        print(f"No, '{user_word}' is not a palindrome!") 

def check_anagram(e):
    if e == sort2:
        print(f"Yes, '{user_word1}' & '{user_word2}' are anagrams!")
    else:
        print(f"No, '{user_word1}' & '{user_word2}' are not anagrams!")

# user greeting
print("Hello.\nThis is a palindrome & anagram checker.")

# ask for goal
goal = input("Which would you like to check for (palindrome or anagram)?: ").lower()

# define user_word palindrome 
if goal == "palindrome":
    user_word = input("Great. Enter your word: ").lower()

# palindrome check procedure
    pot_pal = reverse(user_word)
    check_palindrome(user_word)

# definte user_word anagram
if goal == "anagram":
    user_word1 = input("Great. Enter your first word: ").lower()

    user_word2 = input("Enter your second word: ").lower()

# anagram check procedure
    replace1 = user_word1.replace(" ", "")
    replace2 = user_word2.replace(" ", "")
    sort1 = sorted(replace1)
    sort2 = sorted(replace2)
    check_anagram(sort1)

