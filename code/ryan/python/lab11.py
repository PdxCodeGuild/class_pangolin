operators = ["+", "-", "*", "/"]
operation = input("What is the operation you would like to perform?(+, -, *, /):  ")

while operation not in operators:
    operation = input("Invalid input.  Please choose +, -, *, /:  ")

num1 = int(input("What is the first number?  "))
num2 = int(input("What is the second number?  "))

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
else:
    result = num1 / num2

print(f"Your result is:  {num1} {operation} {num2} = {result}.")
