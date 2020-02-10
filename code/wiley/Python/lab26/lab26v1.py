'''Tic Tac Toe game
11/8/19 Wiley Rummel
Practice Class, Object Orientation, Parent Classes'''


class Player:
    '''Defining a class Player that takes in a name and assigns a token X or O'''
    
    def __init__(self, name, token):
        self.name = name
        self.token = token

    def __repr__(self):
        return self.token
   
players = []
'''Taking user input ans assigning the token'''
for elem in 'XO':
    players.append(Player(name = input("What is your name?"),
    token = elem
    ))


class Game:
    '''Defining Game class. '''
    def __init__(self):
        '''Initializing the game board as a list of 3 lists containing 3 empty string element'''
        self.board =[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        
    def __repr__(self):
        '''Representing the game board. Prints it in a user readable format.'''
        board2 = []
        for line in self.board:
            board2.append('|'.join(line))        
        return '\n'.join(board2)
    
    def move(self,x,y,player):
        '''Game.move method takes in an x value and y value for locating the move and placing a player token accordingly.'''
        self.board[x][y] = player.token
    
    def player_move(self):
        '''Game.player_move gets user input and returns a tuple which is unpacked to assign the x,y coordinates of the players' move. '''
        move_x = int(input("What is the x value of the spot you want to move?"))
        move_y = int(input('What is the y value of the spot you want to move?'))
        if self.board[move_y][move_x] == 'X' or self.board[move_y][move_x] == 'O':
            print("Not a valid move. Cheaters lose.  Goodbye")

        return move_y,move_x
    def get(self, *args):
        '''Game.get method takes in a tuple of x,y coordinates on the game board to check if the space is still free to take.'''
        return self.board[args[0]][args[1]]
        
    def calc_winner(self):
        '''calc_winner checks to see if Game.board has any winning matches according to TicTacToe regulation.'''
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
        '''Game.is_full method finds if the board is filled with X's or O's  by itterating through the lists and 
        appending the elements to a new list and checking its length. It returns True if so.'''
        full_check = []
        for row in range(len(self.board)):
            for elem in range(len(self.board[row])):
                if self.board[row][elem] == 'O' or self.board[row][elem] == 'X':    
                    full_check.append(self.board[row][elem])
                else:
                    break
        return len(full_check) == 8
    def is_game_over(self):
        '''Game.is_game_over methods checks if the board is full and no winner is found.'''
        if self.is_full() and not self.calc_winner():
            return f"CAT, no winner!"
    

def tictactoe(player_list):
    '''This is a REPL loop function to play TicTacToe based on classes built above.'''       
    
    g = Game() #mades an object 'g' that is class Game()
    move_counter = 0
            
    print(f"The current board is: \n{g}") #prints the formatted game board 
    while True:    
        print("New Turn")
        try: #catches inproper inputs
            print(f"{player_list[move_counter % 2].name}'s turn: ")
            place = g.player_move()
            if g.get(*place) == ' ':
                y, x = place
                g.board[y][x] = player_list[move_counter % 2].token
                move_counter +=1

        except ValueError:
            print("Not an acceptable X or Y value. Must be a number.")
        except IndexError:
            print("Not an acceptable X or Y value.  Must be 0,1 or 2.")
        print(g)
        if move_counter > 4 and g.calc_winner():
            print(f"{player_list[(move_counter%2) - 1]} wins")
            break
        if move_counter == 9:
            g.is_full()
            g.is_game_over()
            print("CAT")
            break

tictactoe(players)