#convert numerals to english number phrases

tens_phrase = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
ones_phrase = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
def phraseify(a):
    tens_digit = x // 10
    ones_digit = x % 10
    if tens_digit == 0:
        result = ones_phrase[ones_digit]
        return result
    elif tens_digit == 1:
        result = ones_phrase[x]
        return result
    elif tens_digit > 1:
        if ones_digit == 0:
            result = tens_phrase[tens_digit]
        else:
            result = tens_phrase[tens_digit] + "-" + ones_phrase[ones_digit]
        return result
while True: 
    user_input = (input("Enter a number between 0 and 99, or 'done'. "))
    if user_input == "done":
        break
    x = int(user_input)
    if x in range(0,100):
        print(phraseify(x))
print("Bye!")