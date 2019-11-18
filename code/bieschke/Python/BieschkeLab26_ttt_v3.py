#Bieschke Lab 26_v3: tic tac toe.py

class Game():
    def __init__(self):
        print("Welcome to Tic-Tac-Toe!")

        self.board = {1: '1', 2: '2', 3: '3',
                      4: '4', 5: '5', 6: '6',
                      7: '7', 8: '8', 9: '9'}

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
    def __init__(self, name, token):
        self.name = name
        self.token = token
        #p1 = Player.input_init()
        #p2 = Player.input_init()

def tokens():
    players = ['X', 'O']
    player1 = input(f"{p1}, would you like to be X or O?").upper()
    print(f"Great! {p1} is {player1}!")
    players.remove(player1)
    player2 = str(players)
    #player2 = player2.strip("'[]'")
    player2 = player2[2:-2]
    print(f"That means {p2} is {player2}! LET'S DO THIS!!")

# player1 = ''
# player2 = ''
# turn = ''

# p1 = Player('D', "O")
# p2 = Player('Brandon', "X")

# p1 = str(input("What is player one's name?"))
# p2 = str(input("What is player two's name?"))

g = Game()
p = Player(name, token)

tokens()
print("Play by entering the number of the square you would like to occupy.")
g.__repr__()

player = 0

lions = True
while lions == True:
    player +=1
    for player in range(9):
        if player % 2 == 0:
            turn = p.player1
            print(f"{p1}'s turn!")
        else:
            turn = p.player2
            print(f"{p2}'s turn!")
        g.movement()
