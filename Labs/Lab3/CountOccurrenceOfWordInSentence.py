def numara_cuvinte(propozitie):
    propozitie = propozitie.lower()
    cuvinte = propozitie.split()
    frecventa = {}
    for cuvant in cuvinte:
        if cuvant in frecventa:
            frecventa[cuvant] += 1
        else:
            frecventa[cuvant] = 1
    return frecventa
propozitie = input("Introdu o propoziție: ")
rezultat = numara_cuvinte(propozitie)
print("Frecvența fiecărui cuvânt în propoziție este:")
for cuvant, aparitii in rezultat.items():
    print(f"{cuvant}: {aparitii}")