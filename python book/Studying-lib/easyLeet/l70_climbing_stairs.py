def climbStairs(n):
    temp1 = 0
    temp2 = 1
    result = 0
    i = 0
    while i < n:
        result = temp1 + temp2
        temp1 = temp2
        temp2 = result
        i += 1
    return result
#     res = [0] * (n+1)
#     res[0] = 1
#     res[1] = 1
#     res[2] = 2
#
#     for i in range(3, n + 1):
#         res[i] = res[i - 1] + res[i - 2]
#
#     return res[n]
#
#
print(climbStairs(10))

