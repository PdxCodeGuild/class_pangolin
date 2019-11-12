'''Tic Tac Toe game
11/8/19 Wiley Rummel
Practice Class, Object Orientation, Parent Classes'''


class Player:
    
    def __init__(self, name, token):
        self.name = name
        self.token = token

    def __repr__(self):
        return self.token
    
players = []

for elem in 'XO':
    players.append(Player(name = input("What is your name?"),
    token = elem
    ))
#print(players)




class Game:
    
    def __init__(self):
        self.board =[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        
    def __repr__(self):
        board2 = []
        for line in self.board:
            board2.append('|'.join(line))        
        return '\n'.join(board2)
    def move(self,x,y,player):
        self.board[x][y] = player.token
        
    def calc_winner(self):
        for row in range(len(self.board)):
            if len(set(self.board[row])) == 1:
                return f"The winning is {set(self.board[row])}!"
        diag_check = []
        diag_check.extend([self.board[0][0], self.board[1][1], self.board[2][2]])
        if len(set(diag_check)) == 1:
            return f"The winner is {self.board[0][0]}!"
        diag_check2 = []
        diag_check2.extend([self.board[0][2], self.board[1][1], self.board[2][0]])
        if len(set(diag_check2)) == 1:
            return f"The winner is {self.board[0][2]}!"
        vert_check = []
        vert_check.extend([self.board[0][0], self.board[1][0], self.board[2][0]])
        if len(set(vert_check)) == 1:
            return f"The winner is {self.board[0][0]}!"
        vert_check2 = []
        vert_check2.extend([self.board[0][1], self.board[1][1], self.board[2][1]])
        if len(set(vert_check2)) == 1:
            return f"The winner is {self.board[0][1]}!"
        vert_check3 = []
        vert_check3.extend([self.board[0][2],self.board[1][2], self.board[2][2]])
        if len(set(vert_check3)) == 1:
            return f"The winner is {self.board[0][2]}!"
        

    def is_full(self):
        full_check = []
        for row in range(len(self.board)):
            for elem in range(len(self.board[row])):
                if self.board[row][elem] == 'O' or self.board[row][elem] == 'X':    
                    full_check.append(self.board[row][elem])
                else:
                    break
        return len(full_check) == 8
    def is_game_over(self):
        if self.is_full() and not self.calc_winner():
            return f"CAT, no winner!"
def player_move():
    move_x = int(input("What is the x value of the spot you want to move?"))
    move_y = int(input('What is the y value of the spot you want to move?'))
    # if g.board[move_y][move_x] == 'X' or g.board[move_y][move_x] == 'O':
    #     return print("Not a valid move. Cheaters lose.  Goodbye")
        

    return move_x,move_y

def player_turn(player_list):
    player_list * 4 + [player_list[0]]
    return player_list.pop(0)

def tictactoe(player_list):
    '''This is a REPL loop function to play TicTacToe based on classes built above.'''       
    start_game = input("Want to play TicTacToe?(Y/N)").lower()
    if start_game == 'y':
        start_game == True
    elif start_game == 'n':
        start_game == False
    else:
        print("Not a valid selection. Please enter Y or N")
    # p = Player()
    g = Game()
    move_counter = 0
    
    #print(player_list)        
    print(f"The current board is: \n{g}")
    while start_game:    
        print("New Turn")
        try:
            print(f"{player_list[move_counter % 2]}'s turn: ")
            g.move(*player_move(), player_list[move_counter % 2])
        except ValueError:
            print("Not an acceptable X or Y value. Must be a number.")
        except IndexError:
            print("Not an acceptable X or Y value.  Must be 0,1 or 2.")
        print(g)
        move_counter +=1
        if move_counter > 5:
            g.calc_winner()
            print(f"{player_list.name} wins")
        if move_counter == 9:
            g.is_full()
            g.is_game_over()
            print("CAT")
            break




tictactoe(players)