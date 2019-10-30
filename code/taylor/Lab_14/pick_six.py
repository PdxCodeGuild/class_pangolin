# Taylor Rebbe
# PDX Code Guild
# Lab_14 
# 10/30/2019

# Import random module
import random

# Variables
a, b, c, d, e, f = 0, 0, 0, 0, 0, 0

# Tallies ammount spent on tickets @ 2$ each
expenses = 0

# Function to calculate the winnings
def calc_winnings(a, b, c, d, e, f):
    total = sum([a * 2, b * 4, c * 10, d * 500, e * 1000000, f * 25000000])
    return total

# Function to generate a random list of 6 integers between 1 & 99 inclusive
def get_six():
    six_lst = []
    for n in range(1, 7):
        six_lst.append(random.randint(1, 99))
    return six_lst

# Main program loop
i = 0
while i < 100000:
    expenses += 2
    mtchs = len(set(get_six()) & set(get_six()))# set() & - intersection is used to determin matches in the set

    if mtchs == 1:
        a += 1
    elif mtchs == 2:
        b += 1  
    elif mtchs == 3:
        c += 1
    elif mtchs == 4:
        d += 1
    elif mtchs == 5:
        e += 1
    elif mtchs == 6:
        f += 1
    i += 1

# User output
totals = round(((calc_winnings(a, b, c, d, e, f) - expenses) / expenses) * 100)
print("\nTotal Winnings > $",calc_winnings(a, b, c, d, e, f))
print("Expenses > $", expenses)
print(f"ROI > {totals} %")








