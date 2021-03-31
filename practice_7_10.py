places = {}

place_active = True

while place_active:
    name = input("\nWhat is your name? ")
    place = input("If you could visit one place in the world, where would you go? ")

    places[name] = place

    repeat = input("would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        place_active = False

print("\nResults")
for name, place in places.items():
    print(f"{name} would like to visit {place}.")