# Driver is eligible to drive if older than 18 and
# not drunk
# driver(20, False) >> True
# driver(15, True) >> False
# driver(30, True) >> False
# driver(28, False) >> True
# driver(10, False) >> False

def driver(age, is_drunk):
    if age >= 18 and not is_drunk:
        return True
    return False


print(driver(20, False))
print(driver(15, True))
print(driver(30, True))
print(driver(28, False))
print(driver(10, False))