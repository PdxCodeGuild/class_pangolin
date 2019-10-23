# Taylor Rebbe
# PDX Code Guild
# Lab 09 Complete

# Variables
ft = .3048
mi = 1609.34
km = 1000
m = 1
yd = .9144
nchz = .0254 

message1 = "Enter the length / distance as a number: > "
message2 = "Enter a starting uint as (ft, mi, km, m, yd, nchz): > "
message3 = "Enter a conversion uint as (ft, mi, km, m, yd, nchz): > "

# Numeric input validation function from 101computing.net 
def inputNumber(message):
     while True:
          try:
               user_number_input = int(input(message)) 
          except ValueError:
               print("\nPlease follow the instructions")
               continue
          else:
               return user_number_input
# Unit input validation function
def inputUnits(message):
     while True:
          user_unit = input(message)
          if user_unit.lower() not in ("ft", "mi", "km","m", "yd", "nchz"):
               print("\nPlease follow the instructions")
          else:
               return user_unit
                        
# Greets the user
print("\nWelcome, this tool is a conversion calculator for (ft, mi, km, m, yd, nchz)\n")

# Function call inputUnits
user_starting_unit = inputUnits(message2)

# Calls the input function for the numerical length / distance     
user_number_input = inputNumber(message1)

# Converts the starting unit to meters
if user_starting_unit == "ft":
     to_meters = ft * user_number_input
elif user_starting_unit == "mi":
     to_meters = mi * user_number_input
elif user_starting_unit == "km":
     to_meters = km * user_number_input
elif user_starting_unit == "yd":
     to_meters = yd * user_number_input
elif user_starting_unit == "nchz":
     to_meters = nchz * user_number_input
else:
     to_meters = m * user_number_input

# Function call inputUnits
user_unit_conversion_input =inputUnits(message3)

# Final conversion from meters to desired unit
if user_unit_conversion_input == "ft":
     print(to_meters / ft)
elif user_unit_conversion_input == "mi":
     print(to_meters / mi)
elif user_unit_conversion_input == "km":
     print(to_meters / km)
elif user_unit_conversion_input == "yd":
     print(to_meters / yd)
elif user_unit_conversion_input == "nchz":
     print(to_meters / nchz)
else:
     print(to_meters / m)