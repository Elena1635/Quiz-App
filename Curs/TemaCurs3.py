# Definirea datelor initiale
preturi_produse = {"mere": 1.0, "banane": 0.5, "portocale": 0.8, "mango": 1.5}
stoc_initial = {"mere": 10, "banane": 20, "portocale": 15, "mango": 5}
vanzari = [("mere", 4), ("banane", 6), ("portocale", 10), ("mango", 2)]

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