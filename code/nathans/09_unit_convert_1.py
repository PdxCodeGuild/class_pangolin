# unit_convert.py

import math
import string


user_input = float(input("What is the distance in feet? "))
user_input_meters =float(user_input *0.3048)

print(f"{user_input} feet is equal to {user_input_meters} meters.")