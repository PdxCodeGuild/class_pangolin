# Taylor Rebbe 
# Lab_25
# 11/07/19

class BankAccount():
    def __init__(self):
        
        account = 0,
        deposit = 0,
        check_withdrawl = 0,
        withdraw = 0

    def deposit(self, amount):
        ''' Deposits the given amount in the account '''

    def check_balance(self):
        ''' Returns the account balance '''

    def check_withdrawl(self, amount):
        ''' Returns true if hte withdrawn amount won't put the account in the negative '''

    def withdraw(self, amount):
        ''' WIthdraws the amount from hte account and returns it ''' 

    # Version 2
    ''' Have the ATM maintain a list of transactions. Every time the user makes a deposit or withdrawal, add a string to a list saying 'user deposited $15' or 'user withdrew $15'. Add a new function print_transactions() to your class for printing out the list of transactions '''


    # Version 3
    ''' Allow the user to enter commands into a REPL.

    > what would you like to do (deposit, withdraw, check balance, history)?
    > deposit
    > how much would you like to deposit?
    > $5
    > what would you like to do (deposit, withdraw, check balance, history)?
    > check balance
    > balance: $5 '''