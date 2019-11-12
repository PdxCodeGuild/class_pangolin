'''
ATM lab in which we wrtie a class
written by Rhornberger
last updated nov 7 2019 
'''
#import modules that might be used
import math


# make a class
class Bank():
    #bank transaction list
    
    #initialize an account
    def __init__(self, balance = 0):
        self.balance = balance
    # function to check balance
    def check_balance(self):
        return self.balance
        
    # function to deposite money
    def deposit(self, amount):
        self.balance += amount
        self.transaction_list
        print(f'you have deposited ${amount}') 
        
        return self.balance
    # function to check if pulling out an amount of money will put your account into the negative
    def check_withdrawl(self, amount):
        if amount <= self.balance:
            return True
        else:
            return False

    # withdrawl from the the account
    def withdrawl(self, amount):
        if self.check_withdrawl(amount):
            self.balance -= amount
            self.transaction_list
            print(f'You have withdrawn ${amount}')
            #return self.balance
        else:
            print('You do not have enough money in your account!')
    # create a list of transactions
    def transaction_list(self,amount):
        trans_list = []
        # if self.transaction_list in self.balance:
        #     print(f'you have deposited {amount}')
        # elif self.transaction_list in self.withdrawl:
        #     print( f'You have withdrawn {amount}')
        trans_list.append(amount)
        #print(f'you have changed your account by ${amount}')

# A function that allows options in their use
b1 = Bank()
def bank_func():
    user_input = input('Here at Online bank we are commmited to offering excelence in our options. Please read closely as our options may have changed.\nIf you would like to check your balance please enter "b".\nIf you would like to make a deposit please enter "d".\nIf you would like to make a withdrawl please enter "w".\nIf you would like to exit Online Bank please enter "q".\nPlease make your selection now: ').lower()
    
    if user_input == 'b':
        print(b1.balance)
    elif user_input == 'd':
        user_deposit = input('How much would you like to deposite in this transaction?: ')
        user_deposit = int(user_deposit)
        b1.deposit(user_deposit)
    elif user_input == 'w':
        user_withdrawl = input('How much would you like to withdrawl?: ')
        user_withdrawl = int(user_withdrawl)
        b1.withdrawl(user_withdrawl)
    elif user_input == 'q':
        print('OK')
        quit()
    else:
        print('This was not a valid entry. Please try again at a time that better fits your convenience')
#call on the function and run the program.
bank_func()
user_choice = input('Would you like to make a transaction?\nPlease enter "y" for yes: \nAnd "n" for no: ').lower()
while user_choice == 'y':
    bank_func()
    user_choice = input('Would you like to make a transaction?\nPlease enter "y" for yes: \nAnd "n" for no: ').lower()
else: 
    print('Thank you for using Online Bank, we hope that we have succesfully provided a pleasent experience for you.')







