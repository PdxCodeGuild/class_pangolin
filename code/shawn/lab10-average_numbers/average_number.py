# Shawn Stolsig
# PDX Code Guild 
# Assignment: Lab 10 - Average Numbers
# Date: 10/23/2019

# list of nums
nums = [5, 0, 8, 3, 4, 1, 6]

# initialize sum variable to 0
sum = 0

# iterate through list, adding each element to sum
for i in nums:
    sum += i

# print average
print(f"your average is {sum / len(nums)}")
