# Tic Tac Toe User Messages and Display
# Thank you for visiting https://asciiart.website/
# This ASCII pic can be found at
# https://asciiart.website/index.php?art=objects/computers

a,b,c,d,e,f,g,h,i = '_','_','_','_','_','_',' ',' ',' '

board_as_list = [a, b, c, d, e, f, g, h, i]

game_board_graphic = f'''\n\n
       ._,-,_.              _    ________    _       ______    __
       ||| |||    {a}|{b}|{c}    / \  |__    __|  / \     |   _  \  |  |
       ||| |||    {d}|{e}|{f}   / . \    |  |    / . \    |  |_) /  |  |
       ;|| ||:    {g}|{h}|{i}  / /_\ \   |  |   / /_\ \   |     (   |  |
     ./ /| |\ \.        /  ___  \  |  |  /  ___  \  |  |\  \  |  |
     |./ :_: \.|       /__/   \__\ |__| /__/   \__\ |__| \__\ |__|\n'''


print(game_board_graphic)

