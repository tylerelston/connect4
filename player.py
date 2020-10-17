import random

# calculates the value of a move
def value(board, colour, move):

  pass

def randomMove(board):
  col = random.randint(0,6)
  while (board[0][col] != 0):
    col = random.randint(0,6)
  return col


  # counts the number of adjacent same coloured pieces for a given move
  # assumes the move given is the same as colour as the colour parameter
  def blanksNearMove(board, colour, row, col):
    adjacentCount = 0

    # count to the left
    while col > 0:
      print(board[row][col-1])
      if board[row][col-1] == colour:
        adjacentCount += 1
        col -= 1

    return adjacentCount






# reads board state
# makes a move
def play():
  pass


