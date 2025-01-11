def citeste_filme(denumire_fisier):
    filme = {}
    try:
        with open(denumire_fisier, "r") as fisier:
            for linie in fisier:
                titlu, evaluare = linie.strip().split(", ")
                filme[titlu] = int(evaluare)
    except FileNotFoundError:
        print(f"Fisierul {denumire_fisier} nu a fost găsit. Se va crea unul nou la salvare.")
    return filme

def scrie_filme(denumire_fisier, filme):
    with open(denumire_fisier, "w") as fisier:
        for titlu, evaluare in filme.items():
            fisier.write(f"{titlu}, {evaluare}\n")

def afiseaza_filme(filme):
    filme_sortate = sorted(filme.items(), key=lambda x: x[1], reverse=True)
    print("\nLista de filme:")
    for titlu, evaluare in filme_sortate:
        print(f"{titlu}: {evaluare}")

def adauga_film(filme):
    titlu = input("Introduceți titlul filmului: ").strip()
    if titlu in filme:
        print("Acest film există deja. Folosiți opțiunea de actualizare.")
        return
    evaluare = validare_evaluare()
    filme[titlu] = evaluare
    print(f"Film adăugat: {titlu} cu evaluarea {evaluare}.")

def actualizeaza_evaluare(filme):
    titlu = input("Introduceți titlul filmului pentru actualizare: ").strip()
    if titlu not in filme:
        print("Acest film nu există în listă.")
        return
    evaluare = validare_evaluare()
    filme[titlu] = evaluare
    print(f"Evaluarea filmului {titlu} a fost actualizată la {evaluare}.")

def sterge_film(filme):
    titlu = input("Introduceți titlul filmului pentru ștergere: ").strip()
    if titlu in filme:
        del filme[titlu]
        print(f"Film șters: {titlu}.")
    else:
        print("Acest film nu există în listă.")

def validare_evaluare():
    while True:
        try:
            evaluare = int(input("Introduceți o evaluare între 1 și 5: "))
            if 1 <= evaluare <= 5:
                return evaluare
            else:
                print("Evaluarea trebuie să fie între 1 și 5.")
        except ValueError:
            print("Introduceți un număr valid.")

def meniu_principal():
    denumire_fisier = "movies.txt"
    filme = citeste_filme(denumire_fisier)

    while True:
        print("\n--- Sistem de Evaluare a Filmelor ---")
        print("1. Vizualizează toate filmele și evaluările lor")
        print("2. Adaugă un nou film și evaluarea sa")
        print("3. Actualizează evaluarea unui film existent")
        print("4. Șterge un film din listă")
        print("5. Salvează și ieși")

        optiune = input("Alegeți o opțiune: ").strip()

        if optiune == "1":
            afiseaza_filme(filme)
        elif optiune == "2":
            adauga_film(filme)
        elif optiune == "3":
            actualizeaza_evaluare(filme)
        elif optiune == "4":
            sterge_film(filme)
        elif optiune == "5":
            scrie_filme(denumire_fisier, filme)
            print("Modificările au fost salvate. La revedere!")
            break
        else:
            print("Opțiune invalidă. Încercați din nou.")

if __name__ == "__main__":
    meniu_principal()