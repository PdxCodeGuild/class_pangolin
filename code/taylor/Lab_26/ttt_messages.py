# Tic Tac Toe User Messages and Display
# Thank you for visiting https://asciiart.website/
# This ASCII pic can be found at
# https://asciiart.website/index.php?art=objects/computers

a,b,c,d,e,f,g,h,i = '_','_','_','_','_','_',' ',' ',' '

board_as_list = [a, b, c, d, e, f, g, h, i]

0, 1, 2, 3, 4, 5, 6, 7, 8

''' Win Definition '''
# if abc = X or O
# if aei = X or O
# if adg = X or O
# if beh = X or O
# if cfi = X or O
# if def = X or O
# if ghi = X or O

game_board_graphic = f'''\n\n
       ._,-,_.              _    ________    _       ______    __
       ||| |||    {a}|{b}|{c}    / \  |__    __|  / \     |   _  \  |  |
       ||| |||    {d}|{e}|{f}   / . \    |  |    / . \    |  |_) /  |  |
       ;|| ||:    {g}|{h}|{i}  / /_\ \   |  |   / /_\ \   |     (   |  |
     ./ /| |\ \.        /  ___  \  |  |  /  ___  \  |  |\  \  |  |
     |./ :_: \.|       /__/   \__\ |__| /__/   \__\ |__| \__\ |__|\n'''


print(game_board_graphic, board_as_list[0])

