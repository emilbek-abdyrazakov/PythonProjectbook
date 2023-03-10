# sum13([1, 2, 2, 1]) → 6
# sum13([1, 1]) → 2
# sum13([1, 2, 2, 1, 13]) → 6

def sum13(nums):
    sum = 0
    for i in range(len(nums)-1):
        if nums[i] == 13:
            nums[i + 1] = 0
        if nums[i] == 13:
            nums[i] = 0
    print(nums)

#
# print(sum13([1, 2, 2, 1]))
# print(sum13([1, 1]))
print(sum13([1, 2, 2, 1, 13]))
# print(sum13([13, 1, 13]))
# print(sum13([5, 13, 2]))
# print(sum13([13]))
