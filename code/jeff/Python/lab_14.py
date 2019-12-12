
# lab_14.py
# pick6
# Jeff Smith
'''
Steps
    /Loop 100,000 times, for each loop:
    /Generate a list of 6 random numbers representing the ticket
    /Subtract 2 from your balance (you bought a ticket)
    /Find how many numbers match
    /Add to your balance the winnings from your matches
    /After the loop, print the final balance
'''
import random

cost = 2
bal = 0


def wins(tix_param, lot_param):
    nums = [i for i, j in zip(tix_param, lot_param) if i == j]

    if len(nums) == 6:
        bal += 25000000
    elif len(nums) == 5:
        bal += 1000000
    elif len(nums) == 4:
        bal += 50000
    elif len(nums) == 3:
        bal += 100
    elif len(nums) == 2:
        bal += 7
    elif len(nums) == 1:
        bal = + 4
    print(bal)
    return nums, bal


lot = random.sample(range(1, 100), 6)
print(lot)
count = 0

while count < 1000000:
    # print(count)
    count += 1
    # generate random number list
    tix = random.sample(range(1, 100), 6)

    # check tickets against winning numbers
    def wins(tix_param, lot_param):
        nums = [i for i, j in zip(tix_param, lot_param) if i == j]
        bal = -2
        if len(nums) == 6:
            bal += 25000000
        elif len(nums) == 5:
            bal += 1000000
        elif len(nums) == 4:
            bal += 50000
        elif len(nums) == 3:
            bal += 100
        elif len(nums) == 2:
            bal += 7
        elif len(nums) == 1:
            bal = + 4
        print(bal)
        return nums, bal

roi = 2 * 100000
roi1 = bal - roi
roi2 = roi / roi1
roi3 = roi2 * 100
print(f'Based on your balance, your return on your investment is {roi3}%')

print(tix)
print(wins(tix, lot))
