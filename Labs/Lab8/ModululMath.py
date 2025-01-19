import math

def main():
    try:
        num = int(input("Introduceți un număr pentru a calcula rădăcina pătrată și factorialul: "))
        angle = float(input("Introduceți un unghi în grade pentru a calcula sinusul: "))

        sqrt_result = math.sqrt(num)

        factorial_result = math.factorial(num)

        angle_radians = math.radians(angle)
        sin_result = math.sin(angle_radians)

        print(f"Rădăcina pătrată a {num} este {sqrt_result}")
        print(f"Factorialul lui {num} este {factorial_result}")
        print(f"Sinusul unghiului de {angle} grade este {sin_result}")
    except ValueError:
        print("Eroare: Asigurați-vă că introduceți un număr valid.")
    except Exception as e:
        print(f"A apărut o eroare: {e}")

if __name__ == "__main__":
    main()
