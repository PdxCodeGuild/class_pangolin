#BieschkeLab25: ATM using classes
'''
Let's represent an ATM with a class containing a balance property. 
A newly created account will default to a balance of 0, but the user should be able 
to modify the starting balance. Implement the initializer, as well as the following methods:

check_balance() returns the account balance
deposit(amount) deposits the given amount in the account
check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
withdraw(amount) withdraws the amount from the account and returns it
'''

class Account():

    def __init__(self, money=0):
        print("Bienvenue to the Bieschke Bank!")
        self.money = money

    def __balance(self):
        return self.money

    def deposit(self):
        self.money += 10500
        return self.money   

    def check_withdrawal(self, money):
        self.withdrawal = 500
        if money >= self.withdrawal:
            return True
        else:
            return False

    def withdraw(self):
        if self.check_withdrawal(self.money) is True:
            self.money -= 500
            return self.money
        else:
            print("I'm sorry Dave, I can't do that.")
            return self.money
b = Account()        

print(b.__balance())
print(b.deposit())
print(b.withdraw())
#print(b.balance())

