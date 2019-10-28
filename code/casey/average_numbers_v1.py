'''
Lab 10: Average Numbers - Version 1

Purpose/goal: Average a list of numbers. 
    
    - Start with the following list: nums = [5, 0, 8, 3, 4, 1, 6] - D
    
    - Iterate through it, keeping a 'running sum' - D
    
    - Divide that sum by the number of elements in that list. - D

'''
# iterate over list
nums = [5, 0, 8, 3, 4, 1, 6]

# loop over the elements
for num in nums:
    print(num)

# sum of nums
run_sum = sum(nums)
print(run_sum)

# find average
print(run_sum / len(nums))
