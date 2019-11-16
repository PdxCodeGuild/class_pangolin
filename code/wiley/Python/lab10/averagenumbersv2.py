#Ask the user to enter the numbers one at a time, putting them into a list.
#If the user enters 'done', then calculate and display the average. 
#The following code demonstrates how to add an element to the end of a list.
nums =[] #empty list to work with
#while loop to get the user generated list and break with 'done' command.
while True:
    ask = input("add a number or type 'done'.")
    if ask == 'done':
        break
    nums.append(int(ask))

total = 0 #total variable to find the average
for num in nums:
    total += num
print(f"{total} is the sum of the list 'nums'.")
average = total/len(nums)

# divide by the number of elements
print(f"{average} is the average of the list 'nums'.")
