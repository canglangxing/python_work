pizzas = ['alex','bella','carlo']
friends_pizzas = pizzas[:]

pizzas.append('diablo')
friends_pizzas.append('eve')

print("My favorite pizzas are:")
for pizza in pizzas:
	print(pizza)

print("My friend's favorite pizzas are")
for friends_pizza in friends_pizzas:
	print(friends_pizza)