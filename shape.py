from abc import ABC, abstractmethod

# Abstract Base Classes (ABC) are a way to define interfaces that can be implemented by other classes.
class Shape(ABC):

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def resize(self, factor):
        pass

    @abstractmethod
    def clone(self):
        pass