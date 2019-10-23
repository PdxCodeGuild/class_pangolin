# Conversions to meters formula
ft = .3048
mi = 1609.34
km = 1000
m = 1
yd = .9144
nchz = .0254 
# Greets the user
print("\nWelcome, this tool is a conversion calculator for (ft, mi, km, m, yd, nchz)\n")
# User input 
user_starting_unit = input("Enter a starting uint as (ft, mi, km, m, yd, nchz): > ")
user_number_input = int(input("Enter the length / distance: > "))
user_unit_conversion_input = input("Enter an ending unit as (ft, mi, km, m, yd, nchz): > ")
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