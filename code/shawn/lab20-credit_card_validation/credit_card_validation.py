# Shawn Stolsig
# PDX Code Guild 
# Assignment: Lab 20 - Credit Card Validation
# Date: 10/23/2019

# sample number from lab assignment
# sampleNum = str(4556737586899855)
sampleNum = input("please input a sample number: ")

# define function for validating credit card info is correct
def checkCard(numStr):

    # 1. turn input string into list of numbers
    numList = [int(i) for i in numStr]
    print(numList)

    # 2. Slice off the last digit. That is the check digit.
    checkDigit = numList.pop()
    print(numList)

    # 3. Reverse the digits.
    numList.reverse()
    print(numList)

    # 4. Double every other element in the reversed list.
    numList = [numList[i]*2 if i % 2 == 0 else numList[i] for i in range(0,len(numList))]
    print(numList)

    # 5. Subtract nine from numbers over nine.
    numList = [num-9 if num > 9 else num for num in numList]
    print(numList)

    # 6. Sum all values.
    sum = 0
    for i in range(len(numList)):
        sum += numList[i]
   
    # 7. Take the second digit of that sum
    print(f"check digit is {checkDigit}")
    print(f"sum is {sum}")
    # 8. If that matches the check digit, the whole card number is valid.
    return str(checkDigit) == str(sum)[1]

if checkCard(sampleNum):
    print("Valid!")
else:
    print("Not valid :(")