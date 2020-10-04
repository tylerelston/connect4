import pygame

pygame.init()

size = width, height = 800, 575
speed = [2, 2]
black = 0, 0, 0
grey = 100, 120, 140
red = 255, 0, 0
blue = 0, 0, 255
white = 255, 255, 255


board = [[0 for num in range(7)] for row in range(6)]


screen = pygame.display.set_mode(size)

# display game board
def display_board(screen, board):
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

display_board(screen, board)
pygame.display.update()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    #screen.fill(black)
    pygame.display.flip()