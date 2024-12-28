class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        """Add an item to the shopping cart.
        
        Args:
            item: The item to add to the cart
        """
        self.items.append(item)
        
    def get_items(self):
        """Return all items in the cart."""
        return self.items.copy()
    
    def __str__(self):
        """Return a string representation of the cart."""
        return f"Cart: {', '.join(self.items)}"

# Example
def main():
    # Create separate cart instances
    cart1 = ShoppingCart()
    cart2 = ShoppingCart()
    
    # Add items to first cart
    cart1.add_item('Pioneer Rev 7')
    print(cart1)  # Cart: Pioneer Rev 7
    
    # Add items to second cart
    cart2.add_item('Laptop')
    cart2.add_item('Camera')
    print(cart2)  # Cart: Laptop, Camera
    
    # Demonstrate that carts are independent
    print(f"\nCart 1: {cart1.get_items()}")  # ['Pioneer Rev 7']
    print(f"Cart 2: {cart2.get_items()}")    # ['Laptop', 'Camera']

if __name__ == "__main__":
    main()