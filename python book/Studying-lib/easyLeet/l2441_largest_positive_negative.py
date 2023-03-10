# solution 3
def findMaxK(nums):
    result = -1
    so = sorted(nums)
    d = set()
    for i in so:
        if i > 0:
            d.add(i)
    for i in so:
        if -i in d:
            return -i
    return result


# print(findMaxK([-1, 2, -3, 3]))
print(findMaxK([67, 76, -10, 2, -3, 3, -67]))
