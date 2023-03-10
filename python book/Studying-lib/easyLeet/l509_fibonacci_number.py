def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    f = 0
    s = 1
    for x in range(n):
        next = f + s
        f = s
        s = next

    return f
# print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
