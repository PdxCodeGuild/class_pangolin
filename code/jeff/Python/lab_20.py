# lab_20.py
# Jeff Smith
# CC validation
# Let's write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:

#     1. Convert the input string into a list of ints
#     2. Slice off the last digit. That is the check digit.
#     3. Reverse the digits.
#     4. Double every other element in the reversed list.
#     5. Subtract nine from numbers over nine.
#     6. Sum all values.
#     7. Take the second digit of that sum.
#     8. If that matches the check digit, the card number is valid.

import math

# testing.py
# Workspace for labs
# Jeff Smith

cc = '4556737586899855'

# !. Convert the input string into a list of ints
ccint = [int(x) for x in '4556737586899855']
# print(ccint) # verify the string converst to list

# 2. Slice off last digit. 
ckdg = (ccint[slice(-1)])
slob = ccint[-1]
# print(ckdg) #verify the truncated card number after slice
# print(slob) #verify the sliced number from the card number

# 3. Reverse the digits.
revckdg = ckdg[::-1]
# print(revckdg)

# 4. Double every other element in the reversed list.
double = revckdg[:]
double = [double[index]*2 if index % 2 == 0 else double[index] for index in range(len(double))]
print(double)

# 5. Subtract nine from numbers over nine.
nine = double[:]
nine = [nine[index]-9 if index >= 0 else nine[index] for index in range(len(nine))]

print(nine)

# 6. Sum all values.

# 7. Take the second digit of that sum.

# 8. If that matches the check digit, the card number is valid.
