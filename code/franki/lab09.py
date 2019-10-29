#filename unit_converter

num1 = int(input("What is the distance? "))
input1 = (input("Is your measurement in inches, feet, yards, miles, meters, or kilometers? ").lower())
input2 = (input("Would you like to convert to inches, feet, yards, miles, meters, or kilometers? "))

if input1 in ['inches', 'in', 'inch']:
    unit1 = "inches"
elif input1 in ['feet', 'ft', 'foot']:
    unit1 = "feet"
elif input1 in ['meters', 'meter', 'm']:
    unit1 = "meters"
elif input1 in ['yards', 'yard', 'yd']:
    unit1 = "yards"
elif input1 in ['miles', 'mile', 'mi']:
    unit1 = "miles"
elif input1 in ['kilometers', 'kilometer', 'km']:
    unit1 = "kilometers"
else:
    print("Sorry, that's not a valid unit.")

if input2 in ['inches', 'in', 'inch']:
    unit2 = "inches"
elif input2 in ['feet', 'ft', 'foot']:
    unit2 = "feet"
elif input2 in ['meters', 'meter', 'm']:
    unit2 = "meters"
elif input2 in ['yards', 'yard', 'yd']:
    unit2 = "yards"
elif input2 in ['miles', 'mile', 'mi']:
    unit2 = "miles"
elif input2 in ['kilometers', 'kilometer', 'km']:
    unit2 = "kilometers"
else:
    print("Sorry, that's not a valid unit.")

if unit1 == "feet":
        num2 = num1 * 0.3048
elif unit1 == "miles":
        num2 = num1 * 1609.34
elif unit1 == "meters":
        num2 = num1
elif unit1 == "kilometers":
        num2 = num1 * 1000
elif unit1 == "inches":
        num2 = num1 * 0.0254
elif unit1 == "yards":
        num2 = num1 * 0.9144
else:
    print("Sorry, that is not a valid unit.")
if unit2 == "inches":
    output = num2 * 39.3701
elif unit2 == "feet":
    output = num2 * 3.2808
elif unit2 == "yards":
    output = num2 * 1.09361
elif unit2 == "miles":
    output = num2 * 0.000621371
elif unit2 == "meters":
    output = num2
elif unit2 == "kilometers":
    output = num2 * 0.001
else:
    print("Sorry, I don't understand.")



print(f"{num1} {unit1} is {output} {unit2}.")
