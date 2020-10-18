import random

def playGreedy(board, colour):
  print('counting value')
  moves = {}
  for col in range(len(board[0])):
    # move down to last possible row
    row = 0
    while row < 5 and board[row][col] == 0:
        if board[row][col] == 0 and board[row + 1][col] == 0:
            row += 1
        else:
            break
    moves[col] = adjacentNearMove(board, colour, row, col)
    print(moves[col])
# https://stackoverflow.com/questions/35253971/how-to-check-if-all-values-of-a-dictionary-are-0
  if all(value == moves[0] for value in moves.values()):
    print('all same, choosing random')
    return random.choice(list(moves.keys()))

  return max(moves, key=moves.get)

# calculates the value of a move
def value(board, colour, row, col):
  value = 0
  value += adjacentNearMove(board, colour, row, col)
  return value

def randomMove(board):
  col = random.randint(0,6)
  while (board[0][col] != 0):
    col = random.randint(0,6)
  return col


# counts the number of adjacent same coloured pieces for a given move
# assumes the move given is the same as colour as the colour parameter
def adjacentNearMove(board, colour, row, col):
  oldCol = col
  oldRow = row
  adjacentCount = 0
  # count to the left
  while col > 0:
    if board[row][col-1] == colour:
      adjacentCount += 1
      col -= 1
    else:
      break

  col = oldCol
  row = oldRow
  # count to the right
  while col < 6:
    if board[row][col+1] == colour:
      adjacentCount += 1
      col += 1
    else:
      break

  col = oldCol
  row = oldRow
  # count up
  while row > 0:
    if board[row-1][col] == colour:
      adjacentCount += 1
      row -= 1
    else:
      break

  col = oldCol
  row = oldRow
  # count down
  while row < 5:
    if board[row+1][col] == colour:
      adjacentCount += 1
      row += 1
    else:
      break

  col = oldCol
  row = oldRow
  # up and left
  while row > 0 and col > 0:
    if board[row-1][col-1] == colour:
      adjacentCount += 1
      row -= 1
      col -= 1
    else:
      break

  col = oldCol
  row = oldRow
  # up and right
  while row > 0 and col < 6:
    if board[row-1][col+1] == colour:
      adjacentCount += 1
      row -= 1
      col += 1
    else:
      break

  col = oldCol
  row = oldRow
  # down and left
  while row < 5 and col > 0:
    if board[row+1][col-1] == colour:
      adjacentCount += 1
      row += 1
      col -= 1
    else:
      break

  col = oldCol
  row = oldRow
  # down and right
  while row < 5 and col < 6:
    if board[row+1][col+1] == colour:
      adjacentCount += 1
      row += 1
      col += 1
    else:
      break

  return adjacentCount


# reads board state
# makes a move
def play(board):

  pass


