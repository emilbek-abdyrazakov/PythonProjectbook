def isPalindrome(s):
    palindrome = ""
    for i in s:
        if i.isalnum() == True:
            palindrome = i + palindrome
    return palindrome.lower() == palindrome[::-1].lower()


print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome("0P"))