from shape import Shape
from copy import deepcopy

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        print("Circle.draw")

    def resize(self, factor):
        self.radius *= factor

    def clone(self):
        return deepcopy(self)

    def __str__(self):
        return "Circle with radius {}".format(self.radius)