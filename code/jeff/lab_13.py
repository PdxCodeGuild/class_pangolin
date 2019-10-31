# labe_13.py
# Rot 13 Cypher
# Jeff Smith
'''
Steps
    /Loop 100,000 times, for each loop:
    /Generate a list of 6 random numbers representing the ticket
    Subtract 2 from your balance (you bought a ticket)
    /Find how many numbers match
    Add to your balance the winnings from your matches
    After the loop, print the final balance
'''
# testing.py
# workspace for labs
#
# import random
# res = random.randint(range(0, 100), 6)
# print(str(res))

import random 

lot = random.sample(range(1, 100), 6) 

# counter
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
            bal =+ 4
        print(bal)
        return nums
# print(bal)

# def a_count(in_string):
# return in_string.count('a') 
# total_a = 0
# for num in range(100):
# word = random.choice('bdrnm') + random.choice('aoeui') + random.choice('bdrnm')
# total_a = total_a + a_count(word) 
# total_a
# 14
print(wins(tix, lot))