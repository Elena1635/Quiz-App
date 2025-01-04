import re

def verifica_parola(parola):
    criterii_neindeplinite = []

    if len(parola) < 8:
        criterii_neindeplinite.append("Lungimea trebuie să fie de cel puțin 8 caractere.")
    if not re.search(r'[A-Z]', parola):
        criterii_neindeplinite.append("Lipsește o literă majusculă.")
    if not re.search(r'[a-z]', parola):
        criterii_neindeplinite.append("Lipsește o literă minusculă.")
    if not re.search(r'[0-9]', parola):
        criterii_neindeplinite.append("Lipsește o cifră.")
    if not re.search(r'[!@#$%^&*()\-_+=<>?]', parola):
        criterii_neindeplinite.append("Lipsesc caractere speciale.")
    if ' ' in parola:
        criterii_neindeplinite.append("Parola nu trebuie să conțină spații.")

    if criterii_neindeplinite:
        print("Parola dvs. este slabă.")
        print("Probleme identificate:")
        for criteriu in criterii_neindeplinite:
            print(f"- {criteriu}")
    else:
        print("Parola dvs. este puternică.")


def main():
    input_parole = input("Introduceți parolele (separate prin virgulă): ")
    parole = input_parole.split(',')

    for parola in parole:
        parola = parola.strip()
        print(f"\nVerificare pentru: {parola}")
        verifica_parola(parola)

if __name__ == "__main__":
    main()