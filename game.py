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
                  print("Win:", colour)
                  return True

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
              print("Win:", colour)
              return True

      # check for diagonal win

      return False

  # place piece
  def placePiece(self, col, colour):
      print('PLACING')
      row = 0
      while row < 5 and self.board[row][col] == 0:
          if self.board[row][col] == 0 and self.board[row + 1][col] == 0:
              row += 1
          else:
              break
      self.board[row][col] = colour