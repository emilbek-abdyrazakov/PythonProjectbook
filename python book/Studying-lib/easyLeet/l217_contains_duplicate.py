#true
#false
def containsDuplicate(nums):
    nums = sorted(nums)
    for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
    return False


print(containsDuplicate([1,2,3,1]))
print(containsDuplicate([1,2,3,4]))