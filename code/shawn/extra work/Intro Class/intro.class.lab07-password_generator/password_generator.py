# Shawn Stolsig
# PDX Code Guild 
# Assignment: Intro Class Lab 7 - Password Generator
# Date: 10/24/2019

import random

# create lists of available characters
avail_special = list('~!@#$%^&*()_+[]\':",./<>?"')
avail_letters = list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
avail_numbers = list('1234567890')

# shuffle each list
random.shuffle(avail_special)
random.shuffle(avail_letters)
random.shuffle(avail_numbers)

# get input from user regarding how long a password they want
length_letters = int(input("how many letters? "))
length_numbers = int(input("how many numbers? "))
length_special = int(input("how many special characters? "))

# create unshuffled password to push characters on to
passwordList = []

# loop through each character type and append random character to password
for x in range(length_letters):
    passwordList.append(random.choice(avail_letters))
for x in range(length_numbers):
    passwordList.append(random.choice(avail_numbers))
for x in range(length_special):
    passwordList.append(random.choice(avail_special))

# shuffle and join choices
random.shuffle(passwordList)
passwordStr = ''.join(passwordList)

# print choices
print(f"Your password is {passwordStr}")