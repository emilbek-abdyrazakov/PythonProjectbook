def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

names = ['hannah', 'tom', 'margot']
greet_users(names)

