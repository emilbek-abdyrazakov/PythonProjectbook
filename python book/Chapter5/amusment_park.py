age = 16
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age >= 65:
    price = 10
elif age < 65:
    price = 40
print(f"Your admission cost is ${price}.")