# lab_10a.py
# Jeff Smith
# 10/23/19
# Average user-submitted numbers 

import math
nums = []

ele = input('Enter a number or type done: ').lower()
if ele == 'done':
    print('Ok. Perhaps another time.')

while ele != 'done': 
    nums.append(ele)
    ele = input('Enter a number or type done: ').lower()

nums = [int(i) for i in nums]

print(sum(nums)/len(nums))