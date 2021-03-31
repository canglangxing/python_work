favorite_places = {
    'john': ['Chengdu'],
    'mary': ['Beijing', 'paris'],
    'henry': ['london', 'berlin', 'roma']
}

for name, cities in favorite_places.items():
    if len(cities) == 1:
        print(f"\n{name.title()}'s favorite place is:")
    else:
        print(f"\n{name.title()}'s favorite places are:")

    for city in cities:
        print(f"\t{city.title()}")