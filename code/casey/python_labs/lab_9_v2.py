'''
Lab 9: Unit Converter - Version 2

Purpose/goal: Allow the user to also enter the units. 

    - Depending on the units, convert the distance into meters. The units we'll allow are feet, miles, meters, and kilometers. - D

'''

# user greeting
print("\nGreetings!\nThis is a simple distance unit converter.\nThis tool will convert your distance into meters.")

# define unit
unit = input("What would you like to convert from (mi / ft / m / km)?: ").lower()

if unit in ("mile", "miles", "mi"):
    u = "mi"
if unit in ("feet", "foot", "ft"):
    u = "ft"
if unit in ("meter", "meters", "m"):
    u = "m"
if unit in ("kilometers", "kilometer", "km"):
    u = "km"


# define user distance
dis = float(input("How many?: "))


# convert & return
if u == 'mi':
    c = dis * 1609.34 
    print(f"\nGreat! {dis} {u} is equal to {c} meter(s).")
if u == 'ft':
    c = dis * 0.3048
    print(f"\nGreat! {dis} {u} is equal to {c} meter(s).")
if u == 'm':
    c = dis * 1
    print(f"\nGreat! {dis} {u} is equal to {c} meter(s).")
if u == 'km':
    c = dis * 1000
    print(f"\nGreat! {dis} {u} is equal to {c} meter(s).")

# end program
print("Thanks for using this simple distance unit converter!\nGoodbye.")