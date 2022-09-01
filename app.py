# Prototype Design Pattern Shapes Example
# @author: Juan D. Londoño

from copy import deepcopy
from circle import Circle
from square import Square
from coloredShape import ColoredShape

class Application:
    shapes = []
    def __init__(self):
        self.shape = None

        circle = Circle(10)
        redCircle = ColoredShape(circle, "red")

        anotherRedCircle = redCircle.clone()

        self.addShape(redCircle)
        self.addShape(anotherRedCircle)

        square = Square(10)
        blueSquare = ColoredShape(square, "blue")

        anotherBlueSquare = blueSquare.clone()

        self.addShape(blueSquare)
        self.addShape(anotherBlueSquare)

    def addShape(self, shape):
        self.shapes.append(shape)

    def logic(self):
        shapesCopy = deepcopy(self.shapes)

        print("Shapes before resizing:")
        for shape in self.shapes:
            print(shape)

        shapesCopy[0].resize(2)
        shapesCopy[3].resize(2)

        print("Shapes after resizing:")
        for shape in shapesCopy:
            print(shape)

def main():
    app = Application()
    app.logic()

main()