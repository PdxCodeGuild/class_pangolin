'''Allow the user to also enter the units. Then depending on the units, convert the distance into meters. The units we'll allow are feet, miles, meters, and kilometers.

1 ft is 0.3048 m
1 mi is 1609.34 m
1 m is 1 m
1 km is 1000 m
'''

user_input = int(input('What is the number of feet you would like to convert? '))
user_input = user_input * 0.3048

print(user_input)