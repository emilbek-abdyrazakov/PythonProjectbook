def searchInsert(nums, target):
    # for i in range(len(nums)):
    #     if nums[i] == target:
    #         return i
    nums.append(target)
    nums = sorted(nums)
    for x in range(len(nums)):
        if nums[x] == target:
            return x


print(searchInsert([1,3,5,6], 2))
print(searchInsert([1,3,5,6], 5))
print(searchInsert([1,3,5,6], 7))