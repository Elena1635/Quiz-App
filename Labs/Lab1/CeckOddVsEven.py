def check_odd_or_even(num):
    if num % 2 == 0:
        return "par"
    else:
        return "impar"

try:
    number = int(input("Introduceți un număr:"))
    result = check_odd_or_even(number)
    print(f"Numărul {number} este {result}.")
except ValueError:
    print("Te rog să introduci un număr întreg valid.")