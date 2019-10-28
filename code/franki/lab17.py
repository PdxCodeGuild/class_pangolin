def palindrome_checker(a):
    a = a.replace(" ", "")
    print(a)
    letters = list(a)
    print(list(a))
    letters.reverse()
    if letters == list(a):
        return True
    else:
        return False
def anagram_checker(a, b):
    letters1 = list(a)
    letters1.sort()
    print(letters1)
    letters2 = list(b)
    letters2.sort()
    print(letters2)
    if letters1 == letters2:
        return True
    else:
        return False
running = True
print("Welcome to the palindrome/anagram checker.")
while running == True:
    user_choice = input("Would you like to check for a palindrome or anagram? (Enter 'p', 'a', or 'done'). ").lower()   
    if user_choice in ["p", "palindrome"]:
        word = input("Enter a word. ")
        print(palindrome_checker(word))
    elif user_choice in ["a", "anagram"]:
        word1 = input("Enter a word. ")
        word2 = input("Enter another word. ")
        print(anagram_checker(word1, word2))
    elif user_choice == "done":
        break
    else:
        continue
print("Bye!")