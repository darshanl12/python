class PizzaShop:
    def __init__(self, name):
        self.name = name
        self.menu = {}
        self.orders = []

    def add_item(self, item_name, price):
        self.menu[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.menu:
            del self.menu[item_name]

    def place_order(self, item_name, quantity):
        if item_name in self.menu:
            self.orders.append({"item": item_name, "quantity": quantity})
        else:
            print("Item not found in the menu.")

    def view_menu(self):
        print("Menu:")
        for item, price in self.menu.items():
            print(f"{item}: ${price}")

    def view_orders(self):
        print("Orders:")
        for order in self.orders:
            print(f"{order['item']} x {order['quantity']}")

shop = PizzaShop("Pizza Palace")
shop.add_item("Margherita", 10.99)
shop.add_item("Pepperoni", 12.99)
shop.add_item("Veggie", 11.99)

while True:
    print("\n1. View Menu")
    print("2. Place Order")
    print("3. View Orders")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        shop.view_menu()
    elif choice == "2":
        item_name = input("Enter the item name: ")
        quantity = int(input("Enter the quantity: "))
        shop.place_order(item_name, quantity)
    elif choice == "3":
        shop.view_orders()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")