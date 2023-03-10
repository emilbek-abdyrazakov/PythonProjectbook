def rearrangeCharacters(s, target):

    target_dict = {}
    for i in target:
        target_dict[i] = target_dict.get(i, 0) + 1
    s_dict = {}
    for x in s:
        if x in target_dict:
            s_dict[x] = s_dict.get(x, 0) + 1
    result = []
    for i in target_dict:
        if i not in s_dict:
            return 0
        result.append(s_dict.get(i) // target_dict.get(i))
    return min(result)


print(rearrangeCharacters("ilovecodingonleetcode", "code"))
print(rearrangeCharacters("abbaccaddaeea", "aaaaa"))
print(rearrangeCharacters("abc", "abcd"))

# target_set = set(target)
# tmp_list = []
# for key in target_set:
#     if s.count(key) == 0:
#         return 0
#     else:
#         tmp_list.append(s.count(key) // target.count(key))
# return min(tmp_list)