import csv

def read_csv(file_path):

    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
    return data

def filter_data(data, key, value):
    return [row for row in data if row.get(key) == value]

def write_csv(data, file_path):
    if not data:
        raise ValueError("Nu există date de scris într-un fișier CSV.")

    with open(file_path, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    input_file = input("Introduceți calea fișierului CSV de intrare: ")
    key = input("Introduceți coloana pe baza căreia doriți să filtrați datele: ")
    value = input(f"Introduceți valoarea pentru coloana '{key}': ")
    output_file = input("Introduceți calea fișierului CSV de ieșire: ")

    try:
        data = read_csv(input_file)
        filtered_data = filter_data(data, key, value)

        write_csv(filtered_data, output_file)

        print(f"Datele filtrate au fost scrise într-un fișier: {output_file}")

    except Exception as e:
        print(f"A apărut o eroare: {e}")