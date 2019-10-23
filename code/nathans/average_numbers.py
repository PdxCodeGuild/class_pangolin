# average_numbers.py
nums = [5, 0, 8, 3, 4, 1, 6]

nums_sum = 0
for num in nums:
   nums_sum = nums_sum + num

average = nums_sum / len(nums)

print(average)


