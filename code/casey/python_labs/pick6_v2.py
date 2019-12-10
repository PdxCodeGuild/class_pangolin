'''
Lab 14: Pick6 - Version 2

    - calculate your ROI - D
    - print it out along with your earnings and expenses - D

'''
import random

# define balance & earnings / expenses
balance = 0
earnings = 0
expenses = 0

# define winner ticket
winner = []
for i in range (6):
    winner.append(random.randrange(1, 100, 1))

# pick6 function
def pick6():
    ticket = []
    for i in range (6):
        ticket.append(random.randrange(1, 100, 1))
    return ticket

# create ticket matching function
def num_matches(ticket, winner):
    matches = [i for i, j in zip(ticket, winner) if i == j]
    return matches

# create lottery loop 
lottery = 0
while lottery < 1000:
    # pay $2 for ticket / subtract from balance & expenses
    balance -= 2
    expenses -= 2
    # find ticket/winner number matches
    ticket = pick6()
    matches = num_matches(ticket, winner)
    # assess $ winnings / add to balance & earnings
    index = len(matches)
    win_list = [0, 4, 7, 100, 5000, 1000000, 25000000]
    balance += win_list[index]
    earnings += win_list[index]
    # if len(matches) == 1:
    #     balance += 4
    # if len(matches) == 2:
    #     balance += 7
    # if len(matches) == 3:
    #     balance += 100
    # if len(matches) == 4:
    #     balance += 50000
    # if len(matches) == 5:
    #     balance += 1000000
    # if len(matches) == 6:
    #     balance += 25000000
    # increase lottery counter
    lottery += 1
    print(ticket)
    print(winner)
    print(matches)

# calculate / return ROI 
roi = (earnings - expenses) / expenses 
    
print(f"After playing the lottery 1000 times, you have a blanace of {balance} dollars.\nYour earnings came out to {earnings} dollars.\nYour expenses came out to {expenses} dollars.\nYour ROI is {roi}.\nVery sad.")