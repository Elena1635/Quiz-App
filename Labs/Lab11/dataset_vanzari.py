import numpy as np
import pandas as pd

np.random.seed(42)

zile = 60
produse = ["Tableta", "Laptop", "Televizor", "Monitor", "Camera Foto", "Mouse", "Tastatura", "Casti", "Telefon", "Imprimanta"]
data = []

for zi in range(1, zile + 1):
    numar_produse = np.random.randint(5, 16)
    produse_aleatoare = np.random.choice(produse, numar_produse)
    preturi = np.random.normal(40, 8, numar_produse).clip(min=5)
    cantitati = np.random.randint(1, 11, numar_produse)
    promotii = np.random.choice([0, 1], numar_produse, p=[0.7, 0.3])
    preturi_finale = preturi * (1 - 0.2 * promotii)

    for produs, pret, cantitate, promotie, pret_final in zip(produse_aleatoare, preturi, cantitati, promotii, preturi_finale):
        data.append({
            "Zi": zi,
            "Produs": produs,
            "Pret Initial": round(pret, 2),
            "Promotie": bool(promotie),
            "Pret Final": round(pret_final, 2),
            "Cantitate": cantitate,
            "Total Vanzari": round(pret_final * cantitate, 2),
            "Cost": round(pret_final * cantitate * 0.7, 2)
        })

df = pd.DataFrame(data)

df["Profit"] = df["Total Vanzari"] - df["Cost"]

rezumat_pe_zi = df.groupby("Zi").agg({
    "Total Vanzari": "sum",
    "Profit": "sum"
}).reset_index()

statistici = {
    "Preturi": {
        "Media": round(df["Pret Final"].mean(), 2),
        "Maxim": round(df["Pret Final"].max(), 2),
        "Minim": round(df["Pret Final"].min(), 2)
    },
    "Cantitati": {
        "Media": round(df["Cantitate"].mean(), 2),
        "Maxim": df["Cantitate"].max(),
        "Minim": df["Cantitate"].min()
    },
    "Profituri": {
        "Media": round(rezumat_pe_zi["Profit"].mean(), 2),
        "Maxim": round(rezumat_pe_zi["Profit"].max(), 2),
        "Minim": round(rezumat_pe_zi["Profit"].min(), 2)
    },
    "Totaluri": {
        "Total Vanzari": round(df["Total Vanzari"].sum(), 2),
        "Profit Total": round(df["Profit"].sum(), 2)
    }
}

print("\nDatele generate:\n", df.head())
print("\nStatistici generale:")
for categorie, valori in statistici.items():
    print(categorie + ":")
    for cheie, valoare in valori.items():
        print(f"  {cheie}: {valoare}")

print("\nRezumat pe zile:\n", rezumat_pe_zi.head())
