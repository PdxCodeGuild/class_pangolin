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
        self.balance = balance
        
    
    def __str__(self):
        return f"The balance of you account is: {self.balance}."
    
    #def __add__(self, amount):
       # self.amount += self.balance
        #return self.balance

    # def __sub__(self, amount):
    #     self.balance -= self.amount
    #     return self.balance

    # def __ge__(self, amount):
    #     if self.balance >= self.amount:
    #         return True
    # def __le__(self,amount):
    #     if self.balance <= self.amount:
    #         return False

    def check_balance(self):
        return self.balance
    

    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def check_withdrawal(self, amount):
        if amount > self.balance:
            return True
        if amount < self.balance:
            return False
    
    def withdrawal(self, amount):
        if self.check_withdrawal(amount) == True:
            self.balance -= amount
            return self.balance
        if self.check_withdrawal(amount) == False:
            return f"Insufficeint funds to withdrawal {amount} from your account.  Your balance is {self.balance}."


account = ATM()


while True:
    print("Accessing your account...")
    user_choice = input("""
    What would you like to do?
    Enter 'cb' to check your balance.
    Enter 'd' to make a deposit.
    Enter 'w' to make a withdrawal.
    Enter 'e' to end the transaction. """).lower()
    if user_choice == 'cb':
        print(f"Your account balance is: {account.check_balance()}")
    elif user_choice == 'd':
        deposit_amount = int(input("How much do you want to deposit?"))
        account.deposit(deposit_amount)
        print(account.check_balance())
    elif user_choice == 'w':
        withdrawal_amount = int(input("How much do you want to withdrawal?"))
        account.withdrawal(withdrawal_amount)
        print(account.check_balance())
    elif user_choice == 'e':
        print("Goodbye.")
        break
    else:
        raise ValueError ("Not a proper selection.")
