import math


def calculate_distance(x1, y1, x2, y2):

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


if __name__ == "__main__":
    try:
        print("Calculate the distance between two points in a 2D plane.")

        x1 = float(input("Enter the x-coordinate of the first point: "))
        y1 = float(input("Enter the y-coordinate of the first point: "))

        x2 = float(input("Enter the x-coordinate of the second point: "))
        y2 = float(input("Enter the y-coordinate of the second point: "))

        distance = calculate_distance(x1, y1, x2, y2)
        print(f"The distance between the points ({x1}, {y1}) and ({x2}, {y2}) is {distance:.2f}.")
    except ValueError:
        print("Please enter valid numeric values for the coordinates!")
