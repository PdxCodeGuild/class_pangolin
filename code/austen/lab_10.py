
nums = []
total = 0

while True:
    user_input = input('enter a number, or enter *done*: ')
    nums.append(user_input) #after talking we discussed this could go by break
    if user_input == 'done':
        nums.pop() #un needed in if you put the .append() by the break
        print (nums)
        break
for num in nums:
    total += int(num)
print('sum is', total)

average = total / len(nums)
print('the average is', average)

    






    

    

