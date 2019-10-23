# Shawn Stolsig
# PDX Code Guild 
# Assignment: Lab 10 - Average Numbers
# Date: 10/23/2019

# # list of nums for version 1
# nums = [5, 0, 8, 3, 4, 1, 6]

# create list for nums
nums = []

# use while loop to get input until user types done
not_done = True

while not_done:
    num = input("input a number or \"done\": ")
    if num == 'done':
        not_done = False
    else:
        nums.append(float(num))


# initialize sum variable to 0
sum = 0

# iterate through list, adding each element to sum
for i in nums:
    sum += i

# print your list and average
print(f"your list is {nums}")
print(f"your average is {sum / len(nums)}")
