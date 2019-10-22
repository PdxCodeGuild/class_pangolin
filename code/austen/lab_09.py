
user_unit = input('Enter the type of unit you want to convert?feet, mile, km, yard, inch: ').lower()
user_number = int(input('Enter the number you would like to convert? '))
'''
feet =  user_number *0.3048
mile = user_number *1609.34
km = user_number * 1000
'''
if user_unit == 'feet':
    value = user_number * 0.3048
elif user_unit == 'mile':
    value = user_number * 1609.34
elif user_unit == 'km':
    value = user_number * 1000
elif user_unit == 'yard':
    value = user_number * 0.9144
elif user_unit == 'inch':
    value = user_number * 0.0254
else:
    print('enter a valid number')

print (user_number, user_unit, 'is', value , 'meters')


#user_number = user_number * 0.3048


