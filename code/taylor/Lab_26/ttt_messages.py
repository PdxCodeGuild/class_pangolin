
''' Win Definition '''
winning_definitions = [[0, 1, 2], [0, 4, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [3, 4, 5], [6, 7, 8]] 

board = ['X', 'O', 'X', 'X', 'X', 'O', 'O', 'X', 'X']
winning_list = []

def x_check(board):
  ''' Function to continuously build a list of X's '''
  x_list = []
  for i in range(len(board)):
    if board[i] == 'X':
      x_list.append(i)
      continue
  print(x_list)
  if winner(x_list) != None:
    return 'X'

def o_check(board):
  ''' Function to continuously build a list of O's '''
  o_list = []
  for i in range(len(board)):
    if board[i] == 'O':
      o_list.append(i)
      continue
  print(o_list)
  if winner(o_list) != None:
    return 'O'

def winner(check):
  ''' Function to check if the winnning definitions are a subset of the build lists 'x_check() and o_check' '''
  for i in range(len(winning_definitions)):
    if set(winning_definitions[i]).issubset(check):
      print('chicken dinner')
    else:
      print('no winner')

x_check(board)

def calc_winner(self):
  ''' calc_winner() What token character string has won or None if no one has. '''

def is_full(self):
  ''' is_full() Returns true if the game board is full. '''
  for i in range(len(self)):
    if self[i] == ' ' or self[i] == '_':
      return False
  else:
    return True



        
def is_game_over(self):
  ''' is_game_over() Returns true if the game board is full or a player has won. '''

print(is_full(board))