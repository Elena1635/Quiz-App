import math

def fibonacci(n, memo=None):
    if not isinstance(n, int):
        raise TypeError("Fibonacci number must be an integer.")
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers.")
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

def circle_area(radius):
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number.")
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * radius ** 2

def find_max(numbers):
    if not numbers:
        raise ValueError("Cannot find the maximum of an empty list.")
    if any(not isinstance(num, (int, float)) for num in numbers):
        raise TypeError("All elements in the list must be numbers.")
    return max(numbers)

def geometric_mean(numbers):
    if not numbers:
        raise ValueError("Cannot calculate geometric mean of an empty list.")
    if any(not isinstance(num, (int, float)) for num in numbers):
        raise TypeError("All elements in the list must be numbers.")
    if any(num <= 0 for num in numbers):
        raise ValueError("All numbers must be positive for geometric mean.")
    return math.prod(numbers) ** (1 / len(numbers))

def main():
    print("=== Fibonacci ===")
    try:
        n = int(input("Enter a number for Fibonacci: "))
        print(f"The {n}th Fibonacci number is: {fibonacci(n)}")
    except (ValueError, TypeError) as e:
        print(e)

    print("\n=== Circle Area ===")
    try:
        radius = float(input("Enter the radius of the circle: "))
        print(f"The area of a circle with radius {radius} is: {circle_area(radius)}")
    except (ValueError, TypeError) as e:
        print(e)

    print("\n=== Find Max ===")
    try:
        numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
        print(f"The maximum value in the list {numbers} is: {find_max(numbers)}")
    except (ValueError, TypeError) as e:
        print(e)

    print("\n=== Geometric Mean ===")
    try:
        numbers = list(map(float, input("Enter positive numbers separated by spaces: ").split()))
        print(f"The geometric mean of {numbers} is: {geometric_mean(numbers)}")
    except (ValueError, TypeError) as e:
        print(e)

main()
