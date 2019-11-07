# Create an ATM class.  Create methods.

class ATM:
    balance = 0.0

    def __init__(self, balance):
        self.__balance = balance
        self.__deposit = self.deposit
        self.__withdrawal = self.withdrawal

    def check_balance(self, balance):
        print(f"{balance}")

    def deposit(self, deposit, balance):
        balance += deposit

    def check_withdrawal(self, balance, withdrawal_amount):
        if withdrawal_amount > balance:
            print(f"This will make your account negative")

    def withdrawal(self, balance, withdrawal_amount):
        if withdrawal_amount <= balance:
            balance -= withdrawal_amount
