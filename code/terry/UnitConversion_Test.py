# Unit conversion.  In version 1, we ask the user for the distance in feet and convert it to meters.
# Other versions of this program will expand off this one.
aFoot = 0.3048
aMile = 0.000621
aMeter = 1.0
aKilo = 0.001
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

userUnit = input("What is the unit input? ").lower()
userOutput = input("What is the unit output? ").lower()
userDistance = input("What is the distance to be converted? ")

if userUnit == userOutput:
    print("These units are the same.")
elif int(userDistance) <= 0:
    print("Enter a number above zero.")
else:
    # print("error")
    # print(userUnit)
    # print(userDistance)

    if userUnit == "mi":
        x = 1609.34
    elif userUnit == "ft":
        x = aFoot
    elif userUnit == "m":
        x = aMeter
    elif userUnit == "km":
        x = aKilo
    elif userUnit == "yd":
        x = aYard
    elif userUnit == "in":
        x = anInch

    # print(x)
    # print(userOutput)

    if userOutput == "mi":
        y = aMile
    elif userOutput == "ft":
        y = aFoot
    elif userOutput == "m":
        y = aMeter
    elif userOutput == "km":
        y = 1000
    elif userOutput == "yd":
        y = aYard
    elif userOutput == "in":
        y = anInch

    print(x)
    print(y)
    print(userDistance)
    # x = x * int(userDistance)
    # y = y * int(userDistance)
    # k = (x * y) * int(userDistance)
    # k = (x * y)
    # k = str(round(k, 8))
    # print(k)
