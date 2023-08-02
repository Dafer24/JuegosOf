class Inventory:

    def __init__(self):
        self.inventory_dict = {}

    def add_product(self, name, price, stock):
        self.inventory_dict[name] = [price, stock]

    def update_price(self, name, new_price):
        if name in self.inventory_dict:
            self.inventory_dict[name][0] = new_price

    def show_inventory(self):
        print("Current Inventory:")
        for name, info in self.inventory_dict.items():
            price, stock = info
            print(f"{name} - Price: {price} - Stock: {stock}")


if __name__ == "__main__":
    inventory = Inventory()

    inventory.add_product("boots", 20.000, 3)
    inventory.add_product("flip-flops", 15.000, 2)

    inventory.show_inventory()

    inventory.update_price("boots", 50.000)

    inventory.show_inventory()
