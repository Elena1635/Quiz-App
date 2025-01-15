def filter_lines(input_file, output_file, keyword):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            with open(output_file, 'w', encoding='utf-8') as outfile:
                for line in infile:
                    if keyword in line:
                        outfile.write(line)
        print(f"Fișierul '{output_file}' a fost creat cu succes.")
    except FileNotFoundError:
        print(f"Fișierul '{input_file}' nu a fost găsit.")
    except Exception as e:
        print(f"A apărut o eroare: {e}")

input_file = 'input2.txt'
output_file = 'filtered.txt'
keyword = 'Python'
filter_lines(input_file, output_file, keyword)
