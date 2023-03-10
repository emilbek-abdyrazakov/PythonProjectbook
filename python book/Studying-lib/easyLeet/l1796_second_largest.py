import re
def secondHighest(s):
    largest = -1
    secondLargest = -1
    for i in s:
        if i.isdigit():
            number = int(i)
            if largest < number:
                if secondLargest < largest:
                    secondLargest = largest
                largest = number
            elif secondLargest < number != largest:
                secondLargest = number
    return secondLargest


print(secondHighest("dfa12321afd"))