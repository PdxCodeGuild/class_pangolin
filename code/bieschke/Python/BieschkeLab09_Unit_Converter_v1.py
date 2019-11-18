#Lab9 Unit Converter 
'''
Version 1
Ask the user for the number of feet, and print out the equivalent distance
in meters. 

Hint: 1 ft is 0.3048 m. So we can get the output in meters by multiplying 
the input distance by 0.3048.
'''

feet = input("Hello! How many feet are we converting today?\n>")
feet = int(feet)
meter = feet * 0.3048
print(f"Fab! Your distance is {meter}!") 