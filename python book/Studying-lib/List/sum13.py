# Return the sum of the numbers in the array, returning 0 for an empty array.
# Except the number 13 is very unlucky, so it does not count and numbers that
# come immediately after a 13 also do not count.

def sum13(nums):
    # # flag = False
    # counter = 0
    # res = 0
    # for i in range(len(nums)):
    #     if counter > 0:
    #         counter -= 1
    #         # flag = False
    #     elif nums[i] == 13:
    #         counter = 2
    #         # flag = True
    #     else:
    #         res += nums[i]
    # return res

    # res = 0
    # counter = 0
    # for i in range(len(nums)):
    #     if counter > 0:
    #         counter -= 1
    #     elif nums[i] == 13:
    #         counter = 1
    #     else:
    #         res += nums[i]
    # return res
    # res = 0
    # i = 0
    # while i < len(nums):
    #     if nums[i] == 13:
    #         i += 1
    #     else:
    #         res += nums[i]
    #     i += 1
    # return res

    res = 0
    for i in range(len(nums)):
        if nums[i] == 13:
            nums[i+1] = 0
        else:
            res += nums[i]
    return res


print(sum13([1, 13, 5, 1, 10]))
