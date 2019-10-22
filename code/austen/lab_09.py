
user_unit = input('Enter the type of unit you want to convert?feet, mile, km: ').lower()
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
else:
    print('enter a valid number')

print(value)


#user_number = user_number * 0.3048


