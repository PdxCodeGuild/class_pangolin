
class Player():

    def __init__(self,name,token):
        
        self.name = name
        self.token = token

    def __str__(self):
        return self.name
#print(Player)   

class Board(object):
    #init to initialise list of cells with length 9
    def __init__(self):
        self.cells = [" "]*9
      #  print(self.cells)
    #displays board in a presentable order
    def display(self):
        #print(self.cells)
        print(self.cells[0] + '|' + self.cells[1] + '|' + self.cells[2])
        print('------')
        print(self.cells[3] + '|' + self.cells[4] + '|' + self.cells[5])
        print('------')
        print(self.cells[6] + '|' + self.cells[7] + '|' + self.cells[8])

    #updates board
    def update(self, cell_num,player):
        if self.cells[cell_num-1] == " ":
            self.cells[cell_num-1] = player
        return player
    
    def update2(self,cell_num,player):
        if self.cells[cell_num-1] == " ":
            self.cells[cell_num-1] = player
        return player
           
            
    #checks all conditions for winner
    def iswinner(self, player):

        #horizontal check
        if (self.cells[0]==player and self.cells[1]==player and self.cells[2]==player):
            return True
        if (self.cells[3]==player and self.cells[4]==player and self.cells[5]==player):
            return True
        if (self.cells[6]==player and self.cells[7]==player and self.cells[8]==player):
            return True
        
        #vertical check
        if (self.cells[0]==player and self.cells[3]==player and self.cells[6]==player):
            return True
        if (self.cells[1]==player and self.cells[4]==player and self.cells[7]==player):
            return True
        if (self.cells[2]==player and self.cells[5]==player and self.cells[8]==player):
            return True
        
        #diagonal check
        if (self.cells[0]==player and self.cells[4]==player and self.cells[8]==player):
            return True
        if (self.cells[2]==player and self.cells[4]==player and self.cells[6]==player):
            return True

    #resets board to starting board
    def reset(self):
        self.cells = [" "]*9

    #checks for tie aka board full
    def check(self):
        used = 0
        for cell in self.cells:
            if cell != " ":
                used = used + 1
        if used == 9:
            return True
        else:
            return False
        

def Welcome():
    print("Welcome to tic tac toe\n")
    board.display()
        #player.__init__()

board = Board()
#player = Player()
Welcome()

p1 = Player(input('Player 1 what is your name?'), 'x')
p2 = Player(input('Player 2 what is your name?'), 'o')
token1 = ('x')
token2 = ('o')
# print(p1.__dict__)
# print(p2.__dict__)

while True:
    
    #get X input 
    x = int(input(f"\n Please choose from 1-9\n{p1}\n "))
    board.update(x,token1)
    board.display()

    #check if X is winner
    if(board.iswinner(token1)):
        print(f'\n {p1} wins !')
        replay = input('Do you want to play again ? (Y/N):  ').upper()
        if(replay == "Y"):
            board.reset()
        else:
            break

    #check if it is a tie
    if(board.check()):
        print('\n Tie!')
        replay = input('Do you want to play again ? (Y/N):  ').upper()
        if(replay == "Y"):
            board.reset()
        else:
            break
        
    #get o input
    o = int(input(f"\n Please choose from 1-9\n {p2}\n "))
    board.update2(o, token2)
    board.display()

    #check if o is winner
    if(board.iswinner(token2)):
        print(f'\n {p1} wins !')
        replay = input('Do you want to play again ? (Y/N):  ').upper()
        if(replay == "Y"):
            board.reset()
        else:
            break
        
    #check if it is a tie
    if(board.check()):
        print('\n Tie !')
        replay = input('Do you want to play again ? (Y/N):  ').upper()
        if(replay == "Y"):
            board.reset()
        else:
            break