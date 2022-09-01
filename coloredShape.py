from copy import deepcopy
from shape import Shape

class ColoredShape(Shape):
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color

    def draw(self):
        self.shape.draw()

    def resize(self, factor):
        self.shape.resize(factor)

    def clone(self):
        return deepcopy(self)

    def __str__(self):
        return "{} with color {}".format(self.shape, self.color)