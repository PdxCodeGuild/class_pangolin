# Unit conversion.  In version 1, we ask the user for the distance in feet and convert it to meters.
# Other versions of this program will expand off this one.
aFoot = 0.3048
aMile = 1609.34
aMeter = 1
aKilo = aMeter * 1000
aYard = 0.9144
anInch = 0.0254

# Feet
# numOfFeet = input("What is the distance in feet? ")
# if numOfFeet:
#     numOfFeet = int(numOfFeet)
#     x = numOfFeet * aFoot
#     x = str(round(x, 3))
#     print(f"{numOfFeet}ft is {x}m")
# else:
#     print("You did not enter a value.")

userUnit = ""
userDistance = 0

userUnit = input("What is the unit you would like to have converted to meters? ").lower()
userDistance = input("What is the distance to be converted? ")
# print(userUnit)
# print(userDistance)
if userUnit == "mi":
    x = aMile * float(userDistance)
elif userUnit == "ft":
    x = aFoot * float(userDistance)
elif userUnit == "m":
    x = float(userDistance)
elif userUnit == "km":
    x = 1000 * float(userDistance)
elif userUnit == "yd":
    x = aYard * float(userDistance)
elif userUnit == "in":
    x = anInch * float(userDistance)
print(x)
