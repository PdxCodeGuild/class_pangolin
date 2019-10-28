'''
Lab 11: Simple Calculator - Version 2

Purpose/goal: Allow the user to keep performing operations until they say 'done'. Use while True and break. Below is some sample input/output. - D

'''

# define ops
ops = ["+", "-", "*", "/"]

# user greeting
print("Hello!\nThis is a simple calculator.\n")

# define user op
op = input("What is the operation you'd like to perform? (+, -, * or /): ")

if op not in ops:
    op = input("Please select one of these operations (+, -, * or /): ")

# define user nums
while op in ops:       
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

    op = input("\nWhat is the operation you'd like to perform? (+, -, * or /): ").lower()
    if op == "done":
        break

# end
print("\nThank you for using this simple calculator.\nGoodbye!")