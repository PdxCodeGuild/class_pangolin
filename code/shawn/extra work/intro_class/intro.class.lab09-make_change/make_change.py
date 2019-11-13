# Shawn Stolsig
# PDX Code Guild 
# Assignment: Intro Class Lab 9 - Make Change
# Date: 10/24/2019

import math

# function to turn input amount to pennies
def makePennies(amount):
    ''' function takes a decimal amount and returns amount of pennies '''

    # declare variables for number of each other type of coin
    dollars = int(math.modf(amount)[1])
    cents = int(100*round(math.modf(amount)[0],2))

    return 100 * dollars + cents

# function to figure out the optional way of turning pennies amount into provided coin currency
def makeChange(amount, coins):
    ''' function takes number of pennies and a sorted list of dictionary coin types
    and returns a list of how many of each coin '''

    # iterate through each coin in the sorted high to low list of custom coin
    for coin in coins:
        # figure out how many of that type of coin you can withdraw from the total amount, update dictionary with that amount
        coin['amount'] = amount // coin['value']
        # deduct from the amount the value of the coins you just withdrew
        amount -= coin['value'] * coin['amount']
        # for debugging:
        # print(f"you deducted {coin['amount']} of {coin}")

    # return list of coin dictinoaries, which cointains the amounts of each
    return coins

# function for creating a string from the number and quantity of each coin
def coinString(coins):
    ''' function takes a list of coin dictionaries that values/amounts and returns a string ''' 
    return_string = 'You have '
    for coin in coins:
        return_string += f"{coin['amount']} {coin['name']} "
    return_string += '.'
    return return_string

# function for returning value of key so that you can sort list of dictionaries
def getValue(coinType):
    return coinType['value']

# let user create custom set of coins
def createCoinCatalog():

    # initalize coin set to include pennies
    coin_set = [ { 'name': 'pennies', 'value': 1, 'amount': 0}  ]

    # loop for adding coins until user decides to stop
    while True:

        # get name and value of coin
        new_name = input("please enter coin name: ")
        new_value = int(input("please enter how many pennies this coin is worth: "))

        # add coin to new set
        coin_set.append({'name': new_name, 'value': new_value, 'amount': 0})

        # ask to see if they want to keep making coins
        more_coins = input("create additional coins?  input \'yes\' or \'no\': ")
        if more_coins == 'yes':
            pass
        elif more_coins == 'no': 
            return coin_set
        else:
            print("you input a typo, you're coin set is now finalized")
            return coin_set


# declare a running total of money (in pennies)
running_total_in_pennies = 0

# coins will be tracked using a list of each coin, represented as a dictionary with three keys:
# 'name', 'value', and 'amount'.  These will later be sorted by coin value.

# list of US currency coins to give user option of using these or creating their own
american_coins = [
    { 'name': 'pennies', 'value': 1, 'amount': 0},
    { 'name': 'quarters', 'value': 25, 'amount': 0},
    { 'name': 'dimes', 'value': 10, 'amount': 0},
    { 'name': 'nickles', 'value': 5, 'amount': 0}  
]

# determine if user wants to create their own set of coins or not
# get user's currency
while True:
    input_coins = input("do you want to create your own set of coins? input \'yes\' or \'no\': ")
    # edge case: keep asking for input if given negative number
    if input_coins == 'yes':
        coin_catalog = createCoinCatalog()
        break
    elif input_coins == 'no':
        coin_catalog = american_coins
        break
    else:
        print("try input again please")

# display coin set being used
print('your coins being used are: ')
for coin in coin_catalog:
    print(f"coin name/value: {coin['name']}/{coin['value']}")

# main loop
while True:

    # get operation from user
    while True:
        user_operation = input("choose (add) (subtract) or (done): ")
        if user_operation in ['add', 'subtract']:
            break
        elif user_operation == 'done':
            print("quitting")
            exit()

    # get user's money
    while True:
        input_money = float(input("please input dollar amount: " ))
        # edge case: keep asking for input if given negative number
        if input_money >= 0:
            break

    # get custom currency

    # sort custom currency
    coin_catalog.sort(reverse = True, key=getValue)

    # add operation
    if user_operation == 'add':
        running_total_in_pennies += makePennies(input_money)
        print(coinString(makeChange(running_total_in_pennies,coin_catalog)))

    # subtract operation
    elif user_operation == 'subtract':
        running_total_in_pennies -= makePennies(input_money)
        if running_total_in_pennies <= 0:
            print("You are out of money!")
            # reset your balance to zero when you want out of money to avoid working with negative coins
            running_total_in_pennies = 0
        else:
            print(coinString(makeChange(running_total_in_pennies, coin_catalog)))
        
