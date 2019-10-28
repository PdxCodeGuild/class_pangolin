#BieschkeLab11_simple_calc_v1.py 
'''
Write a simple REPL (read evaluate print loop) calculator that can 
handle addition, subtraction, multiplication, and division. 
Ask the user for an operator and each operand.
Allow the user to keep performing operations until they say 'done'.
'''
tiger = True
operation = ["+", "-", "/", "*"]
first = 0
second = 0

def stop():
    if op == "done" or first == "done" or second == "done":
        print("Sayonara!")
        quit()
    else:
        pass

while tiger == True:
    print("Hello! And welcome to the calculator script.")
    print("You can quit at any time by typing 'done'")
    op = input("What is the operation you'd like to perform?")
    stop()

    if op in operation:
        pass
    else:
        print("Just the 4 basics operands plz")
        continue

    first = (input("What is the first number?"))
    stop()
    first = float(first)
    second = (input("What is the second number?"))
    stop()
    second = float(second)

    if op == '+':
        print(f"{first} + {second} = {first + second}")
    if op == '-':
        print(f"{first} - {second} = {first - second}")
    if op == '*':
        print(f"{first} * {second} = {first * second}")
    if op == '/':
        print(f"{first} / {second} = {first / second}")
    print("*" *50)