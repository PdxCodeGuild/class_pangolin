unit = input("What unit of measurement would you like to convert to meters?  Feet, miles, or kilometers?:  ").lower()
num = int(input(f"How many {unit} would you like to convert?  Please give a whole number: "))

if unit == "feet":
    result = num * .3048
elif unit == "miles":
    result = num * 1609.34
else:
    result = num * 1000

print(f"You entered {num} {unit}.  This equals {result} meters.")
