# practic.py
# Workspace for labs
# Jeff Smith

#Problem 1

# #Write a function that tells whether a number is even or odd
# #(hint, compare a/2 and a//2, or use a%2)
# def is_even(a):
#     if (a%2 == 0):
#          return 'its even!' #initially tried 'print' here and got 
#     return 'its odd!'       #'none on double-digits
#                             #     pass # Even 
#                             # else:
#                             #     pass # Odd   
# # print(is_even(8))
# # print(is_even(9))
# # print(is_even(86))
# ###########################
# # Problem 2

# # Write a function that takes two ints, a and b, and returns True if one is positive and the other is negative.
# def opposite(a, b):
#     if (a < 0) and (b < 0):
#         return 'False'
#     elif (a < 0) or (b < 0):
#         return 'True' 
#     return 'False'

# print(opposite(5, 2)) 
# print(opposite(-5, 2)) 
# print(opposite(-5, -2))

# ############################
# # Problem 3

# # Write a function that returns True if a number within 10 of 100.

# def near_100(num):
#     if num in range(90, 100):
#         return 'True!'
#     elif num in range(101, 111):
#         return 'True'
#     return 'False!'

# print(near_100(75))
# print(near_100(99))
# print(near_100(125))
# #########################

# Problem 4
# Write a function that returns the maximum of 3 parameters.
# def sel(a, b, c):
#     sel1 = [a, b, c]
#     sel2 = sorted(sel1)
#     sel3 = sel2.pop()
#     return sel3

# print(sel(5, 3, 9))
##################
# Problem 5

# Print out the powers of 2 from 2^0 to 2^20

# def exp(a):
#     if a in range(2,21):
#         res = 2 ** a
#         return res
#     return 'out of range'
# print(exp(30))
