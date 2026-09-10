class Product :
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def display_details(self):
        print(f"Product Name : {self.name}\nPrice : {self.price}\nQuantity : {self.quantity}")
    def total_value(self):
        return self.price * self.quantity

product1 = Product("Tote Bag", 650, 5)
product1.display_details()
print(f"Total Value : {product1.total_value()}")