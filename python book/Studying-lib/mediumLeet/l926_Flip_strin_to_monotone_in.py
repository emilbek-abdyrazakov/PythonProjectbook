# A binary string is monotone increasing if it consists of some number of
# 0's (possibly none), followed by some number of 1's (also possibly none).
# You are given a binary string s. You can flip s[i] changing it from 0 to 1
# or from 1 to 0. Return the minimum number of flips to make s monotone
# increasing.
# "0101100011" answer 3
def minFlipsMonoIncr(s):
    # counter = 0
    # for i in range(len(s)-1):
    #     if s[i] == "0" and s[i - 1] == "1":
    #         s[i] += "1"
    #         counter += 1
    #         print(s)
    #     elif s[i] == "0" and s[i + 1 ] != "0":
    #         counter += 1
    # return counter

    one = 0
    ans = 0
    for num in s:
        if num == '1':
            one += 1
        elif one:
            one -= 1
            ans += 1
    return ans


print(minFlipsMonoIncr("00110"))
# print(minFlipsMonoIncr("010110"))
# print(minFlipsMonoIncr("00011000"))
# print(minFlipsMonoIncr("0101100011"))
