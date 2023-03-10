def singleNumber(nums):
    print(((sum(list(set(nums)))) * 2) - sum(nums))
    # return sum(list(set(nums)) * 2) - sum(nums)


print(singleNumber([2,2,1]))
