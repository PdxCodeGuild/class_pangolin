nums = []
sum = 0
number = (input("Please enter a number:  "))

while number != "done":
    number = int(number)
    nums.append(number)
    number = (input("Please enter a number, or 'done' when finished:  "))
else:
    for num in nums:
        sum += num
        avg = sum / len(nums)

print(f"The average of these numbers is:  {avg}")
