# Output: [[1,0,0],[0,1,0],[1,1,1]]
def flipAndInvertImage(image):
    abba = []
    for x in image:
        x.reverse()
        abba.append(x)
    for i in abba:
        for x in range(len(i)):
            if i[x] == 0:
                i[x] = 1
            elif i[x] == 1:
                i[x] = 0
    return abba


print(flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
