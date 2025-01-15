def count_words_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        print(f"Fișierul {file_path} nu a fost găsit.")
        return 0
    except Exception as e:
        print(f"A apărut o eroare: {e}")
        return 0
file_path = 'example.txt'
num_words = count_words_in_file(file_path)
print(f"Numărul total de cuvinte din fișier este: {num_words}")
