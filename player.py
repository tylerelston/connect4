import random

# calculates the value of
def value(board, colour):
  pass

def randomMove(board):
  col = random.randint(0,6)
  while (board[0][col] != 0):
    col = random.randint(0,6)
  return col

# reads board state
# makes a move
def play():
  pass