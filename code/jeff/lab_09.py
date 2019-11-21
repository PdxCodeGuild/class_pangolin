# lab_09.py
# # Jeff Smith
# 10.22.19

import math

orig = int(input('Welcome. Please tell me the distance you would like to convert: '))

measure = input('What are the units? (ft, mi, km): ').lower


unit = [ft == 0.3048, mi == 1609.34, m == 1, km == 1000]

if measure == ft:
    print(orig * ft)