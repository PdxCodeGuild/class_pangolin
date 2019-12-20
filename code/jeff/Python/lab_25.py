# lab_25.py
# ATM
# Jeff Smith


class ATM:
    # task = input('Welcome to the money tree. We offer the following choices:\nBal= Balance Check\nDep= Deposits\nDraw= Withdrawls\nExit= Quit\nWhat service can we provide for you today? ').lower

    def __init__(self):
        self.transactions = []
        self.balance = 0

    def bal(self):
        '''returns account balance'''
        self.transactions.append(f'User checked balance: ${self.balance}')
        return self.balance

    def deposit(self, amount):
        ''' Deposits the given amount in the account'''
        self.transactions.append(f'User deposited ${amount}')
        self.balance += amount

    def print_transactions(self):
        ''' Print list of user transactions'''
        for line in self.transactions:
            print(line)

    def check_withdrawal(self, amount):
        ''' Returns true if the withdrawn amount won't put the account in the negative'''
        return self.balance > amount

    def withdraw(self, amount):
        ''' Withdraws the amount from the acount and returns it'''
        if self.check_withdrawal(amount):
            self.transactions.append(f'User withdrew ${amount}')
            self.balance -= amount
            return amount
        else:
            self.transactions.append(
                f'User unsuccessfully tried to withdraw ${amount}')
            return 'Insufficient funds.'


if __name__ == '__main__':
    atm = ATM()
    valid_inputs = ['deposit', 'd', 'withdraw', 'w',
                    'check balance', 'b', 'history', 'h', 'exit', 'x']
    # while True:
    while True:
        op = input(
            "What would you like to do? \n((d)eposit, (w)ithdraw, check (b)alance, check (h)istory, or e(x)it): ").strip().lower()
        if op not in valid_inputs:
            print('not valid')
        if op in ['exit', 'x']:
            print('Goodbye!')
            break
        elif op in ['deposit', 'd', 'withdraw', 'w']:
            while True:
                op = 'deposit' if op.startswith('d') else 'withdraw'
                try:
                    amount = int(
                        input(f"How much would you like to {op}: ").strip('$'))
                    break
                except ValueError:
                    print('Invalid input.')
        if op == 'deposit':
            atm.deposit(amount)
        elif op == 'withdraw':
            print(f'Withdrawing ${amount}... {atm.withdraw(amount)}')
        elif op in ['check balance', 'b']:
            print(f'Balance: ${atm.bal()}')
        elif op in ['check history', 'h']:
            atm.print_transactions()
