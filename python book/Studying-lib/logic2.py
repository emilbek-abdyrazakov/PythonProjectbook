# Given three ints, a b c, return True if one of b or c
# is "close" (differing from a by at most 1), while the
# other is "far", differing from both other values by
# 2 or more. Note: abs(num) computes the absolute value
# of a number.
# close_far(1, 2, 10) → True
# close_far(1, 2, 3) → False
# close_far(4, 1, 3) → True

def close_far(a, b, c):
    diff1 = abs(a - b)
    diff2 = abs(a - c)

    return (diff1 == 1 and diff2 >= 2) or (diff2 == 1 and diff1 >= 2)

    # if a - b == 1 or a - b == -1:
    #     if b - c >= 2 or b - c <= -2:
    #         return True
    #if a - c == 1 or a - c == 1:
    #    if c - b >= 2 or c - b <= -2:
    #        return True
    #elif a - b == 1 or a - b == -1:
    #    if b - c >= 2 or b - c <= -2:
    #        return True
    #return False


print(close_far(1, 2, 10))
print(close_far(1, 2, 3))
# print(close_far(4, 5, 3))