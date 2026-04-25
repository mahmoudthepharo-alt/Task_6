class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

L=int(input("Enter the length of the rectangle: "))
W=int(input("Enter the width of the rectangle: "))
rectangle = Rectangle(L, W)
print(rectangle.get_area())   