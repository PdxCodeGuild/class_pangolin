# Write a function that tells whether a number is even or odd (hint, compare a/2 and a//2, or use a%2)

def is_even(userInput):
    a = userInput % 2
    if a == 0:
        return True
    return False


userInput = int(input("What is the number? "))
print(f"Is {userInput} even? {is_even(userInput)}")
