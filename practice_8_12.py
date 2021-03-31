def sandwich(*toppings):
    print("\nMaking a sandwich with following toppings:")
    for topping in toppings:
        print(f"- {topping}")

sandwich('egg')
sandwich('sausage', 'chicken','bacon')
sandwich('beef', 'tomato')