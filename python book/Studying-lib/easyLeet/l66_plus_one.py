# Output: [1,2,4]
def plusOne(digits):
    s = [str(i) for i in digits]
    res = int("".join(s))
    res = res + 1
    res = str(res)
    res = map(int, res)
    res = list(res)
    return res


print(plusOne([1, 2, 3]))
print(plusOne([4, 3, 2, 1]))
print(plusOne([9]))
