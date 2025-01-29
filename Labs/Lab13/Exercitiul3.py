import requests

def obtine_cursuri_de_schimb():
    # Utilizam API-ul pentru a obtine cursurile de schimb actuale
    url = "https://v6.exchangerate-api.com/v6/6361d032d28756f2768a65c4/latest/USD"  # Inlocuieste cu cheia ta API
    response = requests.get(url)

    # Verificam daca cererea a fost reusita
    if response.status_code == 200:
        data = response.json()
        return data['conversion_rates']
    else:
        print("Eroare la obținerea cursurilor de schimb!")
        return None

def citeste_moneda():
    while True:
        moneda = input("Introduceți moneda (ex. USD, EUR, RON): ").upper()
        if len(moneda) == 3:  # Verificăm dacă monedele au 3 caractere (ex. USD, EUR)
            return moneda
        else:
            print("Moneda introdusă nu este validă. Introduceți o monedă validă de 3 litere (ex. USD, EUR, RON).")

def citeste_suma():
    while True:
        try:
            suma = float(input("Introduceți suma pe care doriți să o converteșteți: "))
            if suma > 0:
                return suma
            else:
                print("Suma trebuie să fie un număr pozitiv.")
        except ValueError:
            print("Introducerea nu este validă. Vă rugăm să introduceți un număr valid.")

def conversie_valutara():
    # Obținem cursurile de schimb
    cursuri = obtine_cursuri_de_schimb()
    if not cursuri:
        return

    # Solicităm utilizatorului să introducă informațiile
    moneda_provenienta = citeste_moneda()
    moneda_destinatie = citeste_moneda()
    suma = citeste_suma()

    # Verificăm dacă monedele sunt valide
    if moneda_provenienta not in cursuri or moneda_destinatie not in cursuri:
        print("Una dintre monedele introduse nu este validă!")
        return

    # Calculăm cursul de schimb
    curs_de_schimb = cursuri[moneda_destinatie] / cursuri[moneda_provenienta]

    # Calculăm suma finală
    suma_finala = suma * curs_de_schimb

    # Afișăm rezultatele
    print(f"\nConversie valutară:")
    print(f"Suma inițială: {suma} {moneda_provenienta}")
    print(f"Cursul de schimb: 1 {moneda_provenienta} = {curs_de_schimb} {moneda_destinatie}")
    print(f"Suma finală: {suma_finala:.2f} {moneda_destinatie}")

# Exemplu de utilizare:
conversie_valutara()
