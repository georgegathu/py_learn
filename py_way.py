def add_to_cart(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart

cart1 = add_to_cart('Pionner Rev 7')
print(cart1)

cart2 = add_to_cart('Laptop')
print(cart2)

cart3 = add_to_cart('Camera')
print(cart3)