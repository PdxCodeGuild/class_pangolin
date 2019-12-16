class ATM:
    def __init__(self):
        self.balance = 0

    def check_balance(self):
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount

    def check_withdrawal(self, amount):
        if self.balance - amount >= 0:
            return True
        return False

    def withdraw(self, amount):
        return self.balance - amount

a = ATM()
a.deposit(420)
print(a.check_balance())
print(a.check_withdrawal(426))
print(a.withdraw(42))