def convert(s, numRows):
    if numRows == 1:
        return s
    lst = [""] * numRows
    counter = 0
    flag = False
    for x in range(len(s)):
        if counter+1 == numRows:
            flag = True
        lst[counter] += s[x]
        if flag:
            counter -= 1
            if counter == 0:
                flag = False
        else:
            counter += 1
    return "".join(lst)


print(convert("PAYPALISHIRING", 3))
# print(convert("PAYPALISHIRING", 4))
# print(convert("ABC", 1))
