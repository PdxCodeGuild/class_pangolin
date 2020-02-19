class Player:

    def __init__(self, name, token):
        self.token = token
        self.name = name

    def __repr__(self):
        return self.name

class Board:

    def __init__(self):
        self.board= [['_', 'a', 'b', 'c'], ['1', '_', '_', '_'], ['2', '_', '_', '_'], ['3', '_', '_', '_']]
        self.is_game_over = False

    def __repr__(self):
        display = ""
        for row in self.board:
            display += "|".join(row)
            display += '\n'
        return display
    
    def place_token(self, x, y, token):
        if self.board[y][x] != "_":
            return 'That space is taken! Try again. '
        else:
            self.board[y][x] = token

    def get_winner(self):
        a = self.board[1][1]
        b = self.board[1][2]
        c = self.board[1][3]
        d = self.board[2][1]
        e = self.board[2][2]
        f = self.board[2][3]
        g = self.board[3][1]
        h = self.board[3][2]
        i = self.board[3][3]

        if a == b == c and c != "_":
            return c
        elif d == e == f and f != "_":
            return f
        elif g == h == i and i != "_":
            return i
        elif a == d == g and g != "_":
            return g
        elif b == e == h and h != "_":
            return h
        elif c == f == i and i != "_":
            return i
        elif a == e == i and i != "_":
            return i
        elif c == e == g and g != "_":
            return g
        elif self.is_full == True:
                return "draw"
        else:
            return "incomplete"
    
    def is_full(self): 
        for row in self.board:
            for i in range(3):
                if row[i] == "_":
                    return False
            return True

    def main(self):
        print(self.board)


x_values = {'a': 1, 'b': 2, 'c': 3}
while True:
    board = Board()
    name_one = input("Player One, enter your name. ")
    player_one = Player(name_one, "X")
    name_two = input("Player Two, enter your name. ")
    player_two = Player(name_two, "0")
    print(board)
    turns_count = 0
    

    while board.is_game_over == False:
        X = input(f"{player_one.name}, enter your move (column)").lower()
        Y = input(f"{player_one.name}, enter your move (row)")
        Y = int(Y)
        X = x_values[X]
        board.place_token(X, Y, player_one.token)
        print(board)

        X = input(f"{player_two.name}, enter your move (column)").lower()
        Y = input(f"{player_two.name}, enter your move (row)")
        Y = int(Y)
        X = x_values[X]
        board.place_token(X, Y, player_two.token)
        print(board)
        turns_count += 1
        print(f"rounds: {turns_count}")
        if turns_count >= 3:
            winning_token = board.get_winner()
            print(f"winning token: {winning_token}")
            if winning_token == "draw":
                print("It's a draw!")
                board.is_game_over = True
            elif winning_token == "incomplete":
                continue
            else:
                if winning_token == player_one.token:
                    print(f"{player_one} wins!!!")
                    board.is_game_over = True
                elif winning_token == player_two.token:
                    print(f"{player_two} wins !!!")
                    board.is_game_over = True

    if input("Would you like to play again? ").lower() not in ['yes', 'y']:
        break