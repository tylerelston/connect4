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
    evaluateState(board)


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

placePiece(board, 0, "R")
placePiece(board, 1, "R")
placePiece(board, 2, "R")
placePiece(board, 3, "R")
pygame.display.update()

displayBoard(screen, board)
while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pass

    #screen.fill(black)
    pygame.display.flip()
