operators = ["+", "-", "*", "/"]
operation = ""

while True:
    operation = input("What is the operation you would like to perform?(+, -, *, /, or 'done' to quit):  ")

    if operation == "done":
        break
    elif operation not in operators:
        print("Invalid input.  Please choose +, -, *, /, or 'done'.")
    else:
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

print("Goodbye!!")
