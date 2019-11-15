# Taylor Rebbe 
# Lab_25
# 11/07/19

# Imports the bank_class module
import bank_class as bc

# User message variables
message1 = 'Enter (1) Deposit, (2) Withdrawl (3) Check Balance or (4) History > '
message2 =  'How much would you like to deposit? > '
message3 =  'How much would you like to withdraw? > '
message4 =  'Check Balance'
message5 =  'Make a Deposit'
message6 =  'Make a Withdraw'
message7 =  'View History'
message8 =  'Enter an ammount: > '
message9 =  'Enter an account number: > '
message10 = 'Would you like to end this transaction ( Y , N )? > '

# Main loop break variable
end_transaction = 'n'
 # Get the user's account number
account_number = int(input(message9))
# Set the account number to an account object
account = bc.BankAccount(account_number)

# Runs class methods based of user selection.
def define_transaction(selection):
    ''' This function receives the selection of the user and calls the respective BankAccount Class methods. '''
    if selection == 1:
        account.deposit(float(input(message8)))
    elif selection == 2:
        amount = float(input(message8))
        if account.check_withdraw(amount) == True:
            account.withdraw(amount)
        else:
            print('Overdraft: Please make a deposit or decrease the withdraw.')
    elif selection == 3:
             account.check_balance()
    else:
        account.print_transactions()

# Main program loop
while True:
    if end_transaction != 'y':
        define_transaction(int(input(message1)))
        end_transaction = input(message10)
    else:
        break
