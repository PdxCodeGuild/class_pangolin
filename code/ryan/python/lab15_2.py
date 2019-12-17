num = int(input("Enter a number between 100-999:  "))
hundreds = num // 100
tens = (num - (hundreds * 100))  // 10
ones = num % 10
tens_to_word = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
ones_to_word = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine",]
teens_to_word = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "ninteen" ]
hundred_to_word = ["hundred"]

if tens == 0 and ones > 0:
    result = ones_to_word[hundreds - 1] + " " + hundred_to_word[0] + " " + ones_to_word[ones - 1]
elif tens == 0 and ones == 0:
    result = ones_to_word[hundreds - 1] + " " + hundred_to_word[0]
elif ones == 0:
    result =  ones_to_word[hundreds - 1] + " " + hundred_to_word[0] + " " + tens_to_word[tens-1]
elif tens == 1 and ones > 0:
    result =  ones_to_word[hundreds - 1] + " " +  hundred_to_word[0] + " " + teens_to_word[ones - 1]
else:
    result = ones_to_word[hundreds - 1] + " " + hundred_to_word[0] + " " + tens_to_word[tens - 1] + "-" + ones_to_word[ones - 1]

print(result)
