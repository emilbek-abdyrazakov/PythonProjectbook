def majorityElement(nums):
    abc = {}
    result = 0
    biggestValue = 0
    for i in nums:
        abc[i] = abc.get(i, 0) + 1
    for x in abc:
        if biggestValue < abc.get(x):
            biggestValue = abc.get(x)
            result = x
    return result


print(majorityElement([3, 2, 3, 7, 1, 7, 1, 7]))
print(majorityElement([2, 2, 1, 1, 1, 2, 2]))
