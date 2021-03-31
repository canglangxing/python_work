print("Please enter two numbers, and I'll add them.")
first_number = input("\nFirst number: ")
second_number = input("Second number: ")
try:
    answer = int(first_number) + int(second_number)
except ValueError:
    print("Please enter numbers!")
else:
    print(answer)