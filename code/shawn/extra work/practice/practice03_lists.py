# Shawn Stolsig
# PDX Code Guild 
# Assignment: Practice 3 - List
# Date: 10/25/2019

import random

def random_element(a):
    return a[random.randint(0,len(a)-1)]

# fruits = ['apples', 'bananas', 'pears']
# print(random_element(fruits)) #could return 'apples', 'bananas' or 'pears'

def enter_until_done():
    empty_list = []
    while True:
        user_input = input('Enter a number (or done): ')
        if user_input == 'done':
            break
        empty_list.append(user_input)
    return empty_list

# print(enter_until_done())

def eveneven(nums):
    counter = 0
    for num in nums:
        if num % 2 == 0:
            counter += 1
    return counter % 2 == 0

# print(eveneven([5, 6, 2])) # → True
# print(eveneven([5, 5, 2])) # → False