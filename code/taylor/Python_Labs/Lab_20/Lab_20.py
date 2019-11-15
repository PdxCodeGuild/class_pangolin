# Taylor Rebbe
# PDX Code Guild
# Lab 20 Complete

# Message variable
message1 = "\nPlease enter a 16 digit credit card number: >  "

#Convert the input string into a list of ints
user_input1 = list(input(message1).replace(' ',''))
cc_num_usr = [int(i) for i in user_input1]

#Slice off the last digit. That is the check digit.
cc_num_chk = cc_num_usr.pop(-1)

# Reverse the digits.
cc_num_rev = cc_num_usr[::-1]

#Double every other element in the reversed list.
cc_num_dbl = [num * 2 if i % 2 == 0 else num for i, num in enumerate(cc_num_rev)]

#Subtract nine from numbers over nine.
cc_num_nin = [num - 9 if num > 9 else num for i, num in enumerate(cc_num_dbl)]

#Sum all values.
cc_num_sum = 0
for i in range(len(cc_num_nin)):
    cc_num_sum += cc_num_nin[i]

# Convert sum to a list for check
sum_to_lst = list(str(cc_num_sum))

# If that matches the check digit, the whole card number is valid.
if int(sum_to_lst[1]) == cc_num_chk:
    print("\nValid!")

