# Given an integer array nums and an integer val, remove all occurrences
# of val in nums in-place. The relative order of the elements may be changed.
def removeElement(nums, val):
    size = len(nums)
    i = 0
    while i < size:
        if nums[i] == val:
            del nums[i]
            size -= 1
        else:
            i += 1
    return len(nums)


print(removeElement([3, 2, 2, 3], 3))
