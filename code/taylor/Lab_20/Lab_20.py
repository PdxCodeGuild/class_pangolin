message1 = "Please enter a 16 digit credit card number: >  "

cc_num_tst = [4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 9999]
print(len(cc_num_tst))

#Convert the input string into a list of ints
user_input1 = list(input(message1))
cc_num_usr = [int(i) for i in user_input1]

print(cc_num_usr)

#Slice off the last digit. That is the check digit.
cc_num_slc = cc_num_tst.pop(-1)
print(cc_num_slc)

# Reverse the digits.
cc_num_rev = cc_num_tst[::-1]
print(cc_num_rev)

#Double every other element in the reversed list.
cc_num_dbl = [num * 2 for num in cc_num_rev]

print(cc_num_dbl)

#Subtract nine from numbers over nine.
cc_num_nin = [num - 9 for num in cc_num_dbl if num > 9]

print(cc_num_nin)

#Sum all values.
#cc_num_sum = reduce(lambda x,y : x + y, cc_num_nin) ***import functools***
cc_num_sum = 0
for i in range(len(cc_num_nin)):
    cc_num_sum += cc_num_nin[i]

print(cc_num_sum)

# Convert sum to a list for check
sum_to_lst = list(str(cc_num_sum))
print(sum_to_lst)

# If that matches the check digit, the whole card number is valid.
if int(sum_to_lst[1]) == 9:
    print("valid")