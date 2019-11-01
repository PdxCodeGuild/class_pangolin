import random


ballance = 0
winning_numbers = 0
num = 0
total_spent = 0
#create a lits of random numbers between 0-99 randomly picking 6 numbers 
ticket = [random.randint(0,100)for winning_ticket in range(6)]
print (ticket)
#create a while loop that runs 100000 times
while num <= 100000:
    winning_numbers = 0
    #take two dollars from the ballance because you spent that on a ticket
    ballance -= 2
    #this is added to total up the amout of money total you spent on a ticket 
    total_spent +=2
    #print ('actual',ballance)

    #create random tickets for each 100000 tickets 
    your_tickets = [random.randint(0, 100) for winning_ticket in range(6)]
    #print (your_tickets)

    #check tikets this method turns them into tuples then you turn them into lists and check the list in a for loop
    check = zip(ticket,your_tickets)
    check2 = list(check)
   # print(check2)
    for x,y in check2:
        if x == y:
            winning_numbers +=1
    
    #print (winning_numbers)
   # if statements covering all the different parameters 
    if winning_numbers == 1:
        print ('you win $4')
        ballance += 4
    elif winning_numbers == 2:
        print ('you win $7')
        ballance += 7
    elif winning_numbers == 3:
        print ('you win $100')
        ballance += 100
    elif winning_numbers == 4:
        print ('you win $50,000')
        ballance += 50000
    elif winning_numbers == 5:
        print ('you win $1,000,000')
        ballance += 1000000
    elif winning_numbers == 6:
        print ('you win $25,000,000')
        ballance += 25000000
    num += 1

#print('your ballance', ballance)

roi = (ballance) - (total_spent)/total_spent
print ('Your overall winnings are: ', ballance)
print ('You spent: ', total_spent)
print('Your roi is: ', roi)



#print (ballance)
# while True:
#     if winning_ticket == your_ticket:
#         print (true)
#     winning_ticket = [random.randint(0,101)for winning_tickit in range(6)]
#     for winning_ticket
#     if 
# ballance += # winnings