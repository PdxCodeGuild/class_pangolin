'''
Lab 25: ATM - Version 3

Purpose/goal: Allow the user to enter commands into a REPL.

'''

# create atm class
class ATM:

    def __init__(self, balance = 0):
        self.__balance = balance
        self.history = []

    # create check_balance method
    def check_balance(self):
        return format(self.__balance, '.2f')

    # create deposit method
    def deposit(self, amount):
        self.__balance += float(amount)
        self.history.append(f"Deposited ${amount}")
        return format(self.__balance, '.2f')

    # create withdraw_check method
    def withdraw_check(self, amount):
        if self.__balance > float(amount):
            return True
        if self.__balance < float(amount):
            return False

    # create withdrawal method
    def withdrawal(self, amount):
        if self.withdraw_check(amount) == True:
            self.__balance -= float(amount)
            self.history.append(f"Withdrew ${amount}")
            return format(self.__balance, '.2f')
        if self.withdraw_check(amount) == False:
            print(f"Insufficient available funds.\nYour account balance is: ${self.__balance}")

    # create print_transactions method
    def print_transactions(self):
        return self.history


account = ATM()
user_op_list = ["check balance", "deposit", "withdrawal", "history", "quit"]
stars = '*' * 70

print(f"\n{stars}\n\nWelcome.\nThank you for using ATM.")

while True:
    
    user_op = input("Please choose from the following options: check balance, deposit, withdrawal, history or quit: ").lower()

    while user_op not in user_op_list:
        user_op = input("Please choose from the following options: check balance, deposit, withdrawal, history: ").lower()
        if user_op in user_op_list:
            break

    if user_op == "check balance":
        account.check_balance
        print(f"Your current available balance is: ${account.check_balance()}\n")

    if user_op == "deposit":
        amount = input("Please enter your deposit amount: $")
        account.deposit(amount)
        print(f"Your new available balance is: ${account.check_balance()}\n")
        

    if user_op == "withdrawal":
        amount = input("Please enter your withdrawal amount: $")
        account.withdraw_check(amount)
        account.withdrawal(amount)
        print(f"Your new available balance is: ${account.check_balance()}\n")

    if user_op == "history":
        print('\n'.join(account.history), "\n")

    if user_op == "quit":
        print(f"Thank you for using ATM.\nHave a good day!\n\n{stars}\n")
        break