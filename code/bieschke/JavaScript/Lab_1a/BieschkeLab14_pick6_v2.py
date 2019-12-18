#Bieschke Lab 14: pick6.py 

import random

winners = []
expenses = 0
earnings = 0
ticket_master = []

def roi():
    print("ROI is:")
    return ((earnings - expenses)/expenses)

#generates 6 winning numbers and prints them
for i in range (0, 6):
    winner = random.randint(1, 99)
    winners.append(winner)

print(winners)

lions = 0
#number of tickets
while lions < 100000:
    lions += 1
    expenses -= 2   #each ticket costs $2
    ticket = []

    #generates 6 player numbers
    for i in range (0, 6):
        dig = random.randint(1, 99)
        ticket.append(dig)

    print(ticket)
    #ticket = winners       cheat code
    
    matches = []    #set an empty list to hold player numbers to run the check

    for i in range(len(winners)):
        #for j in range(i, len(ticket)):    #this code just matches numbers,
            #print(ticket[j], winners[i])   #regardless of index
        if ticket[i] == winners[i]:
            #print("Match!")
            matches.append(ticket[i])
            print(matches)
    if matches != []:
        if len(matches) == 1: 
            earnings +=4
        elif len(matches) == 2: 
            earnings +=7
        elif len(matches) == 3: 
            earnings +=100
        elif len(matches) == 4: 
            earnings +=50000
        elif len(matches) == 5: 
            earnings +=1000000
        elif len(matches) == 6: 
            earnings +=25000000
        
    ticket_master.append(ticket)
    
print(roi())