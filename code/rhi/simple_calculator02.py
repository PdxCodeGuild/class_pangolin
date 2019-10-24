'''
simple calculator lab 2
written by Rhornberger
last updated oct 24 2019
'''
op = input('What mathmatical operation would you like to perform?: ')
num1 = int(input('What is the first number you would like to enter?: '))
num2 = int(input('What is the second number you would like to enter?: '))

if op == '+':
    result = (num1 + num2)
    result = round(result, 3)
    print(f'{num1} {op} {num2} = {result}')
elif op == '-':
    result = (num1 - num2)
    result = round(result, 3)
    print(f'{num1} {op} {num2} = {result}')
elif op == '*':
    result = (num1 * num2)
    result = round(result, 3)
    print(f'{num1} {op} {num2} = {result}')
elif op == '/':
    result = (num1 / num2)
    result = round(result, 3)
    print(f'{num1} {op} {num2} = {result}')
elif op == '//':
    result = (num1 // num2)
    result = round(result, 3)
    print(f'{num1} {op} {num2} = {result}')
elif op == '%':
    result = (num1 % num2)
    result = round(result, 3)
    print(f'{num1} {op} {num2} = {result}')
elif op == '**':
    result = (num1 ** num2)
    result = round(result, 3)
    print(f'{num1} {op} {num2} = {result}')
else:
    print('not a valid operation!')
    

     
user_input = input('Would you like to perform more math? Or you can enter done to be finished: ')
while user_input != 'done':
    op = input('Please choose and operation: ')
    num1 = int(input('What is the first number you would like to enter?: '))
    num2 = int(input('What is the second number you would like to enter?: '))
    
    
    if op == '+':
        result = (num1 + num2)
    elif op == '-':
        result = (num1 - num2)
    elif op == '*':
        result = (num1 * num2)
    elif op == '/':
        result = (num1 / num2)
    elif op == '//':
        result = (num1 // num2)
    elif op == '%':
        result = (num1 % num2)
    elif op == '**':
        result = (num1 ** num2)
    else:
        print('not a valid operation!')
    
    result = round(result, 3)
    print(f'{num1} {op} {num2} = {result}')
    user_input = input('Would you like to perform more equations? Or enter done to be finished: ')

print('thank you!')

