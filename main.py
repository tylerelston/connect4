import pygame, game

pygame.init()
game = game.Game()

font = pygame.font.SysFont('Comic Sans MS', 40)
size = width, height = 800, 575
speed = [2, 2]
black = 0, 0, 0
grey = 100, 120, 140
red = 255, 0, 0
blue = 0, 0, 255
white = 255, 255, 255


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
  game.board = [[0 for num in range(7)] for row in range(6)]
  displayBoard(screen, game.board)



game.placePiece(0, "R")
game.placePiece(1, "R")
game.placePiece(2, "R")
game.placePiece(3, "R")
displayBoard(screen, game.board)

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
  displayBoard(screen, game.board)
  mouse = pygame.mouse.get_pos() 

  for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pass
      if event.type == pygame.MOUSEBUTTONDOWN:
        # reset button
          if resetX <= mouse[0] <= resetX+resetWidth and resetY <= mouse[1] <= resetY+resetHeight:
            resetGame()

  ## drawing

  # reset
  resetButton = pygame.draw.rect(screen, white, (resetX, resetY, resetWidth, resetHeight))
  text('Reset', screen, resetX+resetWidth/2, resetY+resetHeight/2)

  pygame.display.flip()
