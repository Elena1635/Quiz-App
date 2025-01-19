from circle import area as circle_area, circumference
from rectangle import area as rectangle_area, perimeter

def main():
    try:
        radius = float(input("Introduceți raza cercului: "))
        try:
            print(f"Aria cercului este: {circle_area(radius)}")
            print(f"Circumferința cercului este: {circumference(radius)}")
        except ValueError as e:
            print(f"Eroare la calculul cercului: {e}")

        length = float(input("\nIntroduceți lungimea dreptunghiului: "))
        width = float(input("Introduceți lățimea dreptunghiului: "))
        try:
            print(f"Aria dreptunghiului este: {rectangle_area(length, width)}")
            print(f"Perimetrul dreptunghiului este: {perimeter(length, width)}")
        except ValueError as e:
            print(f"Eroare la calculul dreptunghiului: {e}")

    except ValueError:
        print("Eroare: Asigurați-vă că introduceți un număr valid.")
    except Exception as e:
        print(f"A apărut o eroare neașteptată: {e}")

if __name__ == "__main__":
    main()
