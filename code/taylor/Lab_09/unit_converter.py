# Conversions to meters
ft = .3048
mi = 1609.34
km = 1000
m = 1
yd = .9144
nchz = .0254 
# Greets the user
print("Welcome, this tool calculates your input to meters")
# User input 
user_number_input = int(input("Enter the length / distance: > "))
user_unit_input = input("Enter a unit as (ft, mi, km, m, yd, nchz): > ")
# Converts user defined unit to meters
if user_unit_input == "ft":
     print(f"{user_number_input * ft} meters")
elif user_unit_input == "mi":
     print(f"{user_number_input * mi} meters")
elif user_unit_input == "km":
     print(f"{user_number_input * km} meters") 
elif user_unit_input == "yd":
     print(f"{user_number_input * yd} meters")
elif user_unit_input == "nchz":
     print(f"{user_number_input * nchz} meters")  
else:
 print(f"{user_number_input} meters")


