class Rectangle :
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)
    def display_details(self):
        print(f"Length : {self.length}\nWidth : {self.width}\nArea : {self.area()}\nPerimeter : {self.perimeter()}")

rect1 = Rectangle(5,10)
rect1.display_details()
