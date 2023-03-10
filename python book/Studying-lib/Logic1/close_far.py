# Given three ints, a b c, return True if one of b or c is
# "close" (differing from a by at most 1), while the other
# is "far", differing from both other values by 2 or more.
# Note: abs(num) computes the absolute value of a number.
# close_far(1, 2, 10) → True
# close_far(1, 2, 3) → False
# close_far(4, 1, 3) → True
# close_far(10, 10, 8) → True

def close_far(a, b, c):
    ab = a - b
    ab = abs(ab)
    ac = a - c
    ac = abs(ac)
    bc = b - c
    bc = abs(bc)
    if ab <= 1:
        if bc > 1 and ac > 1:
            return True
    elif ac <= 1:
        if ab > 1 and bc > 1:
            return True
    return False


# print(close_far(1, 2, 10))
# print(close_far(1, 2, 3))
# print(close_far(4, 1, 3))
# print(close_far(4, 5, 3))
print(close_far(10, 10, 8))