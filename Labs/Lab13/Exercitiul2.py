import csv

def procesare_comenzi(input_file, output_file):
    # Deschidem fisierul de input pentru citire
    with open(input_file, mode='r', newline='') as infile:
        reader = csv.DictReader(infile)

        # Cream un fisier de output pentru scriere
        with open(output_file, mode='w', newline='') as outfile:
            # Definim header-ul pentru fisierul de output
            fieldnames = ['Produs', 'Cantitate', 'Pret unitar', 'Valoare totala']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()

            # Citim fiecare linie din fisierul CSV
            for row in reader:
                produs = row['Produs']
                cantitate = int(row['Cantitate'])
                pret_unitar = float(row['Pret unitar'])

                # Calculam valoarea totala pentru comanda
                valoare_totala = cantitate * pret_unitar

                # Scriem rezultatele in fisierul de output
                writer.writerow({
                    'Produs': produs,
                    'Cantitate': cantitate,
                    'Pret unitar': pret_unitar,
                    'Valoare totala': valoare_totala
                })

# Exemplu de utilizare:
input_file = 'comenzi.csv'  # Fisierul de input
output_file = 'rezultate_comenzi.csv'  # Fisierul de output
procesare_comenzi(input_file, output_file)
