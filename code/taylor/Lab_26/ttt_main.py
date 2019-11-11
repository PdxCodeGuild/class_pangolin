import ttt_messages as t3msg    
import ttt_classes as t3cls

print(t3cls.Game(t3msg.board))


def main():
    return None

# 1) Take in player inofrmaiton name, token
# 2) Print the Empty board

# Game Loop -

# 3) Ask player 1 to move
    # - is the space available? True = allow
    # else "Location is full"
# 4) Move player 2 (Random Choice)

# 5) run is_game_over() to determine board is full or there was a winner.
    # 5a) run calc_winner to check for win.
        # -itterate through list if / else for win 3*x or o in a row
    # 5b) Run calc to check if board full.
        # -itterate through list to check if '_' or ' 'remaining.