# Shawn Stolsig
# PDX Code Guild 
# Assignment: Lab 15 - Number to Phrase
# Date: 10/25/2019

# use modulus or string operations to break things up to digits
# use the digit as an index for a list of strings or as a key for a dict of digit:phrase pairs
# ver 3 and 4 are optional
# make function to do this, then call the function

# declare dictionary for number/english equivalents 
num_translated = {
    '0': '',        # will hardcode input of zero, but the empty string is needed for multiples of 10
    '1': 'one',
    '2': 'two', 
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven', 
    '8': 'eight', 
    '9': 'nine',
    '10': 'ten', 
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen', 
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen',
    '20': 'twenty', 
    '30': 'thirty', 
    '40': 'fourty',
    '50': 'fifty', 
    '60': 'sixty',
    '70': 'seventy',
    '80': 'eighty',
    '90': 'ninty'
}

# declare dictionarey for number/roman numeral translation
num_roman = {
    '0': '',       # empty string for edge case
    '1': 'I',
    '2': 'II', 
    '3': 'III',
    '4': 'IV',
    '5': 'V',
    '6': 'VI',
    '7': 'VII', 
    '8': 'VIII', 
    '9': 'IX',
    '10': 'X', 
    '20': 'XX',
    '30': 'XXX',
    '40': 'XL',
    '50': 'L', 
    '60': 'LX',
    '70': 'LXX',
    '80': 'LXXX',
    '90': 'XC',
    '100': 'C', 
    '200': 'CC', 
    '300': 'CCC',
    '400': 'CD', 
    '500': 'D',
    '600': 'DC',
    '700': 'DCC',
    '800': 'DCCC',
    '900': 'CM'  
}

# function for returning ones place
def return_ones_digit(num):
    ''' takes in a int, returns string '''
    return str(num % 10)

# function for returning tens place
def return_tens_digit(num):
    ''' takes an int, returns a string representing how many times that number can be divided by 10 '''
    return str((num // 10) * 10)

# function for returning hundreds place
def return_hundreds_digit(num):
    ''' takes an int, returns a string representing how many times number can be divided by 100 '''
    return str(num // 100)

# function for get input
def get_number_input(mode = 'number'):
    ''' returns user number input as an int.  optional arugment will turn function into time input format instead of a single int'''
    
    # number input
    if mode == 'number':
        while True:
            input_number = int(input("Please input number from 0 to 1000: "))
            if input_number >= 0 and input_number < 1000:
                return input_number
            print("Please try different input")
    # time input
    else:
        while True:
            input_time = input("Please input time in following format HH:MM am/pm: ")

            # adjust input_hour/min depending if one digit hour
            if input_time[1] == ':':
                input_hour = int(input_time[:1:])                                    # slice off first number for single digit hour
                input_min = int(input_time[2:4:])                                    # slice off minutes digits
            # adjust input_hour/min depending if two digit hour
            elif input_time[2] == ':':
                input_hour = int(input_time[:2:])                                    # slice off first two numbers, for two digit hour              
                input_min = int(input_time[3:5:])                                    # slice off minutes digits
            input_ampm = input_time[len(input_time)-2:len(input_time):1].lower()     # slice off am or pm

            # validation to ensure hours/min/am/pm are entered correctly
            if input_hour > 12 or input_hour < 1:
                print("Please input hour between 1 and 12")
            elif input_min > 59 or input_min < 0:
                print("Please input min between 0 and 59")
            elif input_ampm not in ['am', 'pm']:
                print("Please make sure last two digits are either 'am' or 'pm'")
            else:
                # return tuple (hour, min, am/pm)
                return input_hour, input_min, input_ampm

# function for printing english version of number
def print_english_num():
    ''' this function takes no arguments, but will print english version of a number entered by user '''

    # get input 
    num = get_number_input()

    # use if statements to figure out which functions to call based on size of num
    if num == 0:
        print('\n***** Your number is: zero *****\n')  # edge case based on how dictionary is set up
    elif num < 20:
        print(f'\n***** Your number is {num_translated[str(num)]} *****\n')
    elif num >=20 and num <= 99:
        print(f'\n***** Your number is {num_translated[return_tens_digit(num)]} {num_translated[return_ones_digit(num)]} *****\n')
    elif num >=100 and num <= 999:
        print(f'\n***** Your number is {num_translated[return_hundreds_digit(num)]} hundred {num_translated[return_tens_digit(num % 100)]} {num_translated[return_ones_digit(num)]} *****\n')

# function for printing roman numeral version of number
def print_roman_num():
    ''' this function takes no arguments, but will print roman numeral version of a number entered by user '''

    # get input 
    num = get_number_input()

    # use if statements to figure out which functions to call based on size of num
    if num == 0:
        print('\n***** There is no roman numeral for zero *****\n')  # edge case based on how dictionary is set up
    elif num < 10:
        print(f'\n***** Your number is {num_roman[str(num)]} *****\n')
    elif num >=10 and num <= 99:
        print(f'\n***** Your number is {num_roman[return_tens_digit(num)]}{num_roman[return_ones_digit(num)]} *****\n')
    elif num >=100 and num <= 999:
        hundred_string = return_hundreds_digit(num) + '00'  # have to add 0's to make this compatable with funtions used for regular numbers
        print(f'\n***** Your number is {num_roman[hundred_string]}{num_roman[return_tens_digit(num % 100)]}{num_roman[return_ones_digit(num)]} *****\n')

# function for printing english version of time
def print_time():
    ''' this function takes no arguments, but will print roman numeral version of a number entered by user '''

    # get input 
    hours, minutes, ampm = get_number_input('time')   # pass optional parameter to trigger for time input
    # print(get_number_input('time') )
    # print time in english
    print(f'\n******* Your time is {num_translated[str(hours)]} {num_translated[return_tens_digit(minutes)]} {num_translated[return_ones_digit(minutes)]} {ampm} *******\n')

# main loop
while True:

    # select different mode for program 
    prompt = 'Please type number for mode: \n (1) Number to English conversion \n (2) Number to Roman numeral conversion \n (3) Time to English \n (4) Exit \n Input: '
    mode_select = input(prompt)
    if mode_select not in ['1','2','3','4']:
        print('Invalid command, try again')
    elif mode_select == '1':        # time mode
        print_english_num()
    elif mode_select == '2':        # roman numeral mode
        print_roman_num()
    elif mode_select == '3':        # time mode
        print_time()
    elif mode_select == '4':        # quit
        break

print("Program Exiting")

