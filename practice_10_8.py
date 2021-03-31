filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    print(filename)
    try:
        with open(filename) as file_object:
            print(file_object.read())
    except FileNotFoundError:
        print("Sorry, we can't found the file.")