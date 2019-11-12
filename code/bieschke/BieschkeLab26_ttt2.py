#tic tac toe
#without OOP 

board = {1: '1', 2: '2', 3: '3',
         4: '4', 5: '5', 6: '6',
         7: '7', 8: '8', 9: '9'}

def checking(key):
    #move = board[key]
    #if key[value] is X or O:
    if board[key] == 'X' or board[key] == 'O':
        print("That space has already been taken")
        return False
    else:
        return True

    #         new_value = search(board[value])
    #         upper_keys = [key.upper() for key in keys]
    #         new_value[upper_keys.index(value)] = move
    #         print(new_value)
    # #all(value == 'O' for value in board.values())

def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print("\n")
    print("*"*50)

def victory():  
    #conditions for X victory
    if board[1]=='X' and board[2]=='X' and board[3]=='X':
        print("X wins!")
        quit()
    elif board[4]=='X' and board[5]=='X' and board[6]=='X':
        print("X wins!")
        quit()
    elif board[7]=='X' and board[8]=='X' and board[9]=='X':
        print("X wins!")
        quit()
    elif board[1]=='X' and board[4]=='X' and board[7]=='X':
        print("X wins!")
        quit()
    elif board[2]=='X' and board[5]=='X' and board[8]=='X':
        print("X wins!")
        quit()
    elif board[3]=='X' and board[6]=='X' and board[9]=='X':
        print("X wins!")
        quit()
    elif board[1]=='X' and board[5]=='X' and board[9]=='X':
        print("X wins!")
        quit()
    elif board[3]=='X' and board[5]=='X' and board[7]=='X':
        print("X wins!")
        quit()

    #conditions for O victory
    elif board[1]=='O' and board[2]=='O' and board[3]=='O':
        print("O wins!")
        quit()
    elif board[4]=='O' and board[5]=='O' and board[6]=='O':
        print("O wins!")
        quit()
    elif board[7]=='O' and board[8]=='O' and board[9]=='O':
        print("O wins!")
        quit()
    elif board[1]=='O' and board[4]=='O' and board[7]=='O':
        print("O wins!")
        quit()
    elif board[2]=='O' and board[5]=='O' and board[8]=='O':
        print("O wins!")
        quit()
    elif board[3]=='O' and board[6]=='O' and board[9]=='O':
        print("O wins!")
        quit()
    elif board[1]=='O' and board[5]=='O' and board[9]=='O':
        print("O wins!")
        quit()
    elif board[3]=='O' and board[5]=='O' and board[7]=='O':
        print("O wins!")
        quit()
    
    else:
        pass

def board_full():
    full = all([space in ['X', 'O'] for space in board.values()])
    
    if full == True:
        print("There are no moves left")
        quit()
    else:
        pass

def movement():
    move = int(input("What square would you like to occupy?"))
    #checking()
    if checking(move) == True:
        board[move] = turn
    else:
        movement()
    victory()
    board_full()
    printBoard(board)

def participation():
    players = ['X', 'O']

    player1 = input("Who is going first, X or O?\n> ").upper()
    print(f"Great! {player1} is player one!")
    player2 = players.pop(player1)
    print(f"That means player two is {player2}! LET'S DO THIS!!")

print("Hello! And Welcome to TTT!")
participation()
print("Play by entering the number of the square you would like to occupy.")
printBoard(board)

player = 0

lions = True
while lions == True:
    player +=1
    for player in range(9):
        if player % 2 == 1:
            turn = player1
            print("Player 1's turn!")
        else:
            turn = player2
            print("Player 2's turn!")
        movement()
