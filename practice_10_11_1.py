import json

usernumber = input("Please enter your favorite number: ")
filename = 'favorite_number.json'
with open(filename, 'w') as f:
    json.dump(usernumber,f)