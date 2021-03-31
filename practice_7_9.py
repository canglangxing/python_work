sandwich_orders = ['pastrami', 'ham', 'potato', 'pastrami', 'ham', 'fride egg', 
    'pastrami']
print("Pastrami has been sold out")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)