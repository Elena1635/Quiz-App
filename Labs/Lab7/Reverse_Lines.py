def reverse_lines(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            with open(output_file, 'w', encoding='utf-8') as outfile:
                for line in infile:
                    reversed_line = line.rstrip()[::-1]
                    outfile.write(reversed_line + '\n')
        print(f"Fișierul '{output_file}' a fost creat cu succes.")
    except FileNotFoundError:
        print(f"Fișierul '{input_file}' nu a fost găsit.")
    except Exception as e:
        print(f"A apărut o eroare: {e}")

input_file = 'input.txt'
output_file = 'output.txt'
reverse_lines(input_file, output_file)
