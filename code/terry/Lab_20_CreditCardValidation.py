# Design a credit card validator
"""
Convert the input string into a list of ints
Slice off the last digit. That is the check digit.
Reverse the digits.
Double every other element in the reversed list.
Subtract nine from numbers over nine.
Sum all values.
Take the second digit of that sum.
If that matches the check digit, the whole card number is valid.

Other notes:
Amex is 15 digits
all others are 16 digits
no alpha needed in this lab

"""
check_digit = 0
cc_input = 0
card_valid = True
cc_input = input("Please input the CC number: ")
cc_input = [int(i) for i in cc_input]
print(f"The original list is: {cc_input}")

check_digit = cc_input.pop()
print(f"The check digit is: {check_digit}")

revlst = list(reversed(cc_input))
print(f"The reversed list is: {revlst}")

doubled = [d * 2 if i % 2 == 0 else d for i, d in enumerate(revlst)]
print(f"The doubled list is: {doubled}")

cc_input = [n - 9 if n > 9 else n for n in doubled]
print(f"The 'nine' list is: {cc_input}")

inputSum = sum(cc_input)
print(f"The sum of the list is: {inputSum}")

inputSum = [inputSum]

inputSum = [int(x) if x != 0 else x for z in inputSum for x in str(z)]

inputSum = inputSum[1]

if inputSum == check_digit:
    card_valid = True
else:
    card_valid = False
print(f"The check digit is: {check_digit}")
print(f"The second digit of the sum is: {inputSum}")
print(f"Is the card valid? {card_valid}")
