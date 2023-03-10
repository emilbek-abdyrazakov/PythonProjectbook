def reverse1(message):
    temp =''
    for i in message:
        temp = i + temp
    return temp


print(reverse1("Bishkek"))

print(reverse1("Hello world"))