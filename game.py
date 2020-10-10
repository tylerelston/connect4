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