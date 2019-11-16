#Write a function check_palindrome which takes a string, and returns True if the string's a palindrome, or False if it's not.

def check_palindrome():
    var1 = input("Let's find some palindromes! Give me a word.\n").lower()
    var1_list = [x for x in var1]
    var1_list_reverse = []
    print(var1_list)
    var1_list_reverse = var1_list[::-1]
    print(var1_list_reverse)
    if var1_list == var1_list_reverse:
        print("True!")
    else:
        print("False :(")


#Write another function check_anagram that takes two strings as parameters and returns 
#True if they're anagrams of eachother or False if they're not. 

def check_anagram(a,b):
    print("Welcome to anagram checker! Enter two words or phrases you wish to check!")

    a.replace(' ','')
    b.replace(' ','')
    a_list = [x for x in a]
    b_list = [x for x in b]
    a_list.sort()
    b_list.sort()
    if a_list == b_list:
        print("Thats an anagram!")
    else:
        print("Not an anagram.")

#function that lets you choice which checker you want to use!
def palindrome_or_anagram():
    print("""Welcome to the Palindrome or Anagram Checker! 
Please type 'P' if you would like to test a Palindrome or 'A' if you would like to check an Anagram.
Type 'Done' to exit the program.""")
    choice = input("> ").lower()
    if choice == 'p':
        check_palindrome()
        return
    elif choice == 'a':
        a = input("First item to check \n").lower()
        b = input("Second item to check \n").lower()
        check_anagram(a,b)
        return
    elif choice == 'done':
        print("Exiting....")
        return
    else:
        print("Not a valid selection")
        pass

palindrome_or_anagram()