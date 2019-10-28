'''
Lab 9: Unit Converter - Version 4

Purpose/goal: - Ask the user for the distance - D 
              - the starting units - D
              - and the units to convert to - D

'''

# user greeting
print("\nGreetings!\nThis is a simple distance unit converter.")

# define input unit
in_un = input("What unit would you like to convert from (mi / ft / m / km)?: ").lower()

if in_un in ("mile", "miles", "mi"):
    i = "mi"
if in_un in ("feet", "foot", "ft"):
    i = "ft"
if in_un in ("meter", "meters", "m"):
    i = "m"
if in_un in ("kilometers", "kilometer", "km"):
    i = "km"
if in_un in ("yard", "yards", "yds"):
    i = "yds"
if in_un in ("inch", "inches", "in"):
    i = "in"


# define user distance
dis = float(input("How many?: "))

# define output unit
o_un = input("What unit would you like to convert to (mi / ft / m / km)?: ").lower()

if o_un in ("mile", "miles", "mi"):
    o = "mi"
if o_un in ("feet", "foot", "ft"):
    o = "ft"
if o_un in ("meter", "meters", "m"):
    o = "m"
if o_un in ("kilometers", "kilometer", "km"):
    o = "km"
if o_un in ("yard", "yards", "yds"):
    o = "yds"
if o_un in ("inch", "inches", "in"):
    o = "in"

# convert to meters
if i == 'mi':
    m = dis * 1609.34 
if i == 'ft':
    m = dis * 0.3048
if i == 'm':
    m = dis * 1
if i == 'km':
    m = dis * 1000
if i == 'yds':
    m = dis * 0.9144
if i == 'in':
    m = dis * 0.0254

# convert to output unit
if o == 'mi':
    c = m / 1609.34 
if o == 'ft':
    c = m / 0.3048
if o == 'm':
    c = m / 1
if o == 'km':
    c = m / 1000
if o == 'yds':
    c = m / 0.9144
if o == 'in':
    c = m / 0.0254

# return    
print(f"\nGreat!\n{dis} {i} is equal to {c} {o}.")

# end program
print("Thanks for using this simple distance unit converter!\nGoodbye.")