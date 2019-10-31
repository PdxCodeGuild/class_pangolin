#Pick6, lab14.  10/29/2019, Wiley Rummel

#Have the computer play pick6 many times and determine net balance.
#Initially the program will pick 6 random numbers as the 'winner'. 
#Then try playing pick6 100,000 times, with the ticket cost and payoff below.

#A ticket contains 6 numbers, 1 to 99.
#The number of matches between the ticket and the winning numbers determines the payoff.
#Order matters, if the winning numbers are [5,10] and your ticket numbers are [10,5] you have 0 matches
#If the winning numbers are [5,10,2] and your numbers are [10,5,2] you have 1 match. 
#Calculate you net winnings (the sum of all expenses and earnings).

#A ticket costs $2
#if 1 number matches, you win $4
#if 2 numbers match, you win $7
#3 matches, you win $100
#4 matches, you win $50,000
#5 matches, you win $1,000,000
#6 matches, you win $25,000,000

#steps:
#generate a list of 6 random numbers representing the winning tickets 
#start balance 0
#Loop 100,000 times
#for each loop:
#Generate a list of 6 random numbers (computer tickets)
#subtract 2 from you balance
#Find how many numbers match
#Add to your balance the winnings from you matches
#After the loop, print the final balance
import random

#initializing stable variables
attempts = 0
cash = 0
matches = []
earnings = 0
num_of_matches = 0
def pick6_winning():
    '''This function produces a list of 6 random integers between 1-99 to be used as a winning ticket'''
    winning = []
    for i in range(0,6):
        winning.append(random.randint(1,99))
    return winning


winning  = pick6_winning()
print(f"Tonight's numbers are {winning}.")


def pick6_betting():
    '''This function produces a list of 6 random integers between 1-99 to be used as a betting ticket'''
    betting = []
    for i in range(0,6):
        betting.append(random.randint(1,99))
    return betting
betting = pick6_betting()
#print(f"Your ticket is {betting}.")

def compare_lists(x,y):
    '''This function takes in two arguments which are both lists,
    then compares the lists to return the number of matches found.
    A proper match is a number or set of numbers in the corresponding sequence.
    Argument y is checked agaisnt a stable argument x.'''
    matches = [a for a,b in zip(x,y) if a == b]
    #if len(matches) >= 1:
        #print(f"You got a winner! Your matches were: {matches}.")
    return matches


def cash_out(matches):
    '''This function will return a cash value dependent upon the number of matches found in compare_lists()'''
    cash = 0
    if len(matches) == 0:
        return cash
    elif len(matches) == 1:
        cash += 4
        return cash
    elif len(matches) == 2:
        cash += 7
        return cash
    elif len(matches) == 3:
        cash += 100
        return cash
    elif len(matches) == 4:
        cash += 50000
        return cash
    elif len(matches) == 5:
        cash += 1000000
        return cash
    elif len(matches) == 6:
        cash += 25000000
        return cash
        
#User input for how many bets they are going to attempt
attempt_times = int(input("How many bets are you willing to make?"))
while attempts < attempt_times:
    attempts += 1   
    cash -= 2
    
    betting = pick6_betting()
    matches = compare_lists(winning,betting)
    if len(matches) >= 1:  
        cash += cash_out(matches)
        earnings += cash_out(matches)
        num_of_matches += 1
print(f"After betting {attempt_times} times, you went home with {cash} dollars.  Isn't gambling amazing!")
ROI = (earnings - 2*attempt_times)/attempt_times 
print(f"Your ROI was {ROI}")
print(f"You had {num_of_matches} winning tickets!")


