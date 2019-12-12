abc = [" ","a", " ", "b", " ", "c"]
row1 = ["1", "_", "|", "_", "|", "_"]
row2 = ["2", "_", "|", "_", "|", "_"]
row3 = ["3", "_", "|", "_", "|", "_"]

while True:
    player_move = input("What is your move?: ")

    if player_move == "a1":
        row1[1] = "X"
    if player_move == "a2":
        row2[1] = "X"
    if player_move == "a3":
        row3[1] = "X"

    if player_move == "b1":
        row1[3] = "X"
    if player_move == "b2":
        row2[3] = "X"
    if player_move == "b3":
        row3[3] = "X"

    if player_move == "c1":
        row1[5] = "X"
    if player_move == "c2":
        row2[5] = "X"
    if player_move == "c3":
        row3[5] = "X"

    rows = ''.join(abc), ''.join(row1), ''.join(row2), ''.join(row3)
    gameboard = '\n'.join(rows)

    print(gameboard)