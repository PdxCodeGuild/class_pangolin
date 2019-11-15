import itertools

"""This function/method checks for winning positions"""


def win(current_game):
    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False

    # horizontal
    for row in game:
        print(row)
        if all_same(row):
            print(f"Player {row[0]} has won horizontally!")
            return True

    # vertical
    for col in range(len(game[0])):
        check = []
        for row in game:
            check.append(row[col])
        if all_same(check):
            print(f"Player {check[0]} has won vertically!")
            return True

    # / diagonal
    diags = []
    for idx, reverse_idx in enumerate(reversed(range(len(game)))):
        diags.append(game[idx][reverse_idx])

    if all_same(diags):
        print(f"Player {diags[0]} has won diagonally!")
        return True

    # \ diagonal
    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])

    if all_same(diags):
        print(f"Player {diags[0]} has won diagonally!")
        return True

    return False


"""This function/method sets the game board, checks for occupied spaces and checks to make sure the columns and rows 
are in range """


def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print("This space is occupied, try another!")
            return False

        print("   " + "  ".join([str(i) for i in range(len(game_map))]))
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map
    except IndexError:
        print("IndexError, please choose between 0, 1, 2")
        return False
    except Exception as e:
        print(str(e))
        return False


"""Sets the game play to True as long as the user chooses to play"""
play = True
"""Sets the players to player 1 or player 2"""
players = [1, 2]
"""A blank playing board to start the game"""
while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    game_won = False
    """Cycles between player 1 and player 2"""
    player_cycle = itertools.cycle([1, 2])
    game_board(game, just_display=True)
    while not game_won:
        current_player = next(player_cycle)
        played = False
        """Prompts the player for a choice of column and row"""
        while not played:
            print(f"Hello Player: {current_player}")
            column_choice = int(input("Which column? "))
            row_choice = int(input("Which row? "))
            played = game_board(game, player=current_player, row=row_choice, column=column_choice)
        """At the end of a game, asks the user if they wish to play again"""
        if win(game):
            game_won = True
            again = input("The game is over, would you like to play again? 'Y'es or 'N'o ").lower()
            if again == "y":
                print("New game.")
            elif again == "n":
                print("Goodbye.")
                play = False
            else:
                print("Not valid, closing")
                play = False
