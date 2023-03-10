def reverseString(s):
    """
    Do not return anything, modify s in-place instead.
    """
    a = []
    s = s.reverse()
    for i in s:
        a.append(i)
    return a


print(reverseString(["h","e","l","l","o"]))