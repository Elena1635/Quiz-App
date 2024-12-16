def calculate_factorial(n):

    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        return factorial


if __name__ == "__main__":
    while True:
        try:
            num = input("Enter a non-negative integer to calculate its factorial: ")
            if not num.isdigit():
                raise ValueError("Input must be a non-negative integer.")
            num = int(num)

            result = calculate_factorial(num)
            print(f"The factorial of {num} is {result}.")
            break
        except ValueError as e:
            print(f"Error: {e}")
