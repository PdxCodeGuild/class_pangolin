#BieschkeLab25: ATM v2
'''
Version 2
Have the ATM maintain a list of transactions. Every time the user makes a deposit 
or withdrawal, add a string to a list saying 'user deposited $15' or 'user withdrew $15'. 
Add a new function print_transactions() to your class for printing out the list 
of transactions.
'''

class Account():

    def __init__(self, money=0):
        print("Bienvenue to the Bieschke Bank!")
        self.money = money
        self.transactions = ''
        self.transaction_list = []

    def __balance(self):
        return self.money

    def deposit(self):
        self.money += 10500
        self.transactions = f"User deposited ${self.money}"
        self.transaction_list.append(self.transactions)
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
            self.transactions = f"User deposited ${self.money}"
            self.transaction_list.append(self.transactions)
            return self.money
        else:
            print("I'm sorry Dave, I can't do that.")
            return self.money

    def print_transactions(self):
        self.transaction_list.append(self.transactions)
        return self.transaction_list

b = Account()        

print(b.__balance())
print(b.deposit())
print(b.withdraw())
print(b.print_transactions())
#print(b.balance())

