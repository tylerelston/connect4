# holds all game data and methods

class Game:

  def __init__(self): 
    self.board = [[0 for num in range(7)] for row in range(6)]

  # evaluates board for a winning state
  def evaluateState(self):
      consecutive = 1
      # check for row win
      for col in range(len(self.board[0])):
          prevColour = 0
          for row in range(len(self.board)):
              colour = self.board[row][col]
              if colour != 0 and prevColour == colour:
                  consecutive += 1
              else:
                  consecutive = 1
              prevColour = colour

              if consecutive == 4:
                  return colour

      # check for column win
      for row in range(len(self.board)):
        for col in range(len(self.board[row])):
          colour = self.board[row][col]
          if colour != 0 and prevColour == colour:
              consecutive += 1
          else:
              consecutive = 1
          prevColour = colour

          if consecutive == 4:
              return colour

      # check for diagonal win
      for row in range(len(self.board)):
        for col in range(len(self.board[row])):
          # up and left
          colour = self.board[row][col]
          consecutive = 1
          tempRow = row
          tempCol = col
          while colour != 0 and tempRow > 0 and tempCol > 0:
            if self.board[tempRow-1][tempCol-1] == colour:
              consecutive += 1
              tempRow -= 1
              tempCol -= 1
              if consecutive == 4:
                return colour
            else:
              break

          # up and right
          colour = self.board[row][col]
          consecutive = 1
          tempRow = row
          tempCol = col
          while colour != 0 and tempRow > 0 and tempCol < 6:
            if self.board[tempRow-1][tempCol+1] == colour:
              consecutive += 1
              tempRow -= 1
              tempCol += 1
              if consecutive == 4:
                return colour
            else:
              break


      # check if every piece filled
      emptyExists = False
      for row in range(len(self.board)):
        for col in range(len(self.board[row])):
          colour = self.board[row][col]
          if colour == 0:
            emptyExists = True

      if not emptyExists:
        return -1
      return 0

  # place piece, returns row placed at
  def placePiece(self, col, colour):
      row = 0
      while row < 5 and self.board[row][col] == 0:
          if self.board[row][col] == 0 and self.board[row + 1][col] == 0:
              row += 1
          else:
              break
      self.board[row][col] = colour
      return row