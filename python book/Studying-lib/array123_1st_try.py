# Given an array of ints, return True if the sequence of numbers
# 1, 2, 3 appears in the array somewhere.
# array123([1, 1, 2, 3, 1]) → True
# array123([1, 1, 2, 4, 1]) → False
# array123([1, 1, 2, 1, 2, 3]) → True


def array123(nums):
    result = ""
    for i in nums:
        result = result + str(i)
        if len(result) == 2 and not result == "12":
            result = str(i)
        elif len(result) == 3 and not result == "123":
            result = str(i)
        if result == "123":
            return True
    return False


print(array123([7, 3, 5, 6, 1, 2, 3]))
# print(array123([1, 1, 2, 3, 1]))
# print(array123([1, 1, 2, 4, 1]))
# print(array123([1, 1, 2, 1, 2, 3]))
