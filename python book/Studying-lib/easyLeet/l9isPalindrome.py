def isPalindrome(x):
    original = str(x)
    # rev = original[::-1]
    # if original == rev:
    #     return True
    # return False
    temp = ""
    for i in range(len(original)):
        temp = original[i] + temp
    print(temp)
    print(original)
    if temp == original:
        return True
    return False


print(isPalindrome(-121))
