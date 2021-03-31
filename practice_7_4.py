prompt = "Please choose the topping you like:"
prompt += "\n(Please enter 'quit' if you finish selecting.) " 

# message = ""
# while message != 'quit':
#     message = input(prompt)

#     if message != 'quit':
#         print(f"We will add {message} in your pizza.")
#     else:
#         print(message)

# active = True
# while active:
#     message = input(prompt)

#     if message == 'quit':
#         active = False
#     else:
#         print(f"We will add {message} in your pizza.")

while True:
    message = input(prompt)

    if message == 'quit':
        break
    else:
        print(f"We will add {message} in your pizza.")