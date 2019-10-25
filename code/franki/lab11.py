running = True
while running == True:
    user_input = input("What is the operation you'd like to perform?")
    if user_input in ["Done", "done"]:
        break
    elif user_input not in ["X", "x", "-", "/", "+", "*"]:
        print("Sorry, that is not a valid operation.")
        user_input = input("What is the operation you'd like to perform? (if done, type 'done') ")
        if user_input in ["done", "Done"]:
            break

    num1 = input("What is the first number?")
    num2 = input("What is the second number?")

    if user_input in ["X", "x", "*"]:
        calculation = float(num1) * float(num2)
        operator = "*"
    elif user_input == "/":
        calculation = float(num1) / float(num2)
        operator = "/"
    elif user_input == "+":
        calculation = float(num1) + float(num2)
        operator = "+"
    elif user_input == "-":
        calculation = float(num1) - float(num2)
        operator = "-"
    calculation = round(calculation, 4)
    print(f"{num1} {operator} {num2} = {calculation}")
print("Bye-bye.")
