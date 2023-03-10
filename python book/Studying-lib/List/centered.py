# Return the "centered" average of an array of ints, which we ll
# say is the mean average of the values, except ignoring the largest
# and smallest values in the array. If there are multiple copies of
# the smallest value, ignore just one copy, and likewise for the largest
# value. Use int division to produce the final average. You may assume
# that the array is length 3 or more.
#
# centered_average([1, 2, 3, 4, 100]) → 3
# centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
# centered_average([-10, -4, -2, -4, -2, 0]) → -3

def centered_average(nums):
    # a = set()
    # for i in nums:
    #     a.add(i)
    # a = sorted(a)
    # res = 0
    # for i in range(1,len(a)-1):
    #     res += a[i]
    # res = res // (len(a) -2)
    # return res
    res = 0
    sort = sorted(nums)
    div = len(nums) - 2
    for i in range(1, len(sort) - 1):
        res += sort[i]
    res = res // div
    return res




print(centered_average([1, 2, 3, 4, 100]))
# print(centered_average([1, 1, 5, 5, 10, 8, 7]))


