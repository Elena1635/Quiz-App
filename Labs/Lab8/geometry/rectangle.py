def area(length, width):
    if length < 0 or width < 0:
        raise ValueError("Lungimea și lățimea trebuie să fie numere pozitive.")
    return length * width

def perimeter(length, width):
    if length < 0 or width < 0:
        raise ValueError("Lungimea și lățimea trebuie să fie numere pozitive.")
    return 2 * (length + width)
