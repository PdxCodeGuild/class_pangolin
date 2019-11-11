'''
Lab 25: ATM - Version 2

Purpose/goal: Have the ATM maintain a list of transactions. 

    - Every time the user makes a deposit or withdrawal, add a string to    a list saying 'user deposited $15' or 'user withdrew $15'. - D
    
    - Add a new function print_transactions() to your class for printing    out the list of transactions. - D

'''

# create atm class
class ATM:

    def __init__(self, balance = 0):
        self.__balance = balance
        self.history = []

    # create check_balance method
    def check_balance(self):
        return format(self.__balance, '.2f')

    # create deposit method
    def deposit(self, amount):
        self.__balance += float(amount)
        self.history.append(f"Deposited ${amount}")
        return format(self.__balance, '.2f')

    # create withdraw_check method
    def withdraw_check(self, amount):
        if self.__balance > float(amount):
            return True
        if self.__balance < float(amount):
            return False

    # create withdrawal method
    def withdrawal(self, amount):
        if self.withdraw_check(amount) == True:
            self.__balance -= float(amount)
            self.history.append(f"Withdrew ${amount}")
            return format(self.__balance, '.2f')
        if self.withdraw_check(amount) == False:
            print(f"Insufficient available funds.\nYour account balance is: ${self.__balance}")

    # create print_transactions method
    def print_transactions(self):
        return self.history
