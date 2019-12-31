'''
Lab 20: Credit Card Validation

Purpose/goal: Write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:

    - Convert the input string into a list of ints - D

    - Slice off the last digit. That is the check digit. - D

    - Reverse the digits. - D

    - Double every other element in the reversed list. - D

    - Subtract nine from numbers over nine. - D

    - Sum all values. - D

    - Take the second digit of that sum. - D

'''

# request cc number
dig = input("\nPlease enter a valid credit card number: ")

# convert the input string into a list of ints
dig_list = list(dig)
# print(dig_list)

int_list = [int(i) for i in dig_list]
# print(int_list)

# slice off the last digit *this is the check digit*
check = int_list.pop()

# str check for later comparison 
check = str(check)
# print(int_list)

# reverse the digits
int_list.reverse()
# print(int_list)

# double every other element in the reversed list
# if int_list[i] % 2 == 0:
#     int_list[i] * 2 
def every_other_double():
    for i in range(0, len(int_list), 2):
        int_list[i] *= 2
    return int_list
every_other_double()
# print(int_list)

# subtract nine from numbers over nine
int_list = [num - 9 if num > 9 else num for num in int_list]
# print(int_list)

# sum values & str
list_sum = sum(int_list)
# print(list_sum)

list_sum = str(list_sum)
# print(list_sum)

# take second digit of total sum
check2 = list_sum[1]

# print(check2)

# print(check)

# validate with check digit
if check == check2:
    print("Your card has been validated!\n")   
else:
    print("I'm sorry. This is not a valid card number.\n")  
