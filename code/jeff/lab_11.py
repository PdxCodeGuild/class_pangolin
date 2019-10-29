#testing.py
#this is for lab workspace

import math

# Print greeting

print('Welcome to the Great Calculator!')

# Get first operand and convert to integer
o1 = int(input('Enter a number or type done: '))
if o1 == 'done':
    print('Ok. Perhaps another time.')
if o1 != 'done': 
    op = input('Select an operation (+, -, *, /) or done : ')
if op == 'done':
    print('No worries.')
if op != 'done':
    o2 = int(input('Enter a number or type done: '))
if o2 == 'done':
    print('Ok. See you.')

# Convert operand2 from int to float
# 

# Execute calculation
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