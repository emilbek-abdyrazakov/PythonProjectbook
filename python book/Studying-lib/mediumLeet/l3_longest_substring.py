def lengthOfLongestSubstring(s):
    result = 0
    for i in range(len(s)):
        if result > (len(s) - i):
            break
        uniq = set()
        for x in range(i, len(s)):
            if s[x] in uniq:
                break
            text = s[i:x+1]
            uniq.add(s[x])
            if result < len(text):
                result = len(text)
    return result


print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring("bbbbbb"))

# city = set()
# city.add("Bishkek")
# city.add("Chicago")
# city.add("New York")
# city.add("Bishkek")
# print(city)
