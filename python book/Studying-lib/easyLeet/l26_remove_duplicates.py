def removeDuplicates(nums):
    size = len(nums)
    i = 0
    while i < size - 1:
        if nums[i] == nums[i + 1]:
            size -= 1
            del nums[i]
        else:
            i += 1
    return len(nums)


print(removeDuplicates([1, 1, 2]))
print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
print(removeDuplicates([1, 1, 1]))
