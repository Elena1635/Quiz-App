# Definirea datelor initiale
preturi_produse = {"capsuni": 2.0, "piersici": 1.5, "portocale": 0.8, "cirese": 1.5}
stoc_initial = {"capsuni": 10, "piersici": 20, "portocale": 15, "cirese": 6}
vanzari = [("capsuni", 4), ("piersici", 6), ("portocale", 10), ("cirese", 2)]

# Calcularea venitului total si actualizarea stocului
venit_total = sum(preturi_produse[p] * c for p, c in vanzari if p in preturi_produse)
for produs, cantitate_vanduta in vanzari:
    if produs in stoc_initial:
        stoc_initial[produs] -= cantitate_vanduta

# Identificarea produselor ce necesita realimentare
produse_realimentare = {produs for produs, stoc in stoc_initial.items() if stoc < 5}

# Generarea raportului
print(f"Venit total: {venit_total:.2f} RON")
print("Stocuri ramase:")
for produs, stoc in stoc_initial.items():
    print(f"  - {produs}: {stoc}")
print("Produse ce necesita realimentare:" if produse_realimentare else "Nu sunt produse ce necesita realimentare.")
for produs in produse_realimentare:
    print(f"  - {produs}")