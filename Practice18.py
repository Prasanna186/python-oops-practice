class Product :
    def __init__(self,name,price):
        self.name = name
        self.price = price
class ShoppingCart :
    def __init__(self):
        self.products = []
    def add_product(self,product):
        self.products.append(product)
    def remove_product(self,product):
        self.products.remove(product)
    def calculate_total(self):
        total = 0
        for product in self.products:
            total += product.price
        return total
    def display_cart(self):
        print("Shopping Cart:")
        for product in self.products:
            print(f"Product Name: {product.name}, Price: {product.price}")
        print(f"Total Price: {self.calculate_total()}")
ShoppingCart1 = ShoppingCart()
product1 = Product("Laptop", 50000)
product2 = Product("Mouse", 500)
product3 = Product("Keyboard", 1000)
ShoppingCart1.add_product(product1)
ShoppingCart1.add_product(product2)
ShoppingCart1.add_product(product3)
ShoppingCart1.display_cart()
ShoppingCart1.remove_product(product2)
ShoppingCart1.display_cart()


