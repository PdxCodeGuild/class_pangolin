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
cc_input = input("Please input the CC number: ")
cc_input = [int(i) for i in cc_input]
print(f"The original list {cc_input}")

check_digit = cc_input.pop()
print(f"The check digit is {check_digit}")

cc_input = list(reversed(cc_input))
print(f"The reversed list {cc_input}")

doubles = [x * 2 for x in cc_input]
print(f"The doubled list is {doubles}")

