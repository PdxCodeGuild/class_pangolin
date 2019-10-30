# Taylor Rebbe
# PDX Code Guild
# Lab_17v2
# 10/28/2019

# Anagram checker
# Variables receive user input string
user_input_1 = sorted(input("Enter the first word  > ").lower().replace(' ', '')) # Converts input to a list and orders 
user_input_2 = sorted(input("Enter the second word  > ").lower().replace(' ', ''))# Converts input to a list and orders 

print(user_input_1)
if user_input_1 == user_input_2: # After being ordered and converted to a list the inputs are compared for equality
    print("Anagram!")

# Palindrome checker
# Variables receive user input string
user_input_3 = input("Enter the first word  > ").lower().replace(' ', '')
user_input_4 = list(input("Enter the second word  > ").lower().replace(' ', ''))

# Function to reverse teh order of a given string, receives a list and returns a list
def reverse_string(uip1):
    i = len(uip1)
    rev_str = []
    while i > 0:
        rev_str += uip1[i - 1]
        i = i - 1
    return rev_str

# Compares the reveresd string to the second string, if a match it is a palindrome
if reverse_string(user_input_3) == user_input_4:
    print("Palindrome!")