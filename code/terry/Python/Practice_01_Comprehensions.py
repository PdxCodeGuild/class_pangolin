# Write a comprehension to generate the first 10 powers of two.

def powersOfTen():
    powerList = [2**y for y in range(10)]
    return powerList

print(f"{powersOfTen()}")