# Unit conversion.  In version 1, we ask the user for the distance in feet and convert it to meters.
# Other versions of this program will expand off this one.
aMeter = 0.3048

numOfFeet = input("What is the distance in feet? ")
if numOfFeet:
    numOfFeet = int(numOfFeet)
    x = numOfFeet * aMeter
    x = str(round(x, 3))
    print(f"{numOfFeet}ft is {x}m")
else:
    print("You did not enter a value.")
