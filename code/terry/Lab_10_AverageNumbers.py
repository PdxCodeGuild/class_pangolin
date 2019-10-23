# Average a list of numbers.

numbers = [5, 0, 8, 3, 4, 1, 6]
outPut = 0
for num in numbers:
    outPut += num

outPut = outPut / len(numbers)
outPut = round(outPut, 2)
print(outPut)


