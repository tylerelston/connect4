import random

def playGreedy(board, colour, display):
  moves = {}
  if colour == "B":
    oppColour = "R"
  else:
    oppColour = "B"
    
  moveDisplay = ""
  for col in range(len(board[0])):
    # move down to last possible row
    if board[0][col] == 0:
      row = 0
      while row < 5 and board[row][col] == 0:
          if board[row][col] == 0 and board[row + 1][col] == 0:
              row += 1
          else:
              break
      value = 0
      value += adjacentNearMove(board, colour, row, col)
      value += opponentWin(board, colour, row, col)
      value += selfWin(board, colour, row, col)
      value += blockOpp(board, oppColour, row, col)

      moves[col] = value
  moveDisplay += '------------------------------------------------------------\n'
  moveDisplay += 'Moves in the form of Column:Value the player is considering:\n'
  moveDisplay += str(moves) + '\n'
  # https://stackoverflow.com/questions/35253971/how-to-check-if-all-values-of-a-dictionary-are-0
  if len(moves) > 0 and all(value == random.choice(list(moves.values())) for value in moves.values()):
    moveDisplay += 'All moves are equal value\n'
    move = random.choice(list(moves.keys()))
    moveDisplay += 'Choosing randomly: ' + str(move) + '\n'
    return random.choice(list(moves.keys()))

  move = max(moves, key=moves.get)
  moveDisplay += 'Choosing: ' + str(move) + '\n'

  if display:
    print(moveDisplay)

  return move

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

  '''col = oldCol
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
      break'''

  return adjacentCount

# return infinite value for move that blocks opponent win
def opponentWin(board, colour, row, col):
  return 0

# return infinite value for winning move
def selfWin(board, colour, row, col):
  return 0

# counts the amount of consecutive tiles the opponent has (up to 3)
# and chooses to block the most threatening move
# assumes colour is of the opponent, not self.
def blockOpp(board, colour, row, col):
  oldCol = col
  oldRow = row

  oppCount = 0

  #count to the left
  while col > 0:
    if board[row][col-1] == colour:
      oppCount += 1
      col -= 1
    else:
      break

  if oppCount == 3:
    return 9999999999
  else:
    oppCount = 0  
  col = oldCol
  row = oldRow
  # count to the right
  while col < 6:
    if board[row][col+1] == colour:
      oppCount += 1
      col += 1
    else:
      break
    
  if oppCount == 3:
    return 9999999999
  else:
    oppCount = 0    
  col = oldCol
  row = oldRow
  # count up 
  while row > 0:
    if board[row-1][col] == colour:
      oppCount += 1
      row -= 1
    else:
      break

  if oppCount == 3:
    return 9999999999
  else:
    oppCount = 0  
  col = oldCol
  row = oldRow
  # count down
  while row < 5:
    if board[row+1][col] == colour:
      oppCount += 1
      row += 1
    else:
      break

  if oppCount == 3:
    return 9999999999
  else:
    oppCount = 0  
  col = oldCol
  row = oldRow
  # up and left
  while row > 0 and col > 0:
    if board[row-1][col-1] == colour:
      oppCount += 1
      row -= 1
      col -= 1
    else:
      break

  if oppCount == 3:
    return 9999999999
  else:
    oppCount = 0  
  col = oldCol
  row = oldRow
  # up and right
  while row > 0 and col < 6:
    if board[row-1][col+1] == colour:
      oppCount += 1
      row -= 1
      col += 1
    else:
      break

  return oppCount


# reads board state
# makes a move
def play(board):

  pass


