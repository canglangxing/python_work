prompt = "Please tell me your age: "

# age = ""
# while age != 'quit':
#     age = input(prompt)
#     if age != 'quit':
#         age = int(age)
#         if age < 3:
#             print(f"Your ticket price is free.")
#         elif age <= 12:
#             print(f"Your ticket price is $10.")
#         else:
#             print(f"Your ticket price is $15.")

# active = True
# while active:
#     age = input(prompt)
#     if age == 'quit':
#         active = False
#     else:
#         age = int(age)
#         if age < 3:
#             print(f"Your ticket price is free.")
#         elif age <= 12:
#             print(f"Your ticket price is $10.")
#         else:
#             print(f"Your ticket price is $15.")

while True:
    age = input(prompt)
    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            print(f"Your ticket price is free.")
        elif age <= 12:
            print(f"Your ticket price is $10.")
        else:
            print(f"Your ticket price is $15.")