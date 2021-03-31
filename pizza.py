# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushroom', 'extra cheese'],
# }

# print(f"You order a {pizza['crust']}-crust pizza with the following toppings:")

# for topping in pizza['toppings']:
#     print("\t" + topping)

def make_pizza(size, *toppings):
    # """打印顾客点的所有配料"""
    # print(toppings)

    """概述要制作的比萨"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')