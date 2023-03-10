# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are
# horizontally or vertically neighboring. The same letter cell may not be used more than once.

def exist(board, word):
    for i in range(len(board)):
        for x in reversed(range(len(board))):

            print(i, x)


print(exist([["A","B","C","E"],
             ["S","F","C","S"],
             ["A","D","E","E"]], "ABCCED"))
# print(exist([["A","B","C","E"],
#              ["S","F","C","S"],
#              ["A","D","E","E"]], "SEE"))
# print(exist([["A","B","C","E"],
#              ["S","F","C","S"],
#              ["A","D","E","E"]], "ABCB"))