message1 = "enter a number, or "

nums = [5, 0, 8, 3, 4, 1, 6]

sums = 0
for i in range(len(nums)):
    sums += nums[i]
    average = sums / len(nums)

print(sums)
print(average)