unit = input("What unit of measurement would you like to convert?  Feet, inches, miles, meters, yards, or kilometers?:  ").lower()
num = int(input(f"How many {unit} would you like to convert?  Please give a whole number: "))
convert = input("What unit would you like to convert to?  Feet, inches, miles, meters, yards, or kilometers?:  ").lower()

if unit == "feet":
    meters = num * .3048
elif unit == "miles":
    meters = num * 1609.34
elif unit == "inches":
    meters = num * .0254
elif unit ==  "yards":
    meters = num * .9144
elif unit == "meters":
    meters = num *1
else:
    meters = num * 1000

if convert == "feet":
    result = meters / .3048
elif convert == "miles":
    result = meters / 1609.34
elif convert == "inches":
    result = meters / .0254
elif convert ==  "yards":
    result = meters / .9144
elif convert == "meters":
    result =  meters / 1
else:
    result = meters / 1000

print(f"You entered {num} {unit}.  This equals {result} {convert}.")
