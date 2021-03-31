import json

filename = 'favorite_number.json'
with open(filename) as f:
    favorite_number = json.load(f)
    print(f"I konw your favorite number! It's {favorite_number}.")