inventory = {
    "Laptop": 5,
    "Mouse": 20,
    "Keyboard": 10,
    "Monitor": 7,
    "Mobile": 15,
    "Airpods": 12,
    "Charger": 30
}

print('=================Inventory Management System================')


def show_products():
  for product, quantity in inventory.items():
    print(product, '->', quantity)


def add_products():
  product = input('Enter the product name: ')
  quantity = int(input('Enter the quantity of product: '))

  if product in inventory:
    inventory[product] += quantity
    print('product added to inventory successfully 👍')
    print('Available Stock in inventory -> ', product, '->', inventory[product])

  else:
    inventory[product] = quantity



def sell_product():
  product = input('Enter the product name: ')
  quantity = int(input('Enter the quantity of product: '))

  if product not in inventory:
    print('product not found')

  elif quantity > inventory[product]:
    print('Out of stock')

  else:
    inventory[product] -= quantity
    print('product sold successfully 👍')
    print('Remaining Stock -> ', product, '->', inventory[product])


def search_product():
  product = input('Enter the product name: ')

  if product in inventory:
    print('Products Currently Available in Inventory is', product, '->', inventory[product])

  elif product not in inventory:
    print('SORRY!🥲 Product not in Inventory')

  else:
    print('product is out of stock for now 😭')

show_products()
add_products()
sell_product()
search_product()