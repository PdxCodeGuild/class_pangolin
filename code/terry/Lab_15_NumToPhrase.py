# Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99

toBeConverted = input("Type a number to be converted to English. ")

outputSpecial = ""
outputTens = ""
outputOnes = ""

userInput = list(toBeConverted)
userInput = [int(x) if x != 0 else x for z in userInput for x in str(z)]
print(userInput)
#for i in userInput:
if int(toBeConverted) >= 10:
    num2 = int(userInput[0])
    num1 = int(userInput[1])
else:
    num2 = int(userInput[0])

isTen = int(toBeConverted)

if isTen <= 19 and isTen > 9:
    if isTen == 10:
        outputSpecial = "Ten"
    elif isTen == 11:
        outputSpecial = "Eleven"
    elif isTen == 12:
        outputSpecial = "Twelve"
    elif isTen == 13:
        outputSpecial = "Thirteen"
    elif isTen == 14:
        outputSpecial = "Fourteen"
    elif isTen == 15:
        outputSpecial = "Fifteen"
    elif isTen == 16:
        outputSpecial = "Sixteen"
    elif isTen == 17:
        outputSpecial = "Seventeen"
    elif isTen == 18:
        outputSpecial = "Eighteen"
    elif isTen == 19:
        outputSpecial = "Nineteen"
elif isTen >= 20:
    # userInput = list(userInput)
    # userInput = [int(x) if x != 0 else x for z in userInput for x in str(z)]
    # print(userInput)
    #
    # for i in userInput:
    #     num2 = int(userInput[0])
    #     num1 = int(userInput[1])

    # print(num2)
    # print(num1)

# num1 is the Tens, num2 is the Single

    if num2 == 2:
        outputTens = "Twenty"
    elif num2 == 3:
        outputTens = "Thirty"
    elif num2 == 4:
        outputTens = "Forty"
    elif num2 == 5:
        outputTens = "Fifty"
    elif num2 == 6:
        outputTens = "Sixty"
    elif num2 == 7:
        outputTens = "Seventy"
    elif num2 == 8:
        outputTens = "Eighty"
    elif num2 == 9:
        outputTens = "Ninety"

elif isTen <= 9:
    if num2 == 1:
        outputOnes = "One"
    elif num2 == 2:
        outputOnes = "Two"
    elif num2 == 3:
        outputOnes = "Three"
    elif num2 == 4:
        outputOnes = "Four"
    elif num2 == 5:
        outputOnes = "Five"
    elif num2 == 6:
        outputOnes = "Six"
    elif num2 == 7:
        outputOnes = "Seven"
    elif num2 == 8:
        outputOnes = "Eight"
    elif num2 == 9:
        outputOnes = "Nine"

print(outputSpecial)
print(outputTens)
print(outputOnes)
