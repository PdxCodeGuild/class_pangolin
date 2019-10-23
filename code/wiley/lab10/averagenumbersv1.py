#find the average of a list of numbers
#Start with the following list, iterate through it, 
#keeping a 'running sum', then divide that sum by the number of elements in that list. 
#Remember len will give you the length of a list.
nums = [5,0,8,3,4,1,6]
#make a running sum
total = 0
for num in nums:
    total += num
print(f"{total} is the sum of the list 'nums'.")
average = total/len(nums)

# divide by the number of elements
print(f"{average} is the average of the list 'nums'.")