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
inputUnits = input("what are the starting units? ") 
outputUnits = input("What are the desired output units? ")

# initialize output distance/units
outputDistance = -1
inputInMeters = -1

# convert input to meters
if inputUnits == 'ft':
    inputInMeters = float(userDistance) * feetToMeters
elif inputUnits == 'mi':
    inputInMeters = float(userDistance) * milesToMeters
elif inputUnits == 'km':
    inputInMeters = float(userDistance) * kmToMeters
elif inputUnits == 'm':
    # do nothing, meters were input
    inputInMeters = userDistance
else:
    print("input unit not recognized, ending")

# for debugging, checking intermediate step
# print(f"inputInMeters is {inputInMeters}")

# convert meters to desired output
if outputUnits == 'ft':
    outputDistance = float(inputInMeters) / feetToMeters
elif outputUnits == 'mi':
    outputDistance = float(inputInMeters) / milesToMeters
elif outputUnits == 'km':
    outputDistance = float(inputInMeters) / kmToMeters
elif outputUnits == 'm':
    #do nothing, meters were requested
    outputDistance = float(inputInMeters)
else:
    print("output unit not recognized, ending")

print(f"{userDistance} {inputUnits} is {outputDistance} {outputUnits}")