while True:
    name = input("Please enter your name: ")
    if name == '':
        break
    else:    
        print(f"Hello, {name}.")

        filename = 'guest_book.txt'
        with open('guest_book.txt', 'a') as file_object:
            file_object.write(f"{name}\n")