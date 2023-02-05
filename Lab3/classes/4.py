import math


class Point:
    def __init__(self, x, y):
        self.xcoor = x
        self.ycoor = y

    def show(self):
        return self.xcoor, self.ycoor

    def move(self, a, b):
        self.xcoor += a
        self.ycoor += b

    def dist(self, other):
        dx = other.xcoor - self.xcoor
        dy = other.ycoor - self.ycoor
        return math.sqrt(dx**2 + dy**2)


a = Point(3, 5)
b = Point(2, 7)
print(a.show())
a.move(1, -1)
print(a.show())
print(a.dist(b))
