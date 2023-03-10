# Return True if the given string contains an appearance of "xyz" where the
# xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz"
# does not.
# xyz_there('abcxyz') → True
# xyz_there('abc.xyz') → False
# xyz_there('xyz.abc') → True
def xyz_there(str):
    for i in range(len(str)-2):
        if str[i] == 'x' and str[i+1] == 'y' and str[i+2] == 'z':
            if str[i-1] != '.':
                return True
    return False


print(xyz_there('abcxyz'))
print(xyz_there('abc.xyz'))
print(xyz_there('xyz.abc'))
