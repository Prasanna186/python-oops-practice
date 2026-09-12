class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author} - ₹{self.price}"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', price={self.price})"


book = Book("Atomic Habits", "James Clear", 500)

print(book)
print(repr(book))


 # A useful rule to remember:

# __str__ = "How should a user see this object?" - human-readable representation

# __repr__ = "How should a developer inspect this object?" - developer/debug representation