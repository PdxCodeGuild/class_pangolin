# Create an ATM class.  Create methods.

transaction_history = []


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

    def print_transactions(self):
        print(transaction_history)


account1 = ATM()
print(account1.check_balance())
user_input = input(f"Do you want to 'D'eposit, 'W'ithdraw, 'C'heck Balance, or 'V'iew History? ").lower()
if user_input == 'd':
    deposit = int(input(f"How much to deposit? $"))
    ATM.deposit(deposit)
elif user_input == 'w':
    withdraw = int(input(f"How much to withdraw? $"))
    ATM.withdrawal(withdraw)
elif user_input == 'c':
    ATM.balance()
elif user_input == 'v':
    ATM.print_transactions()