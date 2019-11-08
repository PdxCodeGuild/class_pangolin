# Create an ATM class.  Create methods.

transaction_history = []
user_input = ''


class ATM:

    def __init__(self, balance=100.0):
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
        return transaction_history


account1 = ATM()
while user_input != 'done':
    # print(f"Your balance is: ${account1.check_balance()}")
    user_input = input(
        f"Do you want to 'D'eposit, 'W'ithdraw, 'C'heck Balance, 'V'iew History, or 'Done' to quit? ").lower()
    if user_input == 'd':
        deposit = int(input(f"How much to deposit? $"))
        account1.deposit(deposit)
        transaction_history.append(f"User deposited ${deposit}")
        print(f"Your balance is: ${account1.check_balance()}")
    elif user_input == 'w':
        withdraw = int(input(f"How much to withdraw? $"))
        account1.withdrawal(withdraw)
        transaction_history.append(f"User withdrew ${withdraw}")
        print(f"Your balance is: ${account1.check_balance()}")
    elif user_input == 'c':
        account1.check_balance()
        print(f"Your balance is: ${account1.check_balance()}")
    elif user_input == 'v':
        print(account1.print_transactions())
# print(transaction_history)
