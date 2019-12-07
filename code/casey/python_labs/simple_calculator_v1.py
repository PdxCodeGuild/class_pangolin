'''
Lab 11: Simple Calculator - Version 1

Purpose/goal: Write a simple REPL (read evaluate print loop) calculator that can handle addition, subtraction, multiplication, and division. Ask the user for an operator and each operand. - D

'''

# define ops
ops = ["+", "-", "*", "/"]

# user greeting
print("\nHello!\nThis is a simple calculator.\n")

# define user op
op = input("What is the operation you'd like to perform? (+, -, * or /): ")

while op not in ops:
    op = input("Please select an operation from this list (+, -, * or /): ")
    if op in ops:
        break

# define user nums        
num1 = float(input("What is your first number?: "))
num2 = float(input("What is your second number?: "))

if op == "+":
    a = num1 + num2
if op == "-":
    a = num1 - num2   
if op == "*":
    a = num1 * num2    
if op == "/":
    a = num1 / num2
    
# give user answer
print(f"{num2} {op} {num2} = {a}")

# end
print("\nThank you for using this simple calculator.\nGoodbye!")