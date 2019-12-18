word_to_check = input("Enter a word to see if it is a palindrome:  ")

def check_palindrome():
    if word_to_check == word_to_check[:: -1]:
        return word_to_check + " is a palindrome"
    return word_to_check + " is not a palindrome"

print(check_palindrome())
