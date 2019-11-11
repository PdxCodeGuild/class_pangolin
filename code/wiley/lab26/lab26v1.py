'''Tic Tac Toe game
11/8/19 Wiley Rummel
Practice Class, Object Orientation, Parent Classes'''


class Player:
    
    def __init__(self, name, token):
        self.name = name
        self.token = token

    def __repr__(self):
        return f"name is {self.name}, token is {self.token}"
    
players = []
for elem in 'XO':
    players.append(Player(name = input("What is your name?"),
    token = elem
    ))

print(players)


class Game:
    
    def __init__(self):
        self.board =[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        
    def __repr__(self):
        board2 = []
        for line in self.board:
            board2.append('|'.join(line))        
        return '\n'.join(board2)
    def move(self,x,y,player):
        self.y = self.board[y]
        self.x = self.board[y][x]
        self.player = player
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
 

        
        



        



play = Game()
#play.calc_winner()
play.is_full()
play.__repr__()
#play.move()
