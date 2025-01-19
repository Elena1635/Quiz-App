import math

def area(radius):
    if radius < 0:
        raise ValueError("Raza cercului trebuie să fie un număr pozitiv.")
    return math.pi * radius**2

def circumference(radius):
    if radius < 0:
        raise ValueError("Raza cercului trebuie să fie un număr pozitiv.")
    return 2 * math.pi * radius
