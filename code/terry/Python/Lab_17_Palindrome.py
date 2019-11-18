# A palindrome is a word that's the same forwards or backwards, e.g. racecar. Another way to think of it is as a word
# that's equal to its own reverse.

def check_palindrome(userWord):
    userWord1 = list(userWord)
    userWord2 = userWord1.copy()
    userWord1.reverse()
    if userWord1 == userWord2:
        return True
    return False


userWord = input("What is the word? ")
print(f"Is {userWord} a palindrome? {check_palindrome(userWord)}")
