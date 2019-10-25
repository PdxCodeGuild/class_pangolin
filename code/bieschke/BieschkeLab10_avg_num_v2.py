#Lab10 Average Numbers 
'''
Ask the user to enter the numbers one at a time, putting them into a list. 
If the user enters 'done', then calculate and display the average. 
'''

tiger = True
print("Hello! We're going to ask you for some numbers today!")
print("You can finish the list at any time by entering nothing.")

nums = []
avg = []

while tiger is True:
    lion = input("Give me a number:\n>")
    
    if lion == '':
        tiger = False
        break

    else:
        lion = int(lion)
        nums.append(lion)

for num in nums:
    avg.append(num)
    sum(avg)
    bears = (sum(avg)) / (len(avg))

print(f"The sum of your entries is {sum(avg)}")
print(f"The average value of your entries is {(sum(avg)) / (len(avg))}")
print("Sayonara!")