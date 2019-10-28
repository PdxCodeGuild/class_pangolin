num = int(input("Enter a number between 0-99:  "))
tens = num // 10
ones = num % 10
tens_to_word = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
ones_to_word = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine",]
teens_to_word = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "ninteen" ]

if num == 0:
    result = "zero"
elif num in range(10):
    result = ones_to_word[num - 1]
elif num in range(11, 20):
    result = teens_to_word[ones - 1]
else:
    if ones > 0:
        result = tens_to_word[tens - 1] + "-"  + ones_to_word[ones - 1]
    else:
        result = tens_to_word[tens - 1]

print(result)
