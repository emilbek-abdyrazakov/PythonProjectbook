def lengthOfLastWord(s):
    s = s.strip()
    counter = 0
    for i in reversed(s):
        if i == " ":
            return counter
        counter += 1
    return len(s)


print(lengthOfLastWord("Hello World"))
print(lengthOfLastWord("   fly me   to   the moon  "))
print(lengthOfLastWord("a"))
print(lengthOfLastWord("  aaaaaa    "))