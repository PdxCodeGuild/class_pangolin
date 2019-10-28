'''
Lab 9: Unit Converter - Version 3

    - Add support for yards, and inches. - D

'''

# user greeting
print("\nGreetings!\nThis is a simple distance unit converter.\nThis tool will convert your distance into meters.")

# define unit
unit = input("What would you like to convert from (mi / ft / m / km / yds / in)?: ").lower()

if unit in ("mile", "miles", "mi"):
    u = "mi"
if unit in ("feet", "foot", "ft"):
    u = "ft"
if unit in ("meter", "meters", "m"):
    u = "m"
if unit in ("kilometers", "kilometer", "km"):
    u = "km"
if unit in ("yard", "yards", "yds"):
    u = "yds"
if unit in ("inch", "inches", "in"):
    u = "in"


# define user distance
dis = float(input("How many?: "))


# convert
if u == 'mi':
    c = dis * 1609.34 
if u == 'ft':
    c = dis * 0.3048
if u == 'm':
    c = dis * 1
if u == 'km':
    c = dis * 1000
if u == 'yds':
    c = dis * 0.9144
if u == 'in':
    c = dis * 0.0254

# return
print(f"\nGreat! {dis} {u} is equal to {c} meter(s).")

# end program
print("Thanks for using this simple distance unit converter!\nGoodbye.")