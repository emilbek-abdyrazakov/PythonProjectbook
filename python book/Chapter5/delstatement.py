users = {
    'alan': 'tester',
    'john': 'developer',
    'matt': 'production',
     }
for user, position in users.items():
    print(f"{user.title()} is a {position}")
del users['alan']
print(users)
users['amy'] = 'developer'
for user, position in users.items():
    print(f"{user.title()} is a {position}")