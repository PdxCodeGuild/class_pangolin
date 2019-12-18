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
a.deposit(420)
a.withdraw(40)
a.print_transactions()
print(a.check_balance())
