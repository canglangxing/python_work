favorite_numbers = {
    'alex': [5, 9, 0],
    'bob': [28, 31, 9],
    'carlos': [7, 16, 72],
    'david': [6, 10, 3],
    'eve': [19, 43, 84, 98],
}

for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(number)