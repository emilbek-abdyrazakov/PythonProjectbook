def mixed(a, b):
    temp = ""
    if len(b) < len(a):
        c = b
    if (len(b)) > len(a):
        c = a
    for i in range(len(c)):
        temp = temp + b[i] + a[i]
    return temp

print(mixed("bishkek", "osh"))
print(mixed("osh", "bishkek"))
