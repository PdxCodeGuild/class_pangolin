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

def reverselist(nums):
    return nums[-1::-1]

# print(reverselist([1,2,3]))

def extract_less_than_ten(nums):
    return [num for num in nums if num < 10]
    
# print(extract_less_than_ten([12,1,23,2,10,11,3,14]))

def combine(nums1, nums2):
    new_list = []
    for i in range(0,len(nums1)):
        new_list.append(nums1[i])
        new_list.append(nums2[i])
    return new_list

# print(combine(['a','b','c'],[5,10,15])) #→ ['a', 1, 'b', 2, 'c', 3]

def find_pair(nums, target):
    return_list = []
    for x in nums:
        pair_num = target - x
        if pair_num in nums:
            nums.remove(pair_num)
            return_list.append([x,pair_num])
    return return_list

# nums = [5, 6, 2, 3]
# target = 7
# print(find_pair(nums, target)) # → [5, 2]

def combine_all(nums):
    new_list = []
    
    for lst in nums:
        for num in lst:
            new_list.append(num)
    
    return new_list

# nums = [[5,2,3],[4,5,1],[7,6,3]]
# print(combine_all(nums)) #→ [5,2,3,4,5,1,7,6,3]

def minimum(nums):
    min = nums[0]
    for num in nums:
        if num < min:
            min = num
    return min

def maxmimum(nums):
    max = nums[0]
    for num in nums:
        if num > min:
            max = num
    return max

def mean(nums):
    sum = 0
    for num in nums:
        sum += num
    return float(sum/len(nums))

def mode(nums): # (OPTIONAL)
    max_char = nums[0]
    max_count = nums.count(nums[0])

    for num in nums:
        if nums.count(num) > max_count:
            max_char = num
            max_count = nums.count(num)
    
    return max_char

# print(min([1,2,3,0])) 
# print(max([1,2,3,0]))
# print(mean([1,2,3,0]))
# print(mode([1,3,2,3,3]))

def find_unique(nums):
    return_list = []

    for num in nums:
        if num not in return_list:
            return_list.append(num)

    return return_list

nums = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
unique_nums = find_unique(nums) 
print(unique_nums) # → [12, 24, 35, 88, 120, 155]