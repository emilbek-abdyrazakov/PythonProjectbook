"""def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)"""


def animals (breed, type, color=''):
    if color:
        animal_name = f"{breed}, {color}, {type}"
    else:
        animal_name = f"{breed}, {type}"
    return len(animal_name)


animal = animals('husky', 'dog', 'white')
print(animal)

animal = animals('regular', 'cat')
print(animal)