# Given two strings ransomNote and magazine, return true if ransomNote
# can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

def canConstruct(ransomNote, magazine):
    if ransomNote in magazine:
        return True
    return False


print(canConstruct("aa","aab"))
print(canConstruct("a", "b"))
print(canConstruct("aab", "baa"))