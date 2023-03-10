def rotate(matrix):
    temp = [[0]*len(matrix) for i in range(len(matrix))]
    for x in range(len(matrix)):
        counter = 0
        for y in reversed(range(len(matrix))):
            temp[x][counter] = matrix[y][x]
            counter += 1
    for x in range(len(temp)):
        for y in range(len(temp)):
            matrix[x][y] = temp[x][y]


print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
