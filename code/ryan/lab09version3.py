unit = input("What unit of measurement would you like to convert to meters?  Feet, inches, miles, yards, or kilometers?:  ").lower()
num = int(input(f"How many {unit} would you like to convert?  Please give a whole number: "))

if unit == "feet":
    result = num * .3048
elif unit == "miles":
    result = num * 1609.34
elif unit == "inches":
    result = num * .0254
elif unit ==  "yards":
    result = num * .9144
else:
    result = num * 1000

print(f"You entered {num} {unit}.  This equals {result} meters.")
