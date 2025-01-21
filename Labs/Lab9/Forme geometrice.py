import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasele trebuie să implementeze metoda area().")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle with radius {self.radius} has area {self.area():.2f}"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle with width {self.width} and height {self.height} has area {self.area()}"

while True:
    shape_type = input("Introduceți tipul de formă (circle/rectangle/exit): ").strip().lower()

    if shape_type == "circle":
        radius = input("Introduceți raza cercului: ")
        try:
            radius = float(radius)
            shape = Circle(radius)
            print(shape)
        except ValueError:
            print("Introduceți un număr valid!")

    elif shape_type == "rectangle":
        width = input("Introduceți lățimea dreptunghiului: ")
        height = input("Introduceți înălțimea dreptunghiului: ")
        try:
            width = float(width)
            height = float(height)
            shape = Rectangle(width, height)
            print(shape)
        except ValueError:
            print("Introduceți numere valide!")

    elif shape_type == "exit":
        break

    else:
        print("Tip invalid! Alegeți între 'circle', 'rectangle' sau 'exit'.")
