# Shawn Stolsig
# PDX Code Guild 
# Assignment: Lab 14 - Pick 6
# Date: 10/29/2019

import random

# define dictionary for looking up winnings
winnings = dict([(0,0), (1,4), (2,7), (3,100), (4,50000), (5,1000000), (6,25000000)])

# function for generating list of 6 random numbers
def pick6():
    ''' takes no arguments, returns a list of 6 ints each between 1 and 99 '''
    return_list = []
    for i in range(0,6):
        return_list.append(random.randint(1,99))
    return return_list

# function for comparing two lists of numbers
def compare_numbers(num_list1, num_list2):
    ''' function takes two lists of six numbers and returns how many in a row are the same '''
    counter = 0
    while num_list1[counter] == num_list2[counter]:
        counter += 1
    return counter

# Generate a list of 6 random numbers representing the winning tickets
winning_nums = pick6()

# Start your balance at 0
balance = 0
earnings = 0
loops = 100000
expenses = 2 * loops

# Loop 100,000 times, for each loop:
for count in range(0,loops):
    # Generate a list of 6 random numbers representing the ticket
    ticket = pick6()
    # Subtract 2 from your balance (you bought a ticket)
    balance -= 2
    # Find how many numbers match
    matched_nums = compare_numbers(winning_nums,ticket)

    # print a message when you have two or more in a row
    if winnings[matched_nums] > 4:
        print(f'winning ticket: {winning_nums} this ticket: {ticket}  **** winnings of: ${winnings[matched_nums]}')
    # track sum of winnings seperate from balance
    earnings += winnings[matched_nums]
    # Add to your balance the winnings from your matches
    balance += winnings[matched_nums]

# After the loop, print the final balance
print(f'you won: ${earnings} but after buying tickets your balance is now: ${balance}')
print(f'your ROI is: {round(((earnings - expenses) / expenses )*100,2)}%')