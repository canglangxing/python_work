favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

names = ['eric', 'john', 'edward', 'joe', 'sarah']
for name in names:
    if name in favorite_languages.keys():
        print(f"{name.title()}, thank you for taking the poll.")
    else:
        print(f"{name.title()}, please take our poll!")