# Shawn Stolsig
# PDX Code Guild
# Assignment: Optional Lab - Arbitrary Precision Arithmetic
# Date: 11/6/2019

# addition

# get input

while True: 

    # get num1 input, checking to make sure it's an int
    try:
        num1 = int(input("What is the first number? "))
        break
    except ValueError: 
        print("You did not input an int, please try again.")

    # get num2 input, checking to make sure it's an int
    try:
        num2 = int(input("What is the first number? "))
        break
    except ValueError: 
        print("You did not input an int, please try again.")