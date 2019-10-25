num_dict = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
            10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen",
            17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty",
            60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety", 100: "Hundred"}

userInput = input("Enter the number to be converted to English. ")
userInputInt = int(userInput)
outPut = []

userInputStr = list(userInput)
print(userInputStr)
userInputLst = [int(x) if x != 0 else x for z in userInputStr for x in str(z)]
print(userInputLst)

print(len(userInputStr))

for x in range(len(userInputStr)):
    if userInputInt in num_dict:
        outPut.append(num_dict[userInputInt])

print(outPut)
