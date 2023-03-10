def isPowerOfTwo(n):
    while n > 1:
        if n % 2 != 0:
            return False
        n /= 2
    return n == 1



print(isPowerOfTwo(16))
print(isPowerOfTwo(3))
print(isPowerOfTwo(6))
print(isPowerOfTwo(5))
print(isPowerOfTwo(12))
