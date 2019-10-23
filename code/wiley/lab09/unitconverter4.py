#bloated but working
var1 =float(input("What is the distance? "))
var2 =input("What is the unit?")
if var2.lower() == "ft" or var2.lower() == "feet":
    var1 *= .3048
    print(str(var1) + " meters.")    
elif var2.lower() == "mi" or var2.lower() == "miles":
    var1 *= 1609.344
    print(str(var1) + " meters.")
    
elif var2.lower() == "m" or var2.lower() == "meters" or var2.lower() == "meter":
    print(str(var1) + " Meters... DUH!")
    
elif var2.lower() == "km" or var2.lower() == "kilometers" or var2.lower() == "kilometer":
    var1 *= 1000
    print(str(var1) + " meters")
    
elif var2.lower() == "y" or var2.lower() == "yard" or var2.lower() == "yards":
    var1 *= .9144
    print(str(var1)+ " meters")
    
elif var2.lower() == "in" or var2.lower() == "inch" or var2.lower() == "inches":
    var1 *= .0254
    print(str(var1) + " meters.")
else:
    print("Not a valid unit in this version, sorry. ")

var3 = input("what is the desired unit?  ")
if var3.lower() == "ft" or var3.lower() == "feet":
    var1 *= 3.28084
    print(str(var1) + " feet")
elif var3.lower() == "mi" or var3.lower() == "miles":
    var1 *= 0.000621371
    print(str(var1) + " miles")
elif var3.lower() == "km" or var3.lower() == "kilometers":
    var1 *= 1000
    print(str(var1) + " kilometers")
elif var3.lower() == "y" or var3.lower() == "yards":
    var1 *= 1.09361
    print(str(var1) +" yards")
elif var3.lower() == "in" or var3.lower() == "inches":
    var1 *= 39.3701
    print(str(var1) + " inches")
else:
    print("Not a compatible unit, sorry. ")