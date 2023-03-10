import collections
def isValidSudoku(board):
    cols = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    squares = collections.defaultdict(set)

    for r in range(9):
        for c in range(9):
            key = board[r][c]
            if key == ".":
                continue
            if (key in rows[r] or key in cols[c] or key in squares[(r // 3, c // 3)]):
                return False

            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            squares[(r // 3, c // 3)].add(board[r][c])
        print("=====")
        print(cols)
        print(rows)
        print(squares)

    return True
    # a = 0
    # b = 3
    #
    # while a < 9:
    #     if b > 9:
    #         b = 3
    #         a += 3
    #     s = set()
    #     for x in range(a - 3, a):
    #         for i in range(b - 3, b):
    #             if board[x][i] != ".":
    #                 if board[x][i] in s:
    #                     return False
    #                 s.add(board[x][i])
    #     b += 3
    #
    # for x in range(len(board)):
    #     h_set = set()
    #     v_set = set()
    #     for i in range(len(board[x])):
    #         if board[x][i] != ".":
    #             if board[x][i] in h_set:
    #                 return False
    #             h_set.add(board[x][i])
    #         if board[i][x] != ".":
    #             if board[i][x] in v_set:
    #                 return False
    #             v_set.add(board[i][x])
    # return True






# print(isValidSudoku([["5","3","a1","a2","7","a3","a4","a5","a6"]
#                     ,["6","b1","b2","1","9","5","b3","b4","b5"]
#                     ,["c1","9","8","c2","c3","c4","c5","6","c6"]
#                     ,["8","d1","d2","d3","6","d4","d5","d6","3"]
#                     ,["4","e1","e2","8","e3","3","e4","e5","1"]
#                     ,["7","f1","f2","f3","2","f4","f5","f6","6"]
#                     ,["g1","6","g2","g3","g4","g5","2","8","g6"]
#                     ,["h1","h2","h3","4","1","9","h4","h5","5"]
#                     ,["z1","z2","z3","z4","8","z5","z6","7","9"]]))



print(isValidSudoku([["5","3",".",".","7",".",".",".","."]
                    ,["6",".",".","1","9","5",".",".","."]
                    ,[".","9","8",".",".",".",".","6","."]
                    ,["8",".",".",".","6",".",".",".","3"]
                    ,["4",".",".","8",".","3",".",".","1"]
                    ,["7",".",".",".","2",".",".",".","6"]
                    ,[".","6",".",".",".",".","2","8","."]
                    ,[".",".",".","4","1","9",".",".","5"]
                    ,[".",".",".",".","8",".",".","7","9"]]))