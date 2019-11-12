
import re

# regex for x,y input
regex = r"[0-2]{1},[0-2]{1}"

# get user validated user input
while True:
    user_input = input("Please input x,y coordinates: ")

    if re.match(regex, user_input):
        print("good input")
    else:
        print("bad input")

