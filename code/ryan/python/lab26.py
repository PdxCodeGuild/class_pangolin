class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token

class Game:
    def __init__(self, board):
        self.board = [[" " for i in range(3)] for j in range(3)]

    def __repr__(self):
        board_str = ""
        for row in self.board:
            board_str += '|'.join(row)
            board_str += '\n'
        return board_str  

    def move(self, x, y, player):
        print(self.board[x][y])      

g = Game('board')
print(g.__repr__())
print(g.move(1, 1, "player_1"))
