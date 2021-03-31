import json

filename = 'favorite_number.json'
try:
    with open(filename) as f:
        favorite_number = json.load(f)
        print(f"I konw your favorite number! It's {favorite_number}.")
except FileNotFoundError:
    favorite_number = input("Please enter your favorite number: ")
    with open(filename, 'w') as f:
        json.dump(favorite_number,f)