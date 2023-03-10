def hence(a):
    res = 0
    for i in range(1, a + 1):
        res += i
    return res


print(hence(1000000))
