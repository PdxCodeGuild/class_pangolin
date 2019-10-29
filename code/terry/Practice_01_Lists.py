# Write a function using random.randint to generate an index, use that index to pick a random element of a list and return it.

import random


def random_element():
    num = random.randint(1, 200)
    listNum.append(num)
    numChoice = random.choice(listNum)
    return numChoice


listNum = []
for x in range(10):
    random_element()

print(f"{random_element()}")
