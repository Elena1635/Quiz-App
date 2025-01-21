class Carte:
    def __init__(self, titlu, autor, ISBN):
        self.titlu = titlu
        self.autor = autor
        self.ISBN = ISBN
        self.este_imprumutata = False

    def __str__(self):
        return f"'{self.titlu}' de {self.autor} (ISBN: {self.ISBN})"

class MembruBiblioteca:
    def __init__(self, nume):
        self.nume = nume
        self.carti_imprumutate = []

    def imprumuta_carte(self, carte):
        if carte.este_imprumutata:
            print(f"Cartea {carte} este deja împrumutată.")
        else:
            carte.este_imprumutata = True
            self.carti_imprumutate.append(carte)
            print(f"{self.nume} a împrumutat cartea {carte}.")

    def returneaza_carte(self, carte):
        if carte in self.carti_imprumutate:
            carte.este_imprumutata = False
            self.carti_imprumutate.remove(carte)
            print(f"{self.nume} a returnat cartea {carte}.")
        else:
            print(f"{self.nume} nu a împrumutat cartea {carte}.")

class Biblioteca:
    def __init__(self):
        self.carti = []

    def adauga_carte(self, carte):
        self.carti.append(carte)
        print(f"Cartea {carte} a fost adăugată în bibliotecă.")

    def sterge_carte(self, carte):
        if carte in self.carti:
            self.carti.remove(carte)
            print(f"Cartea {carte} a fost ștearsă din bibliotecă.")
        else:
            print(f"Cartea {carte} nu se află în bibliotecă.")

    def listeaza_carti_disponibile(self):
        disponibile = [carte for carte in self.carti if not carte.este_imprumutata]
        if disponibile:
            print("Cărțile disponibile în bibliotecă sunt:")
            for carte in disponibile:
                print(f" - {carte}")
        else:
            print("Nu există cărți disponibile în bibliotecă.")

def adauga_carti_din_tastatura(biblioteca):
    while True:
        titlu = input("Introdu titlul cărții (sau 'stop' pentru a termina): ")
        if titlu.lower() == 'stop':
            break
        autor = input("Introdu autorul cărții: ")
        ISBN = input("Introdu ISBN-ul cărții: ")
        carte = Carte(titlu, autor, ISBN)
        biblioteca.adauga_carte(carte)

def adauga_membri_din_tastatura():
    membri = []
    while True:
        nume = input("Introdu numele membrului (sau 'stop' pentru a termina): ")
        if nume.lower() == 'stop':
            break
        membru = MembruBiblioteca(nume)
        membri.append(membru)
    return membri
def gestioneaza_operatiuni(biblioteca, membri):
    while True:
        print("\nOperațiuni disponibile:")
        print("1. Împrumută o carte")
        print("2. Returnează o carte")
        print("3. Listează cărți disponibile")
        print("4. Adaugă o carte în bibliotecă")
        print("5. Șterge o carte din bibliotecă")
        print("6. Ieșire")
        optiune = input("Alege o opțiune: ")

        if optiune == '1':
            nume_membru = input("Introdu numele membrului: ")
            membru = next((m for m in membri if m.nume == nume_membru), None)
            if not membru:
                print("Membrul nu există.")
                continue

            biblioteca.listeaza_carti_disponibile()
            titlu_carte = input("Introdu titlul cărții de împrumutat: ")
            carte = next((c for c in biblioteca.carti if c.titlu == titlu_carte), None)
            if carte:
                membru.imprumuta_carte(carte)
            else:
                print("Cartea nu există în bibliotecă.")

        elif optiune == '2':
            nume_membru = input("Introdu numele membrului: ")
            membru = next((m for m in membri if m.nume == nume_membru), None)
            if not membru:
                print("Membrul nu există.")
                continue

            titlu_carte = input("Introdu titlul cărții de returnat: ")
            carte = next((c for c in membru.carti_imprumutate if c.titlu == titlu_carte), None)
            if carte:
                membru.returneaza_carte(carte)
            else:
                print("Membrul nu a împrumutat această carte.")

        elif optiune == '3':
            biblioteca.listeaza_carti_disponibile()

        elif optiune == '4':
            titlu = input("Introdu titlul cărții: ")
            autor = input("Introdu autorul cărții: ")
            ISBN = input("Introdu ISBN-ul cărții: ")
            carte = Carte(titlu, autor, ISBN)
            biblioteca.adauga_carte(carte)

        elif optiune == '5':
            titlu = input("Introdu titlul cărții de șters: ")
            carte = next((c for c in biblioteca.carti if c.titlu == titlu), None)
            if carte:
                biblioteca.sterge_carte(carte)
            else:
                print("Cartea nu există în bibliotecă.")

        elif optiune == '6':
            print("La revedere!")
            break

        else:
            print("Opțiune invalidă. Încearcă din nou.")

biblioteca = Biblioteca()

print("Adăugare cărți în bibliotecă:")
adauga_carti_din_tastatura(biblioteca)

print("Adăugare membri în bibliotecă:")
membri = adauga_membri_din_tastatura()

gestioneaza_operatiuni(biblioteca, membri)

