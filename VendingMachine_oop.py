class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Inventory:
    def __init__(self):
        self.inventory = [] 

    def add_product(self, product, quantity):
        self.inventory.append(product)

    def get_product(self, product_name, buy_quantity):
        for product in self.inventory:
            if product_name == product.name:
                return product
        return None

    def update_quantity(self, product_name, quantity):
        for product in self.inventory:
            if product_name == product.name:
                product.quantity -= quantity

    
class VendingMachine:
    def __init__(self, inventory):
        self.inventory = inventory

    def display_products(self):
        print("Available products: \n")
        for product in self.inventory.inventory:
            print(f"{product.name}: ${product.price}  {product.quantity} left. ")

    def select_product(self, product_name, buy_quantity):
        if self.inventory.get_product(product_name, buy_quantity):
            self.dispense_product(product_name, buy_quantity)
        else:
            print("The selected product either doesn't exist or is out of stock.\n")
        return None

    def dispense_product(self, product_name, buy_quantity):
        if buy_quantity > 0:
            ind = [i for i, prod in enumerate(self.inventory.inventory) if prod.name == product_name]
            quantity = self.inventory.inventory[ind[0]].quantity
            if buy_quantity <= quantity:
                total = self.inventory.inventory[ind[0]].price * buy_quantity
                self.insert_money(total, product_name, buy_quantity)
        else:
            print("You introduced an invalid quantity.")

    def insert_money(self, total, product_name, buy_quantity):
        print(f"Total: ${total}")
        inserted_money = 0
        while True:
            inserted_money += int(input(f"Introduce ${total - inserted_money}: $"))
            if inserted_money >= total:
                self.give_change(total, inserted_money)
                print(f"Thanks for buying {buy_quantity} {product_name}")
                self.inventory.update_quantity(product_name, buy_quantity)
                break
            else:
                print(f"Please introduce ${total - inserted_money}")

    def give_change(self, total, inserted_money):
        if inserted_money > total:
            print(f"Change: ${inserted_money - total}")

b = Product('banana', 5, 10)
c = Product('candy', 3, 20)

i = Inventory()
i.add_product(b, 0)
i.add_product(c, 0)

v = VendingMachine(i)

v.display_products()
v.select_product('banana', 1)
print(b.quantity)

