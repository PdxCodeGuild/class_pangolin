account_history = []
class Account:
    
    def __init__(self, b):
        self.balance = b

    def check_balance(self):
        print(f"Your balance is ${self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"You deposited ${amount}. Your new balance is ${self.balance}")
        account_history.append(f"User deposited {amount}.")
        
    def check_withdrawal(self):
        if self.balance - amount > 0:
            return True
        else:
            return False
    
    def withdraw(self, amount):
        self.balance -= amount
        print(f"You withdrew ${amount}. Your new balance is ${self.balance}")
        account_history.append(f"User withdrew {amount}.")

my_account = Account(0)
while True:
    user_input = input("What would you like to do? \n c -- check balance \n d -- deposit \n w -- withdraw \n h -- account history \n x -- exit \n")

    if user_input in ["c", "check", "check balance"]:
        my_account.check_balance()
    elif user_input in ["deposit", "d"]:
        amount = int(input("Enter the amount you would like to deposit. "))
        my_account.deposit(amount)
    elif user_input in ["withdraw", "w"]:
        amount = int(input("Enter the amount you would like to withdraw."))
        is_approved = my_account.check_withdrawal()
        if is_approved == True:
            my_account.withdraw(amount)
        elif is_approved == False:
            print("Sorry, your account balance is too low to withdraw that amount.")
    elif user_input in ["h", "history"]:
        print(account_history)
    elif user_input in ["x", "exit", "quit"]:
        break
    else:
        continue
print("Goodbye.")
