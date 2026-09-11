from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
class Rectangle(shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
class Square(shape):
    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side * self.side
circle = Circle(10)
rectangle = Rectangle(5,10)
square = Square(4)
print(f"Area of Circle : {circle.area()}")
print(f"Area of Rectangle : {rectangle.area()}")
print(f"Area of Square : {square.area()}")  


shapes = [
    Circle(10),
    Rectangle(5, 10),
    Square(4)
]

for shape in shapes:
    print(f"Area: {shape.area()}")