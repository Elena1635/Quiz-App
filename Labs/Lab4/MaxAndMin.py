def find_max_and_min(numbers):

    if not numbers:
        return None, None

    maximum = max(numbers)
    minimum = min(numbers)

    return maximum, minimum

print("Introdu numere separate prin spațiu:")
input_numbers = input()
try:

    numbers = list(map(float, input_numbers.split()))
    if not numbers:
        print("Nu ai introdus numere valide!")
    else:

        maximum, minimum = find_max_and_min(numbers)

        print(f"Valoarea maximă este: {maximum}")
        print(f"Valoarea minimă este: {minimum}")
except ValueError:
    print("Te rog să introduci doar numere valide!")
