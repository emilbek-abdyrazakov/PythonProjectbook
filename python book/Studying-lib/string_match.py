# Given 2 strings, a and b, return the number of the positions
# where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since
# the "xx", "aa", and "az" substrings appear in the same place in both strings.
# string_match('xxcaazz', 'xxbaaz') → 3
# string_match('abc', 'abc') → 2
# string_match('abc', 'axc') → 0


def string_match(a, b):
    smaller = min(a, b)
    counter = 0
    for i in range(len(smaller) - 1):
        if a[i] == b[i] and a[i + 1] == b[i + 1]:
            counter += 1
    return counter


print(string_match('xxcaazz', 'xxbaaz'))
print(string_match('abcdasfdas', 'abc'))
print(string_match('abc', 'axcdsafas'))
print(string_match('hello', 'he'))
print(string_match('he', 'hello'))
print(string_match('h', 'hello'))
print(string_match('', 'hello'))
