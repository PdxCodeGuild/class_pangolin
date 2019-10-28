'''
Convert numbers to their written form
written by Rhornberger
last updated oct 28 2019
'''
# build the dictionaries
ones_dict = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
ten_dict = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
tens_dict = {0: '', 1: '', 2: 'twenty', 3: 'thirty', 4: 'fourty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}
hundreds_dict = {0: '', 1: 'one hundred', 2: 'two hundred', 3: 'three hundred', 4: 'four hundred', 5: 'five hundred', 6: 'six hundred', 7: 'seven hundred', 8: 'eight hundred', 9: 'nine hundred'}
# build the function
def num(user_input):
    if user_input[0] == '0' :
        return 'zero'    
    elif len(user_input) == 1 :
        ones = int(user_input)
        return ones_dict[ones]
    elif user_input[0] == '1' and len(user_input) == 1:
        ten = int(user_input)
        return ten_dict[ten]
    elif len(user_input) == 2:      
        tens_digit = int(user_input) // 10
        ones_digit = int(user_input) % 10
        res = tens_dict[tens_digit] + '-' + ones_dict[ones_digit]
        return res
    elif len(user_input) == 3:
        hun_digit = int(user_input) // 100
        tens_digit = int(user_input[1]) 
        ones_digit = int(user_input) % 10
        if tens_digit == 0 and ones_digit == 0:
            return hundreds_dict[hun_digit]
        elif tens_digit == 0:
            return hundreds_dict[hun_digit] + ' ' + 'and' + '' + tens_dict[tens_digit] + ' ' + ones_dict[ones_digit]
        elif ones_digit == 0:
            return hundreds_dict[hun_digit] + ' ' + 'and' + ' ' + tens_dict[tens_digit]
        elif ones_digit != 0:
            res = hundreds_dict[hun_digit] + ' ' + 'and' + ' ' + tens_dict[tens_digit] + '-' + ones_dict[ones_digit]
            return res
    return 'This number is outside of the parameters of my code!'

      
# ask for the user input and return the result 
user_num = input('What number would you like converted?: ')
print(num(user_num))