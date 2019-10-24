# Taylor Rebbe
# PDX Coed Guild
# Lab_11v2

# Message variables
message1 = "\nWhat is the operation you'd like to perform (+, -, *, /)? > "
message2 = "\nWhat is the first number? > " 
message3 = "\nWhat is the second number? > "
message4 = "\nTo exit type done: > "

# Input variables
get_operator = input(message1)
f_num = float(input(message2))
s_num = float(input(message3))

# Loop variable
game_over = ""

# Math operators dictionary
math_operators = {
     "+": f_num + s_num,
     "-": f_num - s_num,
     "*": f_num * s_num,
     "/": f_num / s_num
     }

# Functions
def getCalculation():
    for key, value in math_operators.items():
     if key == get_operator:
         return value

# Program loop
while game_over != "done":
    print(getCalculation())

    game_over = input(message4)
    print("\nBye bye")