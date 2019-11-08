# Using classes Player and Game, create a game board and player attrib.


# class Player:
#     def __init__(self):
#     #player_name
#     #token


class Game:

    def __init__(self):
        game_board = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append((0))
            game_board.append(row)

        #print(game_board)
        for bl in game_board:
            print(bl)
    #__repr__()
    #move(x,y,player_name)
    #calc_winner
    #is_full
    #is_game_over

new_game = Game()
