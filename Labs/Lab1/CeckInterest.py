credit = float(input("Introdu suma creditului:"))
rata = float(input("Introdu rata dobânzii (în procente):"))
timp = float(input("Introdu perioada (în ani):"))

dobanda = (credit * rata * timp) / 100
print(f"Dobânda acumulată este: {dobanda:.2f}")