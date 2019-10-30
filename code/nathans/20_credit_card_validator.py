# credit_card_validator.py
"""
Unfinished
"""


card_number = [4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 5]
check_digit = card_number.pop(15)
short_card = card_number[:15:]
# reverse_card = short_card[::-1]    

# reverse_card = list(reversed(short_card))

for count,num in enumerate(card_number):
    print(num)


# doubled_num = []
# for num in reverse_card[::2]:
#     doubled_num.append(num * 2)

# print(doubled_num)

    #for num in range(len(card_number)):
       # if num %2 == 0:
       #     print(num * 2)





print(f"The the check digit is: {check_digit} and the shortened card number is {short_card}" )









