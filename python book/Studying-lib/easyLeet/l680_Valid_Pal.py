# Given a string s, return true if the s can be palindrome after
# deleting at most one character from it.
# aba = true
# abca = true
# abc = false

def validPalindrome(s):
    if s == s[::-1]:
        return True
    b = s[::-1]
    for i in range(0, len(s)):
        if s[i] != b[i]:
            temp = s[:i] + s[i + 1:]
            temp1 = b[:i] + b[i + 1:]
            return temp == temp[::-1] or temp1 == temp1[::-1]






# print(validPalindrome("aba"))
# print(validPalindrome("abca"))
print(validPalindrome("abc"))