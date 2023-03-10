# You are a professional robber planning to rob houses along a
# street. Each house has a certain amount of money stashed, the
# only constraint stopping you from robbing each of them is that
# adjacent houses have security systems connected and it will
# automatically contact the police if two adjacent houses were broken
# into on the same night.
# Given an integer array nums representing the amount of money of
# each house, return the maximum amount of money you can rob tonight
# without alerting the police.
# [4,1,2,7,5,3,1] 14

def rob(nums):
    # if nums is []:
    #     return 0
    N = len(nums)
    rob_next_plus_one = 0
    rob_next = nums[N - 1]

    for i in range(N - 2, -1, -1):
        current = max(rob_next, rob_next_plus_one + nums[i])
        # print('===================')
        # print(current)
        # print(rob_next)
        # print(rob_next_plus_one)
        rob_next_plus_one = rob_next

        rob_next = current

    return rob_next


print(rob([10, 3, 3, 9, 15, 8, 4, 8]))
# print(rob([1,2,3,1]))
# print(rob([2,1]))
# print(rob([2,1,1,2]))
# print(rob([1,1,1]))
# print(rob([2,4,2]))
# print(rob([4,4,0,0]))
# # print(rob([4,1,2,7,5,3,1]))
# print(rob([1, 3, 1, 3, 100]))
# print(rob([4, 5, 1, 3, 1, 3, 100, 97]))
# res1 = 0
# res2 = 0
# for i in range(0, len(nums), 2):
#     res1 += nums[i]
# for i in range(1, len(nums), 2):
#     res2 += nums[i]
# res3 = 0
# i = 0
# while i < len(nums)-2:
#     if nums[i] >= nums[i + 1] and nums[i] >= nums[i + 2]:
#         res3 += nums[i]
#         i = i + 2
#     elif nums[i+1] >= nums[i] and nums[i+1] >= nums[i+2]:
#         res3 += nums[i+1]
#         i = i + 3
#     elif nums[i+2] >= nums[i] and nums[i+2] >= nums[i+1]:
#         res3 += nums[i+2]
#         i = i + 4
# if res1 >= res2 and res1 >= res3:
#     return res1
# elif res2 >= res1 and res2 >= res3:
#     return res2
# elif res3 >= res1 and res3 >= res2:
#     return res3
# for i in range(len(nums)-2):
#     if nums[i] > nums[i+1] and nums [i] > nums[i+2]:
#         res3 += nums[i]
#         i = i + 1
#     elif nums[i+1] > nums[i] and nums[i+1] > nums[i+2]:
#         res3 += nums[i+1]
#         i = i + 2
#     elif nums[i+2] > nums[i] and nums[i+2] > nums[i+1]:
#         res3 += nums[i+2]
#         i = i + 3
#
# print(res3)


# if res1 > res2:
#     return res1
# return res2
# res = 0
# for i in range(0, len(nums),2):
#         res += nums[i]
# res1 = 0
# for i in range(1, len(nums),2):
#         res1 += nums[i]
# if res > res1:
#     return res
# return res1
# res = 0
# switch = 0
# for i, x in range(len(nums),2):
#     # if switch == 0:
#         res += nums[i]
#         # switch += 1
#     # else:
#         # switch -= 1
# res1 = 0
# switch1 = 0
# for i in range(1, len(nums),2):
# if switch1 == 0:
#     switch1 += 1
# else:
#     res1 += nums[i]
# switch1 -= 1
# switch2 = 0
# res2 = 0
# for i in range(len(nums)):
#     if switch2 == 0:
#         res2 += nums[i]
#         switch2 += 1
#     elif switch2 == 1:
#         switch2 += 1
#     else:
#         switch2 = 0


# if res1 >= res and res1 >= res2:
#     return res1
# elif res > res1 and res > res2:
#     return res
# return res2
