def findDifference(nums1, nums2):
    # first = set(nums1)
    # second = set(nums2)
    # return [list(first - second), list(second - first)]
    res1 = []
    [res1.append(x) for x in nums1 if x not in res1]
    res2 = []
    [res2.append(x) for x in nums2 if x not in res2]
    temp = []
    for x in res1:
        if x in res2:
            res2.remove(int(x))
            temp.append(x)
    for x in temp:
        if x in res1:
            res1.remove(int(x))
    return res1, res2


print(findDifference([1, 2, 3], [2, 4, 6]))
print(findDifference([1, 2, 3, 3], [1, 1, 2, 2]))
# print(findDifference([-17, 85, -42, -71], [-59, 3, 55, 51, 97, 63, -45]))
