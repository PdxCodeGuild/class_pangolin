user_unit = input('Enter the type of unit you want to convert? *feet, mile, km, yard, inch*: ').lower()
user_number = float(input('Enter the number you would like to convert? '))

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
    
user_unit2 = input('Enter the type of unit you would like to convert to? *feet, mile, km, yard, inch*: ').lower()
if user_unit2 == 'feet':
    value = value / 0.3048
elif user_unit2 == 'mile':
    value = value / 1609.34
elif user_unit2 == 'km':
    value = value / 1000
elif user_unit2 == 'yard':
    value = value / 0.9144
elif user_unit2 == 'inch':
    value = value / 0.0254
else:
    print('enter a valid number')

print (int(user_number), user_unit, 'is', int(value) , user_unit2)


#user_number = user_number * 0.3048


