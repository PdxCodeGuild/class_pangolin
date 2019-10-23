# lab_10.py
# Jeff Smith
# 10/23/19
# Average numbers
import math
nums = [5, 0, 8, 3, 4, 1, 6]

#for [i] in nums:
#    print(num)

#for i in range(len(nums)):
#    print(nums[i])

#i = 0
for i in range(len(nums)):
    print(sum(nums)/len(nums))

squares = [i**2 for i in range(1,11)]
print(squares)
print(list(range(1,11)))

distances_km = [round(distance * 1.6, 1) for distance in distances]