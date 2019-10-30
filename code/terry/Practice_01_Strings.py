# Get a string from the user, print out another string, doubling every letter.

def double_letters(userInput):
    userList = list(userInput)
    y = "".join([x * 2 for x in userList])
    return y


userInput = input("What is the word? ")
print(double_letters(userInput))