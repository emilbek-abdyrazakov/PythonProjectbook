favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
language = favorite_languages ['sarah'].title()
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
for name_1 in favorite_languages.keys():
    print(name_1.upper())
print(f"Sarah's favorite language is {language}")
print(".......")
friends=['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
    if 'erin' not in favorite_languages.keys():
        print("Erin, please take our poll")

print(".............")
for language in set(favorite_languages.values()):
    print(language.title())