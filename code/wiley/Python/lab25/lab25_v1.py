#ATM Lab25 
#11/7/19 Wiley Rummel
'''Represent an ATM with a class containing a balance property. A newly created account will default to a balance of 0. 
Implement the initializer, as well as the following methods: 
check_balance() >>> returns the account balance
deposit(amount) >>> deposits the given amount in the account.
check_withdrawal(amount)>>> returns True if the withdrawn amount won't put the account in the negative.
withdrawal(amount)>>> withdraws the amount from the account and returns it.  '''

class ATM:
    def __init__(self, balance=0):
        self.__balance = balance
        self.ledger = list()
        
    
    def __str__(self):
        return f"The balance of you account is: {self.__balance}."
    

    def check_balance(self):
        return self.__balance
    

    def deposit(self, amount):
        self.__balance += amount
        self.ledger.append(f"Account deposited {amount}. ")
        return self.__balance ,self.ledger
    
    def check_withdrawal(self, amount):
        if amount < self.__balance:
            return True
        if amount > self.__balance:
            return False
    
    def withdrawal(self, amount):
        if self.check_withdrawal(amount) == True:
            self.__balance -= amount
            self.ledger.append(f"User withrew {amount}.")
            return self.__balance
        if self.check_withdrawal(amount) == False:
            return f"Insufficeint funds to withdrawal {amount} from your account.  Your balance is {self.__balance}."
            
    def print_transaction(self):
        return self.ledger


account = ATM()

while True:
    print("Accessing your account...")
    user_choice = input("""
    What would you like to do?
    Enter 'cb' to check your balance.
    Enter 'd' to make a deposit.
    Enter 'w' to make a withdrawal.
    Enter 'e' to end the transaction. 
    Enter 'l' to show your transaction history.""").lower()
    if user_choice == 'cb':
        print(f"Your account balance is: {account.check_balance()}")
    elif user_choice == 'd':
        deposit_amount = int(input("How much do you want to deposit?"))
        account.deposit(deposit_amount)
        print(account.check_balance())
    elif user_choice == 'w':
        withdrawal_amount = int(input("How much do you want to withdrawal?"))
        account.withdrawal(withdrawal_amount)
        print(account.withdrawal(withdrawal_amount))
        print(account.check_balance())
    elif user_choice == 'l':
        print(account.ledger)

    elif user_choice == 'e':
        print("Goodbye.")
        break
    else:
        raise ValueError ("Not a proper selection.")
