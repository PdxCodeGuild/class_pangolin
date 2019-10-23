'''
simple calculator lab 01
written by Rhornberger
last updated oct 23 2019
'''
op = input('What mathmatical operation would you like to perform?: ')
num1 = int(input('What is the first number you would like to enter?: '))
num2 = int(input('What is the second number you would like to enter?: '))
#num1 = [int(i) for i in num1]
#num2 = [int(i) for i in num2]
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
