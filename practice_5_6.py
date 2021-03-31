age = 2
if age < 2:
    generation = 'baby'
elif age < 4:
    generation = 'toddler'
elif age < 13:
    generation = 'child'
elif age < 20:
    generation = 'teenager'
elif age < 65:
    generation = 'adult'
else:
    generation = 'the aged'

print(f"This peoplo is one of {generation}.")