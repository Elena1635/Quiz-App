import math_operations

def main():
    try:
        num1 = float(input("Introduceți primul număr: "))
        num2 = float(input("Introduceți al doilea număr: "))

        print(f"Adunare: {math_operations.add(num1, num2)}")
        print(f"Scădere: {math_operations.subtract(num1, num2)}")
        print(f"Înmulțire: {math_operations.multiply(num1, num2)}")
        try:
            print(f"Împărțire: {math_operations.divide(num1, num2)}")
        except ValueError as e:
            print(e)

    except ValueError:
        print("Eroare: Asigurați-vă că introduceți un număr valid.")
    except Exception as e:
        print(f"A apărut o eroare: {e}")

if __name__ == "__main__":
    main()
