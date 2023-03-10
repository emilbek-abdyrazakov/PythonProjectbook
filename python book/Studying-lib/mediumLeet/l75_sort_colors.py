def sortColors(nums):
    red = 0
    white = 0
    blue = 0
    for i in nums:
        if i == 0:
            red += 1
        elif i == 1:
            white += 1
        elif i == 2:
            blue += 1
    for i in range(len(nums)):
        if red > 0:
            nums[i] = 0
            red -= 1
        elif white > 0:
            nums[i] = 1
            white -= 1
        elif blue > 0:
            nums[i] = 2
            blue -= 1
    print(nums)


print(sortColors([2, 0, 2, 1, 1, 0]))
print(sortColors([2, 0, 1]))
