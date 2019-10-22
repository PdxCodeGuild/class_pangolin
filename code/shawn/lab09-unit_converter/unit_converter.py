# Shawn Stolsig
# PDX Code Guild 
# Assignment: Lab 9 - Unit Converter
# Date: 10/22/2019

# conversion factors...multiply original units by this to convert to meters
feetToMeters = 0.3048
milesToMeters = 1609.34
kmToMeters = 1000

# get user distance input
userDistance = input("What is the distance? ")
userUnits = input("what are the units? ") 

# initialize output distance/units
outputDistance = -1
outputUnits = 'x'

# convert to meters
outputUnits = "m"

if userUnits == 'ft':
    outputDistance = float(userDistance) * feetToMeters
elif userUnits == 'mi':
    outputDistance = float(userDistance) * milesToMeters
elif userUnits == 'km':
    outputDistance = float(userDistance) * kmToMeters

print(f"{userDistance} {userUnits} is {outputDistance} {outputUnits}")