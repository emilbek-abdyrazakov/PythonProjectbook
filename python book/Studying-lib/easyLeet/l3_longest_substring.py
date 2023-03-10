def lengthOfLongestSubstring(s):
    temp = s[:3]
    for i in range(len(s[::-1])-3):
        if temp == s[i+2]:
            return True



print(lengthOfLongestSubstring("abcabcbb"))