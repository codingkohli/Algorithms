"""
A program to generate all the steps taken by a knight to cover the board
"""

class Board:
    def __init__(self,n):
        self.board = [[-1]*n for i in range(n)]

    def generateTour(self,visitMat,steps,xPtr,yPtr,n):
        #print(steps)
        dirn = [(-2, -1), (2, -1), (-2, 1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]
        if steps == n*n:
            return True
        for xAdd,yAdd in dirn:
            xNew = xPtr + xAdd
            yNew = yPtr + yAdd
            if xNew >= 0 and xNew < n and yNew >= 0 and yNew < n and visitMat[xNew][yNew] == -1:
                visitMat[xNew][yNew] = steps

                if Board.generateTour(self,visitMat,steps + 1,xNew,yNew,n):
                    return True
                else:
                    visitMat[xNew][yNew] = -1
        return False


if __name__ == '__main__':
    boardSize = 8
    chessBoard = Board(boardSize)
    chessBoard.board[0][0] = 0
    steps = 1
    if chessBoard.generateTour(chessBoard.board,steps,0,0,boardSize):
        for row in chessBoard.board:
            print(row)
    else:
        print("Cannot genarate solution")






