#Lab9 Unit Converter 
'''
Version 4
Now we'll ask the user for the distance,
the starting units, and the units to convert to.

1 ft is 0.3048 m
1 mi is 1609.34 m
1 m is 1 m
1 km is 1000 m
1 yard is 0.9144 m
1 inch is 0.0254 m
'''
unit_list =     ["km", "kilo", "kilometer", "kilometers",
                 "mile", "miles", "mi", "feet", "ft", "m", "meter", 
                 "meters", "in", "inch", "inches", "yd", "yard", "yards"]


print("Hello! We're converting distances today!")
units_from = input("From what kind of distance are we converting?\n>")
units_from = units_from.lower()
units_to = input("To what kind of distance are we converting?\n>")
units_to = units_to.lower()
distance = input(f"How many {units_from} are we converting today?\n>")
distance = int(distance)
meter = 0

if units_to and units_from not in unit_list:
    print("Just basic distances today please.")

else:
    if units_from in ["km", "kilo", "kilometer", "kilometers"]:
        meter = distance * 1000

    elif units_from in ["mile", "miles", "mi"]:
        meter = distance * 1609.34

    elif units_from in ["feet", "ft"]: 
        meter = distance * 0.3048

    elif units_from in ["m", "meter", "meters"]:
        meter = distance

    elif units_from in ["in", "inch", "inches"]:
        meter = distance * 0.0254

    elif units_from in ["yd", "yard", "yards"]:
        meter = distance * 0.9144

    else:
        print("Hey! That's not a number!")
        

    print(f"Fab! Your distance is {meter} meters! Let's convert that to {units_to}")
    if units_to in ["km", "kilo", "kilometer", "kilometers"]:
        meter = distance * 1000

    elif units_to in ["mile", "miles", "mi"]:
        meter = distance * 0.000621371

    elif units_to in ["feet", "ft"]: 
        meter = distance * 3.28084

    elif units_to in ["m", "meter", "meters"]:
        meter = distance

    elif units_to in ["in", "inch", "inches"]:
        meter = distance * 39.3701

    elif units_to in ["yd", "yard", "yards"]:
        meter = distance * 1.09361

    print(f"Your converted distance is {meter} {units_to}!")