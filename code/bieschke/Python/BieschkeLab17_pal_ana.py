#Bieschke Lab 17: Palindromes and Anagrams 

def palindrome():
    palantir = input("Palindromes it is! What is your word or phrase?").lower()
    #removes all the spaces between the words of the phrase    
    palantir = palantir.replace(" ", "")
    #reveses the string by going to the end of the list and moving backwards
    palantir2 = palantir[::-1]

    if palantir == palantir2:
        print("Palindrome!")
    else:
        print("Nope!")

def anagram():
    phrase1 = input("Anagrams it is! Enter your first phrase now\n>").lower()
    phrase2 = input("Enter your second phrase\n>").lower()

    #removes all the spaces between the words of the phrase
    phrase1 = phrase1.replace(" ", "")
    phrase2 = phrase2.replace(" ", "")

    #sorts the phrases' characters alphabetically
    phrase1 = sorted(phrase1)
    phrase2 = sorted(phrase2)

    if phrase1 == phrase2:
        print("Anagrams!")
    else:
        print("Nope!")

lion = True
while lion == True:
    print("Hello! Would you like to analyze a palindrome or an anagram today?")
    x = input("Type 'pal' for palindrome, 'ana' for anagram, or press Enter to quit.")

    if x == "pal":
        palindrome()
    elif x == "ana":
        anagram()
    elif x == '':
        print("Sayonara!")
        quit()
    else:
        continue