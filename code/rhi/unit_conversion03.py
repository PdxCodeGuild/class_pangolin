'''
unit conversion lab 04
written by Rhornberger
last updated oct 24 2019
'''
import math
# get the users input on the distance and units they want converted.
print('Welcome to your friendly neighborhood unit conversion bot!')
print()
distance = int(input('Please enter the distance you want converted: '))
print()
unit = input('Please enter the unit type you would like to use: ').lower()
m1 = []

# convert from original unit to km.
if unit in ('feet', 'ft', 'foot'):
    m1.append(distance * 0.3048)
elif unit in ('miles', 'mile', 'mi'):
    m1.append(distance * 1609.34)
elif unit in ('meters', 'meter', 'm'):
    m1.append(distance * 1)
elif unit in ('kilometers', 'kilometer', 'km'):
    m1.append(distance * 1000)
elif unit in ('yards', 'yard', 'yd'):
    m1.append(distance * 0.9144)
elif unit in ('inches', 'inch' 'in'):
    m1.append(distance * 0.0254)    

#convert from km to other unit.
new_unit = input('What unit would you like this converted to? ')
new_con1 = []
if new_unit in ('feet', 'ft', 'foot'):
    new_con1.append(m1[0] / 0.3048)
elif new_unit in ('miles', 'mile', 'mi'):
    new_con1.append(m1[0] / 1609.34)
elif new_unit in ('meters', 'meter', 'm'):
    new_con1.append(m1[0] / 1)
elif new_unit in ('kilometers', 'kilometer', 'km'):
    new_con1.append(m1[0] / 1000)
elif new_unit in ('yards', 'yard', 'yd'):
    new_con1.append(m1[0] / 0.9144)
elif new_unit in ('inches', 'inch' 'in'):
    new_con1.append(m1[0] / 0.0254)

new_con1 = round(new_con1[0], 2)

print(f'{new_con1} {new_unit} is the conversion.')
print('Thank you and I hope to see you again soon.')