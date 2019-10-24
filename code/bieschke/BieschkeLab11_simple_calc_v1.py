#BieschkeLab11_simple_calc_v1.py 
'''
Let's write a simple REPL (read evaluate print loop) calculator that can 
handle addition, subtraction, multiplication, and division. 
Ask the user for an operator and each operand.
'''
operation = ["+", "-", "/", "*"]

print("Hello! And welcome to the calculator script")
op = input("What is the operation you'd like to perform?")

if op in operation:
    pass
else:
    print("Just the 4 basics operands plz")
    quit()

first = float(input("What is the first number?"))
second = float(input("What is the second number?"))

if op == '+':
    print(f"{first} + {second} = {first + second}")
if op == '-':
    print(f"{first} - {second} = {first - second}")
if op == '*':
    print(f"{first} * {second} = {first * second}")
if op == '/':
    print(f"{first} / {second} = {first / second}")