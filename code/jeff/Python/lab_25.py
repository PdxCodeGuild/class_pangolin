# lab_25.py
# ATM
# Jeff Smith

# Let's represent an ATM with a class containing a balance property. A newly created account will default to a balance of 0. Implement the initializer, as well as the following methods:

task = input('Welcome to the money tree. We offer the following choices:\nBal= Balance Check\nDep= Deposits\nDraw= Withdrawls\nExit= Quit\nWhat service can we provide for you today? ').lower

class Account:
    def __init__(self, name, balance=0.00):
        self.name = name
        self._balance = balance

    def bal(self):
        '''returns account balance'''
        return self._balance

    def __repr__(self):
        return '{0.__class__.__name__}(name={0.name}, balance={0.balance})'.format(self)

    def __str__(self):
        return 'Bank account of {}, current balance: {}'.format(self.name, self.balance)
        
    def dep(self, amount):
        '''deposits the given amount in the account'''
        self._balance += amount

    def draw(self, amount):
        '''returns true if the withdrawn amount won't put the account in the negative'''
        if amount > self._balance:
            raise ValueError("insufficient funds")
        self._balance -= amount
    
