'''
simple calculator lab 01
written by Rhornberger
last updated oct 23 2019
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
print('Thank you and we hope to see you again!')
