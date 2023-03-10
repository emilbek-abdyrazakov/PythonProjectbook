# [["5","3","4","6","7","8","9","1","2"],
#  ["6","7","2","1","9","5","3","4","8"],
#  ["1","9","8","3","4","2","5","6","7"],
#  ["8","5","9","7","6","1","4","2","3"],
#  ["4","2","6","8","5","3","7","9","1"],
#  ["7","1","3","9","2","4","8","5","6"],
#  ["9","6","1","5","3","7","2","8","4"],
#  ["2","8","7","4","1","9","6","3","5"],
#  ["3","4","5","2","8","6","1","7","9"]]



def solveSudoku(board):
    # hor = []
    # ver = []
    # for x in range(9):
    #     for i in range(9):
    #         hor.append(board[x][i])
    #         ver.append(board[i][x])
    # print(hor)
    # print(ver)
    yRange = 3
    xRange = 0
    forX = 0
    block = []
    xAxis = set()
    yAxis = set()
    while forX < len(board):
        for y in range(yRange - 3, yRange):
            block.append(board[forX][y])
            if len(yAxis) < 3:
                yAxis.add(y)
        xAxis.add(forX)
        if forX == 8 and forX > yRange:
            yRange += 3
            forX = -1
        xRange += 1
        if xRange == 3:
            findingNumber(xAxis, yAxis, block, board)
            print("x" + str(xAxis))
            print("y" + str(yAxis))
            print(block)
            block = []
            xAxis = set()
            yAxis = set()
            xRange = 0
        forX += 1


def findingNumber(xAxis, yAxis, block, board):

    pass


print(solveSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."],
                   ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                   [".", "9", "8", ".", ".", ".", ".", "6", "."],
                   ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                   ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                   ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                   [".", "6", ".", ".", ".", ".", "2", "8", "."],
                   [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                   [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
