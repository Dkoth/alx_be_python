#polymorphism_demo.py
import math

#Initializing Base Class
class Shape:
    def area(self):
        #Errors occure because it should be implemented by derived class
        raise NotImplementedError("Subclasses must override this method")
#Derived classes
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    #Overridding the area()method
    def area(self):
        return self.length * self.width

    class Circle(Shape):
        def __init__(self, radius):
            self.radius - radius

        def area(self):
            return math.pi * (self.radius ** 2)
