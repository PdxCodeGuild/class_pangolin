'''
pick 6 lab 14
written by Rhornberger
last update oct 30 2019
'''
import random
import string
import re
balance = 0
# create a random set of 6 numbers
def pick6():
    six_string = []
    for i in range(6):
        six_string.append(random.randint(1,99))
    return six_string
# check the 2 lists against each other
def num_match(winning, ticket):
    matches = [i for i, j in zip(winning, ticket) if i == j]
    return len(matches)
# buy tickets
def buy():
    num_of_tickets= []
    #balance = 0
    for i in range(100000):
        #balance -= 2
        num_of_tickets.append(pick6())
    return len(num_of_tickets)

def lottery():
    winning_ticket = pick6()
    balance = 0
    tick = 0
    while tick < 100000:
        tick += 1
        balance -= 2
        ticket = pick6()
        matches = [i for i, j in zip(winning_ticket, ticket) if i == j]
        if len(matches) == 6:
            balance += 25000000
            print(f'Big Winner! You had six matches {matches}! you win 25,000,000. Your balance is {balance}')
        elif len(matches) == 5:
            balance += 1000000
            print(f'Winner! You had five matches {matches}! You win $1,000,000. Your balance is {balance}')
        elif len(matches) == 4:
            balance += 50000
            print(f'Winner! You had four matches {matches}, you win $50,000. Your balance is {balance}')
        elif len(matches) == 3:
            balance += 100
            print(f'You win. You had three matches {matches}, you win $100. Your balance is {balance}')
        elif len(matches) == 2:
            balance += 7
            print(f'You had two matches {matches}, you win $7. Your balance is {balance}.')
        elif len(matches) == 1:
            balance += 4
            print(f'You had one match {matches}, You win $4. Your balance is {balance}. ')
       
    print(winning_ticket)
    return matches
print(lottery())

