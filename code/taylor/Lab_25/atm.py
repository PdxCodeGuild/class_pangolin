import bank_class as bc

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

end_transaction = 'n'

# def define_transaction(selection):
#     if selection == 1:
#         return customer.deposit(int(input(message8)))
#     elif selection == 2:
#         return customer.withdraw(int(input(message8)))
#     elif selection == 3:
#         return customer.check_balance()
#     else:
#         return customer.print_transactions()

    # Get the user's account number
account_number = int(input(message9))
    # Set the account number to an account object
account = bc.BankAccount(account_number)
while True:

    
    if end_transaction != 'y':
        # Deposit to the account
        account.deposit(55.00)
        # Check withdraw for overdraft 
        if account.check_withdraw(10) == True:
            print('True')
        else:
            print('False')
        # Withdraw from the accont
        account.withdraw(10)
        # Print the transactions
        bc.BankAccount.print_transactions(account)
        bc.BankAccount.check_balance(account)

        end_transaction = input(message10)
    else:
        break








# print(jims_account.check_balance())



