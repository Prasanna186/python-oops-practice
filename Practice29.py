class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author} - ₹{self.price}"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', price={self.price})"

    def __eq__(self, other):
       return (
        self.title == other.title
        and self.author == other.author
        and self.price == other.price
    )
    def __lt__(self, other):
       if not isinstance(other, Book):
        return NotImplemented

       return self.price < other.price

book1 = Book("Atomic Habits", "James Clear", 500)
book2 = Book("Atomic Habits", "James Clear", 500)
book3 = Book("Clean Code", "Robert Martin", 700)
print(book1 == book2)
print(book1 == book3)
print(book1 is book2)
print(book1 < book2)
print(book1 < book3)
print(book1 < 200)







