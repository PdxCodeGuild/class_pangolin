# Average of numbers in an array.
# This is version 1 as described in the lab.
"""
numbers = [5, 0, 8, 3, 4, 1, 6]
i = len(numbers)
#print(i)
k = sum(numbers)
#print(k)
avg = k/i
avg = float(round(avg, 2))
print(avg)
"""

# Allow the user to enter numbers and them average them.
# Version 2.

numbersArray = []
userNumber = int(input("Please enter a number to average. "))
numbersArray.append(userNumber)

while userNumber > 0:

    userNumber = input("Please enter a number to average. Type 'done' to end. ").lower()
    if userNumber == "done":
        break
    else:
        userNumber = int(userNumber)
        numbersArray.append(userNumber)

i = len(numbersArray)
# print(numbersArray)
k = sum(numbersArray)
# print(k)
# print(i)
avg = k / i
avg = float(round(avg, 2))
print(f"The average of the numbers is: {avg}")
