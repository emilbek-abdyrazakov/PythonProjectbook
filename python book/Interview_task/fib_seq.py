# from functools import lru_cache
# @lru_cache(maxsize=1000)
# def fib2(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     elif n > 2:
#         return fib2(n-1) + fib2(n-2)
#
# for i in range(1,501):
#     print(fib2(i))

# def fibanacci(n):
#     print('++++++++++')
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     elif n > 2:
#          return fibanacci(n-1) + fibanacci(n-2)
#
# # print(fibanacci(10))
#
def fib1(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    elif n == 2:
        return 1
    a = 1
    b = 1
    res = 0
    for i in range(n-2):
        res = a + b
        a = b
        b = res
    return res

print(fib1(500))
print(fib1(10))
#
