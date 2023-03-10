def intersection(nums1, nums2):
    a = set(nums1)
    b = set(nums2)
    res = []
    for i in a:
        if i in b:
            res.append(i)
    return res


print(intersection([1, 2, 2, 1], [2, 2]))
print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))
