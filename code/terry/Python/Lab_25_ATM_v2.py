# Create an ATM class.  Create methods.

"""Sets global variables"""
transaction_history = []
user_input = ''

"""Class ATM"""


class ATM:
    """The balance is set to $100 for testing purposes"""

    def __init__(self, balance=100.0):
        self.balance = balance
        self.__deposit = self.deposit
        self.__withdrawal = self.withdrawal

    """Check balance is used to return the current balance of the account in ATM"""

    def check_balance(self):
        return self.balance

    """Accepts the deposited amount and adds it to the balance"""

    def deposit(self, deposit):
        self.balance = self.balance + deposit
        return self.balance

    """This verifies that there is enough funds in balance to make the withdrawal"""

    def check_withdrawal(self, withdrawal_amount):
        if withdrawal_amount > self.balance:
            return f"This will make your account negative."
        else:
            return f"Yes, you have enough funds to make this withdrawal."

    """This does not check before the withdrawal is made, but instead just subtracts the amount"""

    def withdrawal(self, withdrawal_amount):
        if withdrawal_amount <= self.balance:
            self.balance = self.balance - withdrawal_amount
            return self.balance

    """Prints the user's transaction history"""

    def print_transactions(self):
        return transaction_history


"""sets the user to account1"""
account1 = ATM()
"""A while loop continues to prompt the user"""
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
