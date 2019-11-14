# Shawn Stolsig
# PDX Code Guild 
# Assignment: Lab 25 - ATM
# Date: 11/7/2019

class Account:

    def __init__(self):
        '''
        '   Init function for Account class
        '   Account's attributes are a (private) balance and a list of strings, representing the log
        '   Parameters: none (all accounts start with 0 balance) 
        '''
        self.__balance = 0
        self.__log = [f"Account created, balance is ${self.__balance}"]

    def __str__(self):
        '''
        '   Dunder string function for making it easy to print out account balance
        '   Parameters: none    Returns: a string representation of the balance
        '''
        return  f"${self.__balance}"

    def __eq__(self, input_act):
        '''
        '   Dunder equals function for making it easy to compare values of two accounts
        '   Parameters: another account  Returns: boolean (True if accounts are equal)
        '''
        return self.__balance == input_act.check_balance()

    def check_balance(self):
        '''
        '   Function for checking balance of account
        '   Parameters: none        Returns: balance of account (which is stored as a private attribute)
        '''
        return round(self.__balance,2)

    def deposit(self,amount):
        '''
        '   Function for depositing money into accout
        '   Parameters: amount to be deposited      Returns: none
        '''

        # only deposit if a postive number was input:
        try:
            if amount > 0:
                self.__balance += amount
                print(f"${amount} was deposited.")
                self.__log.append(f"${amount} was deposited.")
        except TypeError:
            print("Please input a positive number for deposit.  No changes made to balance.")
            return

    def check_withdrawal(self,amount):
        '''
        '   Function for verifying a withdraw won't overdraft an account
        '   Parameters: amount to be withdrawn      Returns: bool (True if account won't overdraft)
        '''
        # only deposit if a postive number was input:
        try:
            if amount > 0:
                return (self.__balance - amount) >= 0
        except TypeError:
            print("Please input a positive number for withdraw.  No changes made to balance.")
            return None

    def withdraw(self,amount):
        '''
        '   Function for withdrawing money from accout
        '   Parameters: amount to be withdrawn      Returns: amount withdrawn
        '''
        # only deposit if a postive number was input:
        try:
            if amount > 0:
                self.__balance -= amount
                print(f"${amount} was withdrawn.")
                self.__log.append(f"${amount} was withdrawn.")
                return amount
        except TypeError:
            print("Please input a positive number for withdraw.  No changes made to balance.")
            return  0

    def print_transactions(self):
        '''
        '   Function will print out transaction log
        '   Parameters: none    Returns: none (will print out log)
        '''
        print("\nTransaction history: ")
        for transaction in self.__log:
            print(transaction)

# create new empty account
new_account = Account()

# REPL
while True:

    # get user input
    user_input = input("\nWhat would you like to do? \n1: Deposit (d) \n2. Withdraw (w)) \n3. Check balance (c)\n4. Show transaction history (s) \n5. Quit (q)\nYour input: ")

    # check to make sure input is valid
    if user_input == 'd':
        new_account.deposit(float(input("Please input how much to deposit: $")))
    elif user_input == 'w':
        user_withdraw_amount = float(input("Please input how much to withdraw: $"))
        if new_account.check_withdrawal(user_withdraw_amount):
            new_account.withdraw(user_withdraw_amount)
        else:
            print("That amount would overdraft!  Overdraft protection kicking in...no balance change.")
    elif user_input == 'c':
        print(f"Your account balance is: ${new_account.check_balance()}")
    elif user_input == 's':
        new_account.print_transactions()
    elif user_input == 'q':
        break
    else:
        print("Invalid input, please try again.")

print("Program quitting.")