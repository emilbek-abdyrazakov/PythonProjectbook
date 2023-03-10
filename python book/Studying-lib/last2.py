
# Given a string, return the count of the number of times that a substring
# length 2 appears in the string and also as the last 2 chars of the string,
# so "hixxxhi" yields 1 (we won't count the end substring).
#
#
# last2('hixxhi') → 1
# last2('xaxxaxaxx') → 1
# last2('axxxaaxx') → 2

def last2(str):
    if len(str) < 4:
        return 0
    counter = 0
    for i in range(len(str)-2):
        if str[len(str)-2:] == (str[i]+str[i+1]):
            counter = counter + 1
    return counter


print(last2('hixxhi'))
print(last2('xaxxaxaxx'))
print(last2('axxxaaxx'))
