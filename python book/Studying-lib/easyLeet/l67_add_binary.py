def addBinary(a, b):
    sum = bin(int(a, 2) + int(b, 2))
    sum = sum[2:]
    return sum


print(addBinary('11', '1')) #answer '100'
print(addBinary('1010', '1011')) #answer '10101'