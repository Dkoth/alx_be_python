#main.py
from polymorphism_demo import Shape, Rectangle, Circle

def main():
    # Creating a Rectangle and Circle instance
    rectangle = Rectangle(10, 5)
    circle = Circle(7)

    # Demonstrating polymorphism
    shapes = [rectangle, circle]

    for shape in shapes:
        print(f"The area of the {type(shape).__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()
