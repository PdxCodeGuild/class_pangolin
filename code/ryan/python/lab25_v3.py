class ATM:
    def __init__(self):
        self.balance = 0
        self.transactions = []

    def check_balance(self):
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"user deposited ${amount}")

    def check_withdrawal(self, amount):
        if self.balance - amount >= 0:
            return True
        return False

    def withdraw(self, amount):
        self.balance -= amount
        self.transactions.append(f"user withdrew ${amount}")

    def print_transactions(self):
        print(self.transactions)

a = ATM()

while True:
    action = input("What would you like to do? ((d)eposit, (w)ithdraw, (c)heck balance, (h)istory).  Enter 'done' to exit.  ")
    if action == "d":
        amount = int(input("How much would you like to deposit?  $"))
        a.deposit(amount)
    elif action == "w":
        amount = int(input("How much would you like to withdraw?  $")) 
        if a.check_balance() - amount >= 0:
            a.withdraw(amount)
        else:
            print("You don't have enough money in your account!") 
    elif action == "c":
        print(f"Your balance is:  ${a.check_balance()}")
    elif action == "h":
        a.print_transactions()
    else:
        break    



