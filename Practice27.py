# Dunder Methods
class Book :
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price
    def __str__(self):
        return f"{self.title} by {self.author} - {self.price}"
book = Book("Atomic Habits", "James Clear", 500)
print(book) # automatically calls book.__str__().