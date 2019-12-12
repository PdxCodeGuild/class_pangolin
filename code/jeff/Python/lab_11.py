# testing.py
# this is for lab workspace

import math

# Print greeting

print('Welcome to the Great Calculator!')

ops = ['+', '-', '*', '/']

while True:
    # Get first operand and convert to integer
    op = input('Select an operation (+, -, *, /) or done : ')
    if op == 'done':
        break
    elif op in ops:
        o1 = int(input('Enter your first number: '))
        o2 = int(input('Enter your second number: '))
    if (op == "-"):
        sol = o1 - o2
        print(f'The answer to {o1} - {o2} = {sol}')
    if (op == "+"):
        sol = o1 + o2
        print(f'The answer to {o1} + {o2} = {sol}')
    if (op == "*"):
        sol = o1 * o2
        print(f'The answer to {o1} * {o2} = {sol}')
    if (op == "/"):
        sol = o1 / o2
        print(f'The answer to {o1} / {o2} = {sol}')
