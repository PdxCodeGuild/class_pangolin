
''' Win Definition '''
a = [0, 1, 2] 
b = [0, 4, 8] 
c = [0, 3, 6] 
d = [1, 4, 7] 
e = [2, 5, 8] 
f = [3, 4, 5] 
g = [6, 7, 8] 

board = ['O', 'X', 'X', 'O', '_', '_', 'O', ' ', ' ']
winning_list = []

def x_check(board):
  x_list = []
  for i in range(len(board)):
    if board[i] == 'X':
      x_list.append(i)
      continue
  print(x_list)
  if winner(x_list) != None:
    print('X is the winner')
    return x_list

def o_check(board):
  o_list = []
  for i in range(len(board)):
    if board[i] == 'O':
      o_list.append(i)
      continue
  print(o_list)
  if winner(o_list) != None:
    print('O is the winner')
    return o_list

def winner(check_list):
  if check_list == a or check_list == b or check_list ==c or check_list == d or check_list == e or check_list == f or check_list == g:
    return 0 
  else:
    return None

x_check(board)
o_check(board)


  # if check_list == [0,1,2]:
  #   return check_list
  # elif check_list == [0,4,8]:
  #   return check_list
  # elif check_list == [0,3,6]:
  #   return check_list
  # elif check_list == [1,4,7]:
  #   return check_list
  # elif check_list == [2,5,8]:
  #   return check_list
  # elif check_list == [3,4,5]:
  #   return check_list
  # elif check_list == [6,7,8]:
  #   return check_list
  # else: 
  #   return False




def calc_winner(self):
  ''' calc_winner() What token character string has won or None if no one has. '''

def is_full(self):
  ''' is_full() Returns true if the game board is full. '''
        
def is_game_over(self):
  ''' is_game_over() Returns true if the game board is full or a player has won. '''

