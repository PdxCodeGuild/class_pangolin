'''
Lab 25: ATM - Version 1

Purpose/goal: Represent an ATM with a class containing a balance property. 

    - A newly created account will default to a balance of 0. - D
    
    Implement the initializer, as well as the following methods:

    - check_balance() returns the account balance - D

    - deposit(amount) deposits the given amount in the account - D

    - check_withdrawal(amount) returns true if the withdrawn amount won't   put the account in the negative - D

    - withdraw(amount) withdraws the amount from the account and returns    it - D

'''

# create atm class
class ATM:

    def __init__(self, balance = 0):
        self.__balance = balance

    # create check_balance method
    def check_balance(self):
        print(self.__balance)

    # create deposit method
    def deposit(self, amount):
        self.__balance += amount
        return self.__balance

    # create withdraw_check method
    def withdraw_check(self, amount):
        if self.__balance > amount:
            return True
        if self.__balance < amount:
            return False

    # create withdrawal method
    def withdrawal(self, amount):
        if self.withdraw_check(amount) == True:
            self.__balance -= amount
            return self.__balance
        if self.withdraw_check(amount) == False:
            print(f"Insufficient available funds. Your account balance is: ${self.__balance}")




        
    





