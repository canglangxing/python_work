print("Please enter two numbers, and I'll add them.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == '':
        break
    second_number = input("Second number: ")
    if second_number == '':
        break

    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("Please enter numbers!")
    else:
        print(answer)