'''
Palindrome and Anagram lab
written by Rhornberger
last updated oct 28 2019
'''
#write a function that will tell if a word is the same forward and backwords

def pal(user_choice):
    if user_choice == user_choice[::-1]:
        return 'Yes this is a palindrome!'
    return 'I am sorry this is not a palindrome.'


#write a function that tells you if a word is an anagram

def ana(a, b):
    a2 = a.replace(' ', '')
    b2 = b.replace(' ', '')
    a3 = sorted(a2)
    b3 = sorted(b2)
    if a3 == b3:
        return 'Yes! These are anagrams of eachother. '
    return 'No, these are not anagrams of eachother'

# get the user input
user_input = input('Would you like to check for an anagram or a palindrome?: ').lower()
if user_input == 'anagram':
    word1 = input('Please enter your first word.: ').lower()
    word2 = input('Please enter your second word.: ').lower()
    print(ana(word1, word2))
elif user_input == 'palindrome':
    word = input('what word would you like to check?: ').lower()
    print(pal(word))
else:
    print('I am sorry that word is outside of my programmed understanding. Please try again another time.')
print('Thank you for using the Anagram Palindrome bot!')