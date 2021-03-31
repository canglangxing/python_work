cars = ['audi','bmw','subaru','toyota ']
# cars.sort(reverse=True)
# print("Here is original list:")
# print(cars)

# print("\nHere is the sorted list:")
# print(sorted(cars,reverse=True))

# print("\nHere is the original list again:")
# print(cars)

# cars.reverse()
# print(cars)

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())