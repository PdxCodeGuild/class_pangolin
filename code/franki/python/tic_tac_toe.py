class Player:

    def __init__(self, token, name):
        self.token = token
        self.name = name

    def __repr__(self):
        return self.token

class Board:
    def __init__(self):
        self.board= [['_' for i in range(3)] for j in range(3)]

    def __repr__(self):
        display = ""
        for row in  self.board:
            display += "|".join(row)
            return display
    
    def place_token(self, token, x, y):
        if self.board[y][x] != "_":
            return 'That space is taken! Try again. '
            else:
                self.board[y][x] = token

    def get_winner(self):
        for i in range(3):
            row = self.board[i]
            if row[0] == row[1] == row[2]:
                return row[0]

            column = [self.board[i][j] for j in range(3)]
            if col[0] ==  col[1] == col[2] and col[1] != "_":
                return col[0]
            
            if (self.board[0][0] == self.board[1][1] == self.board[0][0]) and self.board[0][0] != "_":
                return self.board[0][0]

            if (self.board[0][2] == self.board[1][1] == self.board[2][0]) and self.board[1][1] != "_":
                return self.board[1][1]
    
    def is_full(self): 
        for row in self.board:
            for i in range(3):
                if row[i] == "_":
                    return False
            return True
    
    def is_game_over(self):
        if self.is_full() == True:
            return self.get_winner()

    def main(self):