def countAsterisks(s):
    counter = 0
    pipe = 0
    for i in range(len(s)):
        if pipe % 2 == 0 and s[i] != '|':
            if s[i] == '*':
                counter += 1
        if s[i] == '|':
            pipe += 1
    return counter


print(countAsterisks("l|*e*et|c**o|*de|"))
