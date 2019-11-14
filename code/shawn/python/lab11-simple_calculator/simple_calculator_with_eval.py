# Shawn Stolsig
# PDX Code Guild 
# Assignment: Lab 11 - Simple Calculator
# Date: 10/23/2019

# for literal_eval
import ast


# main loop
while True:

    ################################ Version 2
    # # get operator input
    # op = input("What is the operation you'd like to perform? ")

    # # create loop exit
    # if op == "done":
    #     break

    # # get number input
    # num1 = float(input("What is the first number? "))
    # num2 = float(input("What is the second number? "))

    # # otherwise, print operation
    # if op == '+':
    #     print(f"{num1} {op} {num2} = {num1 + num2}")
    # elif op == '-':
    #     print(f"{num1} {op} {num2} = {num1 - num2}")
    # elif op == '/':
    #     print(f"{num1} {op} {num2} = {num1 / num2}")
    # elif op == '*':
    #     print(f"{num1} {op} {num2} = {num1 * num2}")
    # elif op == '%':
    #     print(f"{num1} {op} {num2} = {num1 % num2}")
    # elif op == '**':
    #     print(f"{num1} {op} {num2} = {num1 ** num2}")
    # else:
    #     print("unknown operator, restarting")

    ###################### Version 3
    # get operator input
    op = input("Please type out your expression: ")

    # create loop exit
    if op == "done":
        break

    # use literal_eval to evaluate
    print(f"solved: {eval(op)}")


print('goodbye!')
