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
    oldCol = col
    oldRow = row
    adjacentCount = 0

    # count to the left
    while col > 0:
      print(board[row][col-1])
      if board[row][col-1] == colour:
        adjacentCount += 1
        col -= 1
      else:
        break

    col = oldCol
    row = oldRow
    # count to the right
    while col < 6:
      print(board[row][col+1])
      if board[row][col+1] == colour:
        adjacentCount += 1
        col += 1
      else:
        break

    col = oldCol
    row = oldRow
    # count up
    while row < 0:
      print(board[row-1][col])
      if board[row-1][col] == colour:
        adjacentCount -= 1
        row -= 1
      else:
        break

    col = oldCol
    row = oldRow
    # count down
    while col < 6:
      print(board[row+1][col])
      if board[row+1][col] == colour:
        adjacentCount += 1
        row += 1
      else:
        break

    return adjacentCount






# reads board state
# makes a move
def play():
  pass


