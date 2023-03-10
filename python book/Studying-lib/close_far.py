# Given three ints, a b c, return True if one of b or c is "close"
# (differing from a by at most 1), while the other is "far", differing
# from both other values by 2 or more. Note: abs(num) computes the
# absolute value of a number.
# `close_far(-1, 10, 0) → True`
def close_far(a, b, c):
    resc = b - c
    resc = abs(resc)

    resa = a - b
    resa = abs(resa)

    resb = a - c
    resb = abs(resb)
    c1 = c - b
    b1 = b - a
    a1 = a - c
    c1 = abs(c1)
    b1 = abs(b1)
    a1 = abs(a1)
    if resa <= 1 and c1 >= 3:
        return True
    elif resb <= 1 and c1 >=3:
        return True
    elif resc <= 1 and b1 >= 3:
        return True
    return False
    # if resa <= 1 or resb <= 1 or resc <= 1:
    #     c1 = c - b
    #     b1 = b - a
    #     if abs(c1) >= 2 or abs(b1) >= 2:

    #         return True
    # return False

print(close_far(4, 1, 3))
# print(close_far(10, 8, 9))
# print(close_far(10, 10, 8))
# print(close_far(-1, 10, 0))
