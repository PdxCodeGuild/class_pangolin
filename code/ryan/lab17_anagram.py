def check_anagram():
    first_word = input("What is your first word?  ").lower()
    second_word = input("What is your second word?  ").lower()
    first_word = first_word.replace(" ", "")
    second_word = second_word.replace(" ", "")

    if sorted(first_word) == sorted(second_word):
        return True
    return False

if check_anagram() == True:
    print("This is an anagram")
else:
    print("Not an anagram")
