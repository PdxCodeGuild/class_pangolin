# Unit conversion.  In version 1, we ask the user for the distance in feet and convert it to meters.
# Other versions of this program will expand off this one.
aFoot = 0.3048
aMile = 1609.34
aMeter = 1
aKilo = aFoot * 1000

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
    x = aKilo / float(userDistance)
print(x)
