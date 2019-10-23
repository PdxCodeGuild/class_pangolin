'''
lab 09 unit conversion
written by Rhrnberger
last updated oct 22 2019
'''
#import ascii
print('Welcome to your friendly neighborhood unit conversion bot!')
print()
distance = int(input('please enter the distance you want converted into meters: '))
print()
unit = input('please enter the units you would like to use either feet, miles, meters, or kilometers: ').lower()
print()
if unit == 'feet':
    print(f'{distance} {unit} is equal to {distance * 0.3048} meters.')
elif unit == 'miles':
    print(f'{distance} {unit} is equal to {distance * 1609.34} meters')
elif unit == 'meters':
    print(f'{distance} {unit} is equal to {distance * 1} meters')
elif unit == 'kilometers':
    print(f'{distance} {unit} is equal to {distance * 1000} meters')
print()
print('Thank you and I hope to see you again soon.')
