# Create an ATM class.  Create methods.
class ATM:

    def __init__(self, balance=10.0):
        self.balance = balance
        self.__deposit = self.deposit
        self.__withdrawal = self.withdrawal

    def check_balance(self):
        return self.balance

    def deposit(self, deposit):
        self.balance = self.balance + deposit
        return self.balance

    def check_withdrawal(self, withdrawal_amount):
        if withdrawal_amount > self.balance:
            return f"This will make your account negative."
        else:
            return f"Yes, you have enough funds to make this withdrawal."

    def withdrawal(self, withdrawal_amount):
        if withdrawal_amount <= self.balance:
            self.balance = self.balance - withdrawal_amount
            return self.balance


account1 = ATM()
print(account1.check_balance())
print(account1.deposit(100.00))
print(account1.check_withdrawal(1000))
print(account1.withdrawal(100))
