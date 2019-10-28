'''
Convert numbers to their written form
written by Rhornberger
started oct 25 2019
last updated oct 28 2019
'''
# build the dictionaries
ones_dict = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
ten_dict = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
tens_dict = {0: '', 1: '', 2: 'twenty', 3: 'thirty', 4: 'fourty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}
# build the function
def num(user_input):
    if user_num[0] == '0':
        return 'zero'
    elif len(user_num) == 1:
        ones = int(user_num)
        return ones_dict[ones]
    elif user_num[0] == '1':
        ten = int(user_num)
        return ten_dict[ten]
    elif len(user_num) == 2:      
        tens_digit = int(user_num) // 10
        ones_digit = int(user_num) % 10
        res = tens_dict[tens_digit] + '-' + ones_dict[ones_digit]
        return res
      
# ask for the user input and return the result 
user_num = input('What number would you like converted?: ')
print(num(user_num))