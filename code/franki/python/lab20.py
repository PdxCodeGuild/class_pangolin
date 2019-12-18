
# nums = [4, 5, 6, 7, 3, 1, 2, 1, 7, 9, 9, 4, 2, 8, 7, 0]
nums = []
while len(nums) != 16:
    nums = list(input("Please enter your 16-digit number. "))
nums = [int(num) for num in nums]

# print(f"List: {nums}")
check_digit = nums[15]
# print(f"check digit: {check_digit}")
nums.reverse()
nums.remove(nums[0])
# print(f"Reversed: {nums}")
# x = 0
# while x <= 14:
#     nums = [nums[x] * 2 for nums[x] in nums if x % 2 == 0 else nums[x] for nums[x] in nums]
#aaaaaaagh I give up! It doesn't make sense!
x = 0
for num in nums:
    while x <= 14:
        nums[x] = nums[x] * 2
        x = x + 2
# print(f"Doubled: {nums}")


nums = [num - 9 if num > 9 else num for num in nums]

# print(f"Minus 9: {nums}")
sum = sum(nums)
# print(f"Sum: {sum}")
sum_digits = [int(x) for x in str(sum)]
# print(sum_digits[1])
if sum_digits[1] == check_digit:
    print(f"{sum_digits[1]} = {check_digit}")
    print("That card is valid.")
else:
    print(f"{sum_digits[1]} /= {check_digit}")
    print("That card is invalid.")
# print(nums)
