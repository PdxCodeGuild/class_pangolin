# Shawn Stolsig
# PDX Code Guild 
# Assignment: Lab 9 - Unit Converter
# Date: 10/22/2019

# conversion factors...multiply original units by this to convert to meters
feetToMeters = 0.3048
milesToMeters = 1609.34
kmToMeters = 1000

# declare function for handling user input
def cleanUnits(input):
    # convert to lowercase
    input = input.lower()

    # use if statements to check for different ways of spelling/abbreviating units
    if input == 'feet' or input == 'ft':
        return 'ft'
    elif input == 'kilometer' or input == 'km' or input == 'kilometers':
        return 'km'
    elif input == 'meters' or input == 'meter' or input == 'm':
        return 'm'
    elif input == 'mi' or input == 'miles' or input == 'mile':
        return 'mi'
    else:
        print("You've broken me...I don't understand your input, please try again!")

# get and clean user distance input
userDistance = input("What is the distance? ")
inputUnits = input("what are the starting units? ") 
inputUnits = cleanUnits(inputUnits)
outputUnits = input("What are the desired output units? ")
outputUnits = cleanUnits(outputUnits)

# initialize output distance/units (using negative number to help with debug)
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