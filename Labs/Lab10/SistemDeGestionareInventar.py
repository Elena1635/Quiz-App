class Inventar:
    def __init__(self):
        self.produs_inventar = {}

    def adauga_produs(self):
        try:
            nume_produs = input("Introduceți numele produsului: ").strip()
            if not nume_produs:
                raise ValueError("Numele produsului nu poate fi gol.")
            cantitate = int(input("Introduceți cantitatea produsului: "))
            if cantitate <= 0:
                raise ValueError("Cantitatea trebuie să fie un număr pozitiv.")
            if nume_produs in self.produs_inventar:
                self.produs_inventar[nume_produs] += cantitate
            else:
                self.produs_inventar[nume_produs] = cantitate
            print(
                f"Produsul '{nume_produs}' a fost adăugat cu succes, cantitatea actualizată este {self.produs_inventar[nume_produs]}.")
        except ValueError as e:
            print(f"Eroare: {e}")

    def cauta_produs(self):
        nume_produs = input("Introduceți numele produsului de căutat: ").strip()
        if nume_produs in self.produs_inventar:
            print(f"Produsul '{nume_produs}' are cantitatea de {self.produs_inventar[nume_produs]}.")
        else:
            print(f"Produsul '{nume_produs}' nu există în inventar.")

    def actualizeaza_cantitate(self):
        try:
            nume_produs = input("Introduceți numele produsului pentru a actualiza cantitatea: ").strip()
            if nume_produs not in self.produs_inventar:
                raise ValueError("Produsul nu există în inventar.")
            cantitate_noua = int(input("Introduceți cantitatea actualizată: "))
            if cantitate_noua < 0:
                raise ValueError("Cantitatea nu poate fi negativă.")
            self.produs_inventar[nume_produs] = cantitate_noua
            print(f"Cantitatea produsului '{nume_produs}' a fost actualizată la {cantitate_noua}.")
        except ValueError as e:
            print(f"Eroare: {e}")

def meniu():
    inventar = Inventar()
    while True:
        print("\nMeniu:")
        print("1. Adăugați produs")
        print("2. Căutați produs")
        print("3. Actualizați cantitatea unui produs")
        print("4. Ieși")

        alegere = input("Alegeți opțiunea: ")
        if alegere == '1':
            inventar.adauga_produs()
        elif alegere == '2':
            inventar.cauta_produs()
        elif alegere == '3':
            inventar.actualizeaza_cantitate()
        elif alegere == '4':
            print("Ieșire din program.")
            break
        else:
            print("Opțiune invalidă! Vă rugăm să alegeți o opțiune validă.")

if __name__ == "__main__":
    meniu()
