def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Eroare: Împărțirea la zero nu este permisă."
def main():
    încercări = 5
    while încercări > 0:
        try:
            x = float(input("Introduceți primul număr (deimpartitul): "))
            y = float(input("Introduceți al doilea număr (împărțitorul): "))
            print("Rezultatul este:", safe_divide(x, y))
            break
        except ValueError:
            încercări -= 1
            print(f"Eroare: Introduceți doar numere valide. Mai aveți {încercări} încercări.")
    if încercări == 0:
        print("Programul s-a încheiat din cauza prea multor erori.")

if __name__ == "__main__":
    main()
