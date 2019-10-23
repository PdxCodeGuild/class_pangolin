# Average a list of numbers.

numbers = [5, 0, 8, 3, 4, 1, 6]
outPut = 0
for num in numbers:
    outPut += num

outPut = outPut / len(numbers)
outPut = round(outPut, 2)
print("Version 1")
print(outPut)

# Average a list of numbers entered by the user.

numbers2 = []
userInput = ""
outPut2 = 0
finish = True

print("\nVersion 2")
while finish:

    userInput = input("Please enter a number or 'Done' to finish. ")
    if userInput.lower() == 'done':
        finish = False
    else:
        numbers2.append(userInput)
        outPut2 += int(userInput)

outPut2 = outPut2 / len(numbers2)
outPut2 = round(outPut2, 2)

print(f"The average of the numbers is: {outPut2}")