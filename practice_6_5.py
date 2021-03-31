rivers = {
    'nile': 'egypt',
    'danube': 'germany',
    'seine': 'france',
    }

for river,nation in rivers.items():
    print(f"The {river.title()} runs through {nation.title()}.")

for river in rivers.keys():
    print(river.title())

for nation in rivers.values():
    print(nation.title())