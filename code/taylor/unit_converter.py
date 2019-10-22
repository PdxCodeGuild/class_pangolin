# Conversions to meters
ft = 3.6576
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
     print(f"{ft * user_number_input} meters")
elif user_unit_input == "mi":
     print(f"{mi * user_number_input} meters")
elif user_unit_input == "km":
     print(f"{km * user_number_input} meters") 
elif user_unit_input == "yd":
     print(f"{yd * user_number_input} meters")
elif user_unit_input == "nchz":
     print(f"{nchz * user_number_input} meters")  
else:
 print(f"{user_number_input} meters")


