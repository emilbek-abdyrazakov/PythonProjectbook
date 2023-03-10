def twoSum(nums, target):
    lis = [0, 0]
    for i in range(len(nums) - 1):
        for x in reversed(range(i + 1, len(nums))):
            if nums[i] + nums[x] == target:
                return [i, x]
    return lis


print(twoSum([2, 8, 11, 15, 3, 6], 9))
