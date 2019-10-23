# Unit conversion.  In version 1, we ask the user for the distance in feet and convert it to meters.
# Other versions of this program will expand off this one.
aFoot = 0.3048
aMile = 1609.34
aMeter = 1.0
aKilo = 1000.0
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
userOutput = ""
userDistance = 0

userUnit = input("What is the unit input? From: ").lower()
userOutput = input("What is the unit output? To: ").lower()
userDistance = input("What is the distance to be converted? ")

if userUnit == userOutput:
    print("These units are the same.")
elif int(userDistance) <= 0:
    print("Enter a number above zero.")
else:
    # Start of the Input.
    if userUnit == "mi":
        x = 1609.34 * float(userDistance)
    elif userUnit == "ft":
        x = 0.3048 * float(userDistance)
    elif userUnit == "m":
        x = float(userDistance)
    elif userUnit == "km":
        x = 1000 * float(userDistance)
    elif userUnit == "yd":
        x = 0.9144 * float(userDistance)
    elif userUnit == "in":
        x = 0.0254 * float(userDistance)

    # Start of the Output
    if userOutput == "mi":
        y = 0.000621
    elif userOutput == "ft":
        y = 3.281
    elif userOutput == "m":
        y = 1
    elif userOutput == "km":
        y = 0.001
    elif userOutput == "yd":
        y = 1.094
    elif userOutput == "in":
        y = 39.370

    k = x * y
    print(f"{userDistance} {userUnit} to {userOutput} is approx: {k}")
