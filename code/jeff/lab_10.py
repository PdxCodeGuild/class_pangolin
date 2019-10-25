# lab_10.py
# Jeff Smith
# 10/23/19
# Average numbers

import math

nums = [5, 0, 8, 3, 4, 1, 6]

for i in range(len(nums)):
    avg = (sum(nums)/len(nums))
avg = round(avg, 1)
print(avg)