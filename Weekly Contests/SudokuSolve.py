# psuedo algo
# traverse each row
# traverse each column
# check for the 3*3 sqaure rules
# Pramp Challenge

def sudoku_solve(board):
    cFlag = False
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == ".":
                for val in range(1, 10):
                    board[i][j] = str(val)
                    cFlag = validate_board(i, j, board)
                    #need to iplement recursive instead of iterative

    return


def validate_board(i, j, board):
    # validating the row entry for newly modified
    hashRow = {}
    for x in range(len(board)):
        if board[x][j] != ".":
            try:
                hashRow[board[x][j]] = 1
            except:
                return False
    # validating the column entry for newly modified
    hashCol = {}
    for y in range(len(board[0])):
        if board[i][y] != ".":
            try:
                hashRow[board[i][y]] = 1
            except:
                return False
    # validating the 3*3 board
    hashBox = {}
    boxX = i / 3
    boxY = j / 3
    for x in range(3):
        for y in range(3):
            xCor = x + 3 * boxX
            yCor = y + 3 * boxY
            if board[xCor][yCor] != ".":
                try:
                    hashBox[board[xCor][yCor]] = 1
                except:
                    return False
    # everything passes
    return True