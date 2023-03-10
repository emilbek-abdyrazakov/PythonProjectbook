# Given a number n, return True if n is in the range 1..10, inclusive.
# Unless outside_mode is True, in which case return True if
# the number is less or equal to 1, or greater or equal to 10.
# in1to10(5, False) → True
# in1to10(11, False) → False
# in1to10(11, True) → True
# print(in1to10(11, True)) → True

def in1to10(n, outside_mode):
    if (n >=1 and n <=10) and not outside_mode:
        return True
    if outside_mode:
        return True
    if (n<=1 or n>=10) and not outside_mode:
        return False
    return False


print(in1to10(5, False))
print(in1to10(11, False))
print(in1to10(11, True))
print(in1to10(11, True))


    # if 0 < n < 11 and not outside_mode:
    #     return True
    #
    # if 2 > n > 9 and outside_mode:
    #     return True
    # return False
    # if 0 < n < 11 :
    #     return True
    # if 1 > n > 9 and outside_mode:
    #     return True
    # return False



