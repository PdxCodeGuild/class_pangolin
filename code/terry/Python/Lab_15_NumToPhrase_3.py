num_dict = {0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight",
            9: "Nine",
            10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen",
            17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty",
            60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety", 100: "Hundred"}

userInput = input("Enter the number to be converted to English. ")
userInputInt = int(userInput)
ifTen = False
if100 = False
ifOnes = False
isSpecial = False

userInputStr = list(userInput)
# print(userInputStr)
userInputLst = [int(x) if x != 0 else x for z in userInputStr for x in str(z)]
# print(userInputLst)

if userInputInt >= 100:
    if100 = True
elif userInputInt <= 99 and userInputInt > 9:
    ifTen = True
else:
    ifOnes = True

i = 0
result = []
if if100:
    num1 = int(userInputStr[0])
    if num1 in num_dict:
        result.append(num_dict[num1])
    num2 = int(userInputStr[1])
    num3 = int(userInputStr[2])
    if num2 != 0:
        num2 *= 10
        if num2 in num_dict:
            result.append(num_dict[num2])
    if num3 in num_dict:
        result.append(num_dict[num3])
        i += 1
    result.insert(1, "Hundred")

if ifTen:
    num1 = int(userInputStr[0])
    num1 *= 10
    print(num1)
    if num1 in num_dict:
        result.append(num_dict[num1])
    num2 = int(userInputStr[1])
    print(num2)
    if num2 != 0:
        num2 *= 10
        if num2 in num_dict:
            result.append(num_dict[num2])
    num4 = num1 + num2
    if num4 >= 10 and num4 <=19:
        if num4 in num_dict:
            result.append(num_dict[num4])
            i += 1
    else:
        print("error")

if ifOnes:
    num1 = int(userInputStr[0])
    if num1 in num_dict:
        result.append(num_dict[num1])
        i += 1

separate = ' '
outPut = separate.join(result)
print(outPut)
