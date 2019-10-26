num_dict = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
            10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen",
            17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty",
            60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety", 100: "Hundred"}

userInput = input("Enter the number to be converted to English. ")
userInputInt = int(userInput)
# outPut = []
ifTen = False
if100 = False

userInputStr = list(userInput)
print(userInputStr)
userInputLst = [int(x) if x != 0 else x for z in userInputStr for x in str(z)]
print(userInputLst)

if userInputInt >= 100:
    if100 = True
    num1 = int(userInputLst[0])
    num2 = int(userInputLst[1])
    num3 = int(userInputLst[2])

elif userInputInt <= 99 and userInputInt > 9:
    ifTen = True
    num1 = int(userInputLst[0])
    num2 = int(userInputLst[1])
else:
    num1 = int(userInputLst[0])

i = 0
testWord2 = []
if if100:
    num1 = int(userInputStr[0])
    if num1 in num_dict:
        testWord2.append(num_dict[num1])
    num2 = int(userInputStr[1])
    num2 *= 10
    if num2 in num_dict:
        testWord2.append(num_dict[num2])
    num3 = int(userInputStr[2])
    if num3 in num_dict:
        testWord2.append(num_dict[num3])
        i += 1
    testWord2.insert(1, "Hundred")
# testWord = [[i] for i in outPut]
print(testWord2)
