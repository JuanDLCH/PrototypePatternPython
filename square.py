from shape import Shape
from copy import deepcopy

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def draw(self):
        print("Square.draw")

    def resize(self, factor):
        self.side *= factor

    def clone(self):
        return deepcopy(self)

    def __str__(self):
        return "Square with side {}".format(self.side)