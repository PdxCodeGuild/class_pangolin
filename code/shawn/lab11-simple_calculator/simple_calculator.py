# Shawn Stolsig
# PDX Code Guild 
# Assignment: Lab 11 - Simple Calculator
# Date: 10/23/2019

# ( version 3: might not be possible since they've limited literal_eval
# to not execute expressions....safe version of eval called ast.literal_eval  must import ast  )

# main loop
while True:
    # get operator input
    op = input("What is the operation you'd like to perform? ")

    # create loop exit
    if op == "done":
        break

    # get number input
    num1 = float(input("What is the first number? "))
    num2 = float(input("What is the second number? "))

    # otherwise, print operation
    if op == '+':
        print(f"{num1} {op} {num2} = {num1 + num2}")
    elif op == '-':
        print(f"{num1} {op} {num2} = {num1 - num2}")
    elif op == '/':
        print(f"{num1} {op} {num2} = {num1 / num2}")
    elif op == '*':
        print(f"{num1} {op} {num2} = {num1 * num2}")
    elif op == '%':
        print(f"{num1} {op} {num2} = {num1 % num2}")
    elif op == '**':
        print(f"{num1} {op} {num2} = {num1 ** num2}")
    else:
        print("unknown operator, restarting")

print('goodbye!')
