# Taylor Rebbe
# PDX Coed Guild
# Lab_10v2

# Module
import os

# Message variables
message1 = "\nEnter a number, or 'done': > "

# List variables
num_list_user = []

# Functions
def findListAverage(num_list):
    sums = 0
    for i in range(len(num_list)):
        sums += num_list[i]
    average = sums / len(num_list)
    return average
        
def genUserDefinedList(user_num):
    num_list_user.append(user_num)
    return num_list_user

# Fresh console
os.system('cls' if os.name == 'nt' else 'clear')

# Main program loop
while True:
    
    user_input = input(message1)
    if user_input != 'done':
        genUserDefinedList(int(user_input))
        average = round(findListAverage(num_list_user))
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\nNumber List: > {num_list_user}\nAverage: > {average}")

    else:
        print("\nBye bye")
        break

    
  
    