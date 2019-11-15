
def anagram ():
    print ('Lets check if your words are anagrams')

    enter_word = input ('Enter your first word:').lower().replace(" ", "")
    enter_word2 = input ('Enter your second word:').lower().replace(" ", "")
    user_word = list (enter_word)
    user_word2 = list (enter_word2)

    user_word.sort()
    user_word2.sort()

    if user_word == user_word2:
        print ('Yes they are a anagram')
    if user_word !=  user_word2:
        print ('They are not a anagram')

    play_again = input ("do you want to play again yes or no:..")

    if play_again in ["yes", "y"]:
        anagram()


def palindrome ():
    print ('Lets check if your words are palindrome')

    enter_word = input ('Enter your word: ').lower()
    result = ""
    for i in reversed(enter_word):
        result += i
    print (result)

    if enter_word == result:
        print ('True your word is a palindrome')
    else:
        print ('False your word is a plindrome')


while True :
    options = (input('Would you like to use the anagram or palindrome checker?\n *please select a or p or quit: '))

    if options == 'a':
        anagram ()
    elif options == 'p':
        palindrome ()
    else:
        print ('Thank you for playing!')
        break