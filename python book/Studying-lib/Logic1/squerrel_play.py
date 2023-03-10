# The squirrels in Palo Alto spend most of the day playing. In particular,
# they play if the temperature is between 60 and 90 (inclusive). Unless
# it is summer, then the upper limit is 100 instead of 90. Given an int
# temperature and a boolean is_summer, return True if the squirrels play
# and False otherwise.
# squirrel_play(70, False) → True
# squirrel_play(95, False) → False
# squirrel_play(95, True) → True

def squirrel_play(temp, is_summer):
    # if 59 < temp < 91 and not is_summer or 59 < temp < 101 and is_summer:
    if (temp > 59 and temp < 91) and not is_summer:
        return True
    if (temp > 59 and temp < 101) and is_summer:
        return True
    return False


print(squirrel_play(70, False))
print(squirrel_play(95, False))
print(squirrel_play(95, True))
