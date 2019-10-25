# Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99

toBeConverted = input("Type a number to be converted to English. ")

outputSpecial = ""
outputTens = ""
outputOnes = ""
isSpecial = False
isOne = False
isLarge = False


userInput = list(toBeConverted)

userInput = [int(x) if x != 0 else x for z in userInput for x in str(z)]

if int(toBeConverted) >= 10:
    num2 = int(userInput[0])
    num1 = int(userInput[1])
else:
    num1 = int(userInput[0])

isTen = int(toBeConverted)
if isTen <= 9:
    isOne = True
    num1 = int(userInput[0])
elif isTen <= 19 and isTen > 9:
    isSpecial = True
    num2 = int(userInput[0])
    num1 = int(userInput[1])
elif isTen >= 20:
    isLarge = True
    isOne = True
    num2 = int(userInput[0])
    num1 = int(userInput[1])

if isSpecial:
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

if isLarge:
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

if isOne:
    if num1 == 1:
        outputOnes = "One"
    elif num1 == 2:
        outputOnes = "Two"
    elif num1 == 3:
        outputOnes = "Three"
    elif num1 == 4:
        outputOnes = "Four"
    elif num1 == 5:
        outputOnes = "Five"
    elif num1 == 6:
        outputOnes = "Six"
    elif num1 == 7:
        outputOnes = "Seven"
    elif num1 == 8:
        outputOnes = "Eight"
    elif num1 == 9:
        outputOnes = "Nine"
    elif num1 == 0:
        outputOnes = "Zero"

if outputSpecial:
    print(outputSpecial)
if isLarge:
    if outputOnes == "" or outputOnes == "Zero":
        print(outputTens)
    elif outputOnes != "Zero":
        print(f"{outputTens}-{outputOnes}")
elif isOne:
    print(outputOnes)
