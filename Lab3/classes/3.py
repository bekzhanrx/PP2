class Shape():
    def __init__(self):
        pass

    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, length, width):
        Shape.__init__(self)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


x = Rectangle(4, 5)
y = Shape()
print(x.area())
print(y.area())
