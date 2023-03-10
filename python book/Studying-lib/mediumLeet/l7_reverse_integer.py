def reverse(x):
    emp = ""
    if x <= -2 ** 31 or x >= 2 ** 31 - 1:
        return 0
    jst = str(x)
    for i in jst:
        if i != '-':
            emp = i + emp
    emp = int(emp)
    if jst[0] == '-':
        emp = emp * -1
    if emp <= -2 ** 31 or emp >= 2 ** 31 - 1:
        return 0
    return emp


print(reverse(123))
print(reverse(-123))
print(reverse(9000))
print(reverse(-1563847412))