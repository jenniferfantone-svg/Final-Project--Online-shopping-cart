class ItemToPurchase:
    def __init__(self, name="none", price=0.0, quantity=0, description="none"):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description

        
    def print_item_cost(self):
        total = self.price * self.quantity
        print(f"{self.name} {self.quantity} @ ${self.price:.2f} = ${total:.2f}")


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart.")

    def modify_item(self, modified_item):
        for item in self.cart_items:
            if item.name == modified_item.name:
                item.quantity = modified_item.quantity
                return
            print("Item not found in cart.")

    def get_num_items(self):
        return sum(item.quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        return sum(item.price * item.quantity for item in self.cart_items)

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")

        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()

        print(f"Total: ${self.get_cost_of_cart():.2f}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Description")
        for item in self.cart_items:
            print(f"{item.name}: {item.description}")


def print_menu(cart):
    menu = (
        "\nMENU\n"
        "a - Add item to cart\n"
        "r - Remove item from cart\n"
        "c - Change item quantity\n"
        "i - Output items' descriptions\n"
        "o - Output shopping cart\n"
        "q - Quit\n"
    )

    command = ""
    while command != "q":
        print(menu)
        command = input("Choose an option: ").lower()

        if command == "a":
            name = input("Enter the item name: ")
            description = input("Enter the item description: ")
            price = float(input("Enter the item price: "))
            quantity = int(input("Enter the item quantity: "))
            cart.add_item(ItemToPurchase(name, price, quantity, description))

        elif command == "r":
            name = input("Enter name of item to remove: ")
            cart.remove_item(name)

        elif command == "c":
            name = input("Enter the item name: ")
            quantity = int(input("Enter the new quantity: "))
            temp_item = ItemToPurchase(name=name, quantity=quantity)
            cart.modify_item(temp_item)

        elif command == "i":
            cart.print_descriptions()

        elif command == "o":
            cart.print_total()

        elif command == "q":
            print("Exiting menu.")

        else:
            print("Invalid option. Please try again.")

# MAIN PROGRAM
customer_name = input("Enter customer's name: ")
current_date = input("Enter today's date: ")

print(f"\nCustomer Name: {customer_name}")
print(f"Today's Date: {current_date}")

shopping_cart = ShoppingCart(customer_name, current_date)

print_menu(shopping_cart)
