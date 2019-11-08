#BieschkeLab25: ATM v3
'''
Version 3
Allow the user to enter commands into a REPL.
'''

class Account():

    def __init__(self, money=0):
        print("Bienvenue to the Bieschke Bank!")
        self.__money = money
        self.transactions = ''
        self.transaction_list = []

    def balance(self):
        return self.__money

    def deposit(self):
        self.__money += deposit
        self.transactions = f"User deposited ${self.__money}"
        self.transaction_list.append(self.transactions)
        #return self.__money   

    def check_withdrawal(self, money):
        self.withdrawal = withdraw
        if money >= self.withdrawal:
            return True
        else:
            return False

    def withdraw(self):
        if self.check_withdrawal(self.__money) is True:
            self.__money -= withdraw
            self.transactions = f"User withdrew ${withdraw}"
            self.transaction_list.append(self.transactions)
            #return self.__money
        else:
            print("I'm sorry Dave, I can't do that. Insufficient funds")
            #return self.__money

    def print_transactions(self):
        #self.transaction_list.append(self.transactions)
        return self.transaction_list

b = Account()        
lions = True
while lions == True:
    action = input("You can deposit, withdraw, check balance, or history, or enter q or 1 to quit.\n>")

    if action in ('d', 'deposit'):
        deposit = int(input("How much would you like to deposit?\n> "))
        b.deposit()

    elif action in ('w', 'withdraw'):
        withdraw = int(input("How much would you like to withdraw?\n> "))
        b.withdraw()
    
    elif action in ('c', 'check'):
        print("Today we check your balance!")
        print(b.balance())

    elif action in ('h', 'history'):
        print("Today we check history!")    
        print(b.print_transactions())
    
    elif action in ('q', '1'):
        print("Sayonara!")
        quit()

