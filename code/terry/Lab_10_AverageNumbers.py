# Average a list of numbers.

numbers = [5, 0, 8, 3, 4, 1, 6]
outPut = 0
for num in numbers:
    outPut += num

outPut = outPut / len(numbers)
outPut = round(outPut, 2)
print(outPut)

# Average a list of numbers entered by the user.

numbers2 = []
userInput = ""
finish = True

while finish:
    userInput = input("Please enter a number or 'Done' to finish. ")
    if userInput == 'Done':
        finish = False
    else:
        numbers2.append(userInput)

print(userInput)
print(numbers2)