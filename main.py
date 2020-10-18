import pygame, game, player, random

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
  return random.choice(turns)


displayBoard(screen, game.board)

pygame.display.update()

#board = resetGame()
pygame.display.update()

# reset
resetX = 100
resetY = 310
resetWidth = 100
resetHeight = 50

# currentTurn
turns = ["Player", "Computer"]
currentTurn = random.choice(turns)
currentTurnX = 150
currentTurnY = 280

# win
win = "Winner: "
winX = 150
winY = 450

pygame.display.update()

# https://stackoverflow.com/questions/18839039/how-to-wait-some-time-in-pygame
delay = 0

while 1:
  tick = pygame.time.get_ticks()
  screen.fill(grey)
  displayBoard(screen, game.board)
  mouse = pygame.mouse.get_pos() 

  # check for win
  state = game.evaluateState()
  if (state != 0):
    text(win + state, screen, winX, winY)

  if state == 0 and currentTurn == "Computer" and delay < tick:
    #game.placePiece(player.randomMove(game.board), "B")
    game.placePiece(player.playGreedy(game.board, "B"), "B")
    currentTurn = "Player"

  for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pass
      if event.type == pygame.MOUSEBUTTONDOWN:
        # reset button
          if resetX <= mouse[0] <= resetX+resetWidth and resetY <= mouse[1] <= resetY+resetHeight:
            currentTurn = resetGame()
        # no winner yet
          if state == 0:
          # player move
            if currentTurn == "Player":
              # col 0
              if 15 <= mouse[0] <= 15+30 and 15 <= mouse[1] <= 250:
                game.placePiece(0, "R")
                currentTurn = "Computer"
              # col 1
              if 55 <= mouse[0] <= 55+30 and 15 <= mouse[1] <= 250:
                game.board, "R", game.placePiece(1, "R")
                currentTurn = "Computer"
              # col 2
              if 95 <= mouse[0] <= 95+30 and 15 <= mouse[1] <= 250:
                game.board, "R", game.placePiece(2, "R")
                currentTurn = "Computer"
              # col 3
              if 135 <= mouse[0] <= 135+30 and 15 <= mouse[1] <= 250:
                game.board, "R", game.placePiece(3, "R")
                currentTurn = "Computer"
              # col 4
              if 175 <= mouse[0] <= 175+30 and 15 <= mouse[1] <= 250:
                game.placePiece(4, "R")
                currentTurn = "Computer"
              # col 5
              if 205 <= mouse[0] <= 205+30 and 15 <= mouse[1] <= 250:
                game.placePiece(5, "R")
                currentTurn = "Computer"
              # col 6
              if 245 <= mouse[0] <= 245+30 and 15 <= mouse[1] <= 250:
                game.board, "R", game.placePiece(6, "R")
                currentTurn = "Computer"
            delay = tick + 1000

  ## drawing

  # reset
  resetButton = pygame.draw.rect(screen, white, (resetX, resetY, resetWidth, resetHeight))
  text('Reset', screen, resetX+resetWidth/2, resetY+resetHeight/2)

  # currentMove
  text('Current Move: ' + currentTurn, screen, currentTurnX,currentTurnY)

  pygame.display.flip()
