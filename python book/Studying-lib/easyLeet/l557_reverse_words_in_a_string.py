def reverseWords(s):
    res= ""
    s = s[::-1]
    reversed = s.split(" ")
    reversed.reverse()
    for i in reversed:
        res += i + " "
    return res.strip()
    # # # for i in s:
    # res = ""
    # res1 = ""
    # for i in s:
    #     if i == " ":
    #         res1 += res
    #         res = ""
    #     res = i + res
    # res1 = res1 + " " + res
    # print(res1.strip())


# print(reverseWords("God Ding"))
print(reverseWords("Let's take LeetCode contest"))