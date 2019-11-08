# Taylor Rebbe 
# Lab_25
# 11/07/19

class BankAccount:

    def __init__(self, number):
        self.number = number
        self.account = 0
        self.transactions = []
    
    def __str__(self):
        ''' String dunder to format output of "self" '''
        return f"Account [ {self.number} ]"
 
    def deposit(self, amount=0):
        ''' Deposits the given amount in the account '''
        self.account += amount
        self.transactions.append(f"{self} Deposited > ${amount}")
        return self.account

    def check_balance(self):
        ''' Returns the account balance '''
        return print(self.account)

    def withdraw(self, amount=0):
        ''' WIthdraws the amount from the account and returns it '''
        self.account -= amount
        self.transactions.append(f"{self} Withdrew: > ${amount}")
        return self.account

    def check_withdraw(self, amount=0):
        ''' Returns true if the withdrawn amount won't put the account in the negative '''
        if self.account - amount >= 0:
            return True

    def print_transactions(self):
        ''' Print transaction record function as list of strings '''
        return print(self.transactions)
    
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
    

