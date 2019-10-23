'''
unit conversion lab 03
written by Rhornberger
last updated oct 23 2019
'''
print('Welcome to your friendly neighborhood unit conversion bot!')
print()
distance = int(input('please enter the distance you want converted into meters: '))
print()
unit = input('please enter the units you would like to use either feet, ft, miles, mi, meters, m, kilometers, km, yards, yd, or inches, in: ').lower()

print()
if unit == 'feet' or 'ft':
    print(f'{distance} {unit} is equal to {distance * 0.3048} meters.')
elif unit == 'miles' or 'mi':
    print(f'{distance} {unit} is equal to {distance * 1609.34} meters.')
elif unit == 'meters' or 'm':
    print(f'{distance} {unit} is equal to {distance * 1} meters.')
elif unit == 'kilometers' or 'km':
    print(f'{distance} {unit} is equal to {distance * 1000} meters.')
elif unit == 'yards' or 'yd':
    print(f'{distance} {unit} is equal to {distance * 0.9144} meters.')
elif unit == 'inches'or 'in':
    print(f'{distance} {unit} is equal to {distance * 0.0254} meters.')
print()
print('Thank you and I hope to see you again soon.')