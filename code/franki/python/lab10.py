nums = []
user_input = input("enter a number, or 'done': ")
while user_input != "done":
    nums.append(float(user_input))
    user_input = input("enter a number, or 'done': ")

running_sum = 0
place = 0
while place < len(nums):
    for num in nums:
        running_sum = nums[place] + running_sum
        place += 1

average = round(running_sum / len(nums), 3)
print(f"The average is {average}")
