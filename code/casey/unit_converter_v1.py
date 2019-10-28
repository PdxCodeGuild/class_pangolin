'''
Lab 9: Unit Converter - Version 1

Purpose/goal: Write a program that allows the user to convert a number between units.

    - Ask the user for the number of feet. - D
    - Print out the equivalent distance in meters. - D 

'''

# user greeting
print("\nGreetings!\nThis is a simple distance unit converter.")

# define user input
x = float(input("Type a number of feet to receive the equivalent in meters: "))

# convert
y = x * 0.3048

# return user's conversion
print(f"\nGreat! {x} feet is {y} meters.")

# end program
print("Thanks for using this simple distance unit converter!\nGoodbye.")