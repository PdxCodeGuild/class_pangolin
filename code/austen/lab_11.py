def operation():

    while True:
        operation_type = input('What operation would you like to preform? +, -, *, / : ')
        first_num = float(input('What is the first number? '))
        second_num = float(input('What is the second number? '))

        print(f'{first_num} {operation_type} {second_num}')
        if operation_type == '+':
            print(first_num + second_num)
        elif operation_type == '-':
            print(first_num - second_num)
        elif operation_type == '*':
            print(first_num * second_num)
        elif operation_type == '/':
            print(first_num / second_num)
        else:
            print('Please enter a valid responce: ')

operation()

while True:
    ask_again= input('Would you like to try different numbers? ')
    if ask_again in ['yes','y']:
        operation()
    elif ask_again in ['no', 'n']:
        print('Thank you for participating')
        break
    else:
        print ('please enter a valid option * yes or no * ')
   
        