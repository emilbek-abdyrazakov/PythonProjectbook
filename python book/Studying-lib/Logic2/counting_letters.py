def letter_count(s):
    d = {}
    for i in s:
        d[i] = d.get(i, 0) + 1
    return d


print(letter_count("string is an, immutable object"))
