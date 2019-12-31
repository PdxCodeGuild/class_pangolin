'''
Lab 14: Pick6 - Version 1

Purpose/goal: Have the computer play pick6 many times and determine net balance.

    - Generate a list of 6 random numbers representing the winning tickets - D

    - Start your balance at 0 - D

    - Loop 1000 times, for each loop: - D
    
    - Generate a list of 6 random numbers representing the ticket - D
    
    - Subtract 2 from your balance (you bought a ticket) - D
    
    - Find how many numbers match - D
    
    - Add to your balance the winnings from your matches - D
    
    - After the loop, print the final balance - D
'''
import random

# define balance
balance = 0

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
    # pay $2 for ticket / subtract from balance
    balance -= 2
    # find ticket/winner number matches
    ticket = pick6()
    matches = num_matches(ticket, winner)
    # assess $ winnings / add to balance
    index = len(matches)
    win_list = [0, 4, 7, 100, 5000, 1000000, 25000000]
    balance += win_list[index]
    lottery += 1
    print(ticket)
    print(winner)
    print(matches)

print(f"After playing the lottery 1000 times, you have a blanace of {balance} dollars.")
