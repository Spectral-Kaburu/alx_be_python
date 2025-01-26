import math


class shape:
    def area(self):
        NotImplementedError("The area() method should be overridden in a subclass")

class rectangle(shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    