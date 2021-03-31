while True:
    reason = input("Please tell us why you like coding: ")
    if reason == '':
        break
    else:
        filename = 'reasons.txt'
        with open('reasons.txt', 'a') as file_object:
            file_object.write(f"{reason}\n")