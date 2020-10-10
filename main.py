import pygame

pygame.init()
font = pygame.font.SysFont('Comic Sans MS', 40)
size = width, height = 800, 575
speed = [2, 2]
black = 0, 0, 0
grey = 100, 120, 140
red = 255, 0, 0
blue = 0, 0, 255
white = 255, 255, 255

board = [[0 for num in range(7)] for row in range(6)]

screen = pygame.display.set_mode(size)

# https://www.geeksforgeeks.org/python-display-text-to-pygame-window/
def text(text, screen, x, y):
  text = font.render(text, True, black)
  textRect = text.get_rect()
  textRect.center = (x,y)
  screen.blit(text, textRect)

# display game board
def displayBoard(screen, board):
    pygame.draw.rect(screen, grey, (10, 10, 560, 560))
    colour = white
    x = 15
    y = 15
    for row in board:
        for tile in row:
            if tile == "B":
                colour = blue
            if tile == "R":
                colour = red
            pygame.draw.rect(screen, colour, (x, y, 30, 30))
            x += 40
            colour = white
        x = 15
        y += 40

def resetGame():
  screen.fill(grey)
  board = [[0 for num in range(7)] for row in range(6)]
  displayBoard(screen, board)
  return board

# place piece
def placePiece(board, col, colour):
    print('PLACING')
    row = 0
    while row < 5 and board[row][col] == 0:
        if board[row][col] == 0 and board[row + 1][col] == 0:
            row += 1
        else:
            break
    board[row][col] = colour
    displayBoard(screen, board)
    return evaluateState(board)


# evaluates board for a winning state
def evaluateState(board):
    consecutive = 1
    # check for row win
    for col in range(len(board[0])):
        prevColour = 0
        for row in range(len(board)):
            colour = board[row][col]
            if colour != 0 and prevColour == colour:
                consecutive += 1
            else:
                consecutive = 1
            prevColour = colour

            if consecutive == 4:
                print("Win:", colour)
                return True

    # check for column win
    for row in range(len(board)):
      for col in range(len(board[row])):
        colour = board[row][col]
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

placePiece(board, 0, "R")
placePiece(board, 1, "R")
placePiece(board, 2, "R")
placePiece(board, 3, "R")
pygame.display.update()

#board = resetGame()
pygame.display.update()

resetX = 400
resetY = 25
resetWidth = 100
resetHeight = 50

pygame.display.update()
while 1:
  screen.fill(grey)
  displayBoard(screen, board)
  mouse = pygame.mouse.get_pos() 

  for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pass
      if event.type == pygame.MOUSEBUTTONDOWN:
        # reset button
          if resetX <= mouse[0] <= resetX+resetWidth and resetY <= mouse[1] <= resetY+resetHeight:
            board = resetGame()

  ## drawing

  # reset
  resetButton = pygame.draw.rect(screen, white, (resetX, resetY, resetWidth, resetHeight))
  text('Reset', screen, resetX+resetWidth/2, resetY+resetHeight/2)

  pygame.display.flip()
