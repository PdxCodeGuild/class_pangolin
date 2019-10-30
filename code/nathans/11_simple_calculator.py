# simple_calculator.py

user_input_op = input("Chose the operation to perform. Enter +, -, *, or / : ")
first_num = float(input("What is the first number?: "))
second_num = float(input("What is the second number?: "))

#op = ['+', '-', '*', '/']

if user_input_op == '+':
    print(first_num + second_num)

elif user_input_op == '-':
     print(first_num - second_num)

elif user_input_op == '*':
    print(first_num * second_num)

elif user_input_op == '/':
    print(first_num / second_num)



