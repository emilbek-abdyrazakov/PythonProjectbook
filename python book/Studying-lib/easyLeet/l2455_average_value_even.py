# Output: 9
def averageValue(nums):
    average = []
    for i in nums:
        if i % 6 == 0:
            average.append(i)
    if len(average) == 0:
        return 0
    result = sum(average) // len(average)
    return result


print(averageValue([1,3,6,10,12,15]))
print(averageValue([1,2,4,7,10]))