#Bieschke Lab 26: tic tac toe.py

class Game():
    def __init__(self):
        print("Welcome to Tic-Tac-Toe!")

        self.board = {1: '1', 2: '2', 3: '3',
                      4: '4', 5: '5', 6: '6',
                      7: '7', 8: '8', 9: '9'}

    # def printBoard(self, board):
    #     print(self.board[1] + '|' + self.board[2] + '|' + self.board[3])
    #     print('-+-+-')
    #     print(self.board[4] + '|' + self.board[5] + '|' + self.board[6])
    #     print('-+-+-')
    #     print(self.board[7] + '|' + self.board[8] + '|' + self.board[9])
    #     print("\n")
    #     print("*"*50)

    def __repr__(self):
        print(self.board[1] + '|' + self.board[2] + '|' + self.board[3])
        print('-+-+-')
        print(self.board[4] + '|' + self.board[5] + '|' + self.board[6])
        print('-+-+-')
        print(self.board[7] + '|' + self.board[8] + '|' + self.board[9])
        print("\n")
        print("*"*50)

    def movement(self):
        move = int(input("What square would you like to occupy?"))
        #checking()
        if self.checking(move) == True:
            self.board[move] = turn
        else:
            self.movement()
        self.calc_winner()
        self.board_full()
        g.__repr__()

    def checking(self, key):
        if self.board[key] == 'X' or self.board[key] == 'O':
            print("That space has already been taken")
            return False
        else:
            return True

    def calc_winner(self):  
        #conditions for X victory
        if self.board[1]=='X' and self.board[2]=='X' and self.board[3]=='X':
            print("X wins!")
            quit()
        elif self.board[4]=='X' and self.board[5]=='X' and self.board[6]=='X':
            print("X wins!")
            quit()
        elif self.board[7]=='X' and self.board[8]=='X' and self.board[9]=='X':
            print("X wins!")
            quit()
        elif self.board[1]=='X' and self.board[4]=='X' and self.board[7]=='X':
            print("X wins!")
            quit()
        elif self.board[2]=='X' and self.board[5]=='X' and self.board[8]=='X':
            print("X wins!")
            quit()
        elif self.board[3]=='X' and self.board[6]=='X' and self.board[9]=='X':
            print("X wins!")
            quit()
        elif self.board[1]=='X' and self.board[5]=='X' and self.board[9]=='X':
            print("X wins!")
            quit()
        elif self.board[3]=='X' and self.board[5]=='X' and self.board[7]=='X':
            print("X wins!")
            quit()

        #conditions for O victory
        elif self.board[1]=='O' and self.board[2]=='O' and self.board[3]=='O':
            print("O wins!")
            quit()
        elif self.board[4]=='O' and self.board[5]=='O' and self.board[6]=='O':
            print("O wins!")
            quit()
        elif self.board[7]=='O' and self.board[8]=='O' and self.board[9]=='O':
            print("O wins!")
            quit()
        elif self.board[1]=='O' and self.board[4]=='O' and self.board[7]=='O':
            print("O wins!")
            quit()
        elif self.board[2]=='O' and self.board[5]=='O' and self.board[8]=='O':
            print("O wins!")
            quit()
        elif self.board[3]=='O' and self.board[6]=='O' and self.board[9]=='O':
            print("O wins!")
            quit()
        elif self.board[1]=='O' and self.board[5]=='O' and self.board[9]=='O':
            print("O wins!")
            quit()
        elif self.board[3]=='O' and self.board[5]=='O' and self.board[7]=='O':
            print("O wins!")
            quit()
        
        else:
            pass

    def board_full(self):
        full = all([space in ['X', 'O'] for space in self.board.values()])
        
        if full == True:
            print("There are no moves left")
            quit()
        else:
            pass

class Player():
    def __init__(self):
        # self.name = name
        # self.token = token
        #p1 = Player.input_init()
        #p2 = Player.input_init()
        self.p1 = str(input("What is player one's name?"))
        self.p2 = str(input("What is player two's name?"))

    def tokens(self):
        self.players = ['X', 'O']
        self.player1 = input(f"{self.p1}, would you like to be X or O?").upper()
        #self.player1 = input("Who is going first, X or O?\n> ").upper()
        print(f"Great! {self.p1} is {self.player1}!")
        #print(f"Great! {self.player1} is player one!")
        self.players.remove(self.player1)
        self.player2 = str(self.players)
        self.player2 = self.player2.strip("'[]'")
        print(f"That means {self.p2} is {self.player2}! LET'S DO THIS!!")

g = Game()
p = Player()

#print("Hello! And Welcome to TTT!")
p.tokens()
print("Play by entering the number of the square you would like to occupy.")
#g.printBoard(g.board)
g.__repr__()


player = 0

lions = True
while lions == True:
    player +=1
    for player in range(9):
        if player % 2 == 0:
            turn = p.player1
            print(f"{p.p1}'s turn!")
        else:
            turn = p.player2
            print(f"{p.p2}'s turn!")
        g.movement()
