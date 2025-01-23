def sum_numbers_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            total = 0
            for line in file:
                try:
                    number = float(line.strip())
                    total += number
                except ValueError:
                    print(f"Eroare: '{line.strip()}' nu este un număr valid și va fi ignorat.")
            return total
    except FileNotFoundError:
        return "Eroare: Fișierul nu există."
    except IOError:
        return "Eroare: A apărut o problemă la citirea fișierului."

if __name__ == "__main__":
    file_path = input("Introduceți calea către fișierul text: ")
    result = sum_numbers_from_file(file_path)
    print("Rezultatul este:", result)