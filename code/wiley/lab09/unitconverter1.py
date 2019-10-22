#this lab will involve writing a program that allows the user to convert a number between units. 
#1 ft = .3048 meters We can get the output of feet in meters by multiplying the input distance by 0.3048
while True: 
    try:
        var1 = float(input("What is the distance in feet?  "))
        response = var1 * .3048
        print(f"{var1} feet is equal to {response} meters.\n ")
        print("Thanks for converting!")
        break
    except ValueError:
        print("You must give a number, without any thing else.")