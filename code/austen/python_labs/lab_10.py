
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


# check if they are done first then go and continue so switch line 7 and 8 and get rid of the break

# on line 17 you need to put str(average) so that you can concatinate if you leave it as a float then it just adds it. also you should have put a + insted of the , 

# another example of line 17 is print(f'average: {average}')
    






    

    

