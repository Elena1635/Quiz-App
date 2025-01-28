"""
credit = float(input("Introdu suma creditului:"))
rata = float(input("Introdu rata dobânzii (în procente):"))
timp = float(input("Introdu perioada (în ani):"))

dobanda = (credit * rata * timp) / 100
print(f"Dobânda acumulată este: {dobanda:.2f}")
"""
def get_float_input(mesaj):
    while True:
        try:
            valoare = float(input(mesaj))
            return valoare
        except ValueError:
            print("Eroare: Te rog să introduci un număr valid!")

credit = get_float_input("Introdu suma creditului: ")
rata = get_float_input("Introdu rata dobânzii (în procente): ")
timp = get_float_input("Introdu perioada (în ani): ")

dobanda = (credit * rata * timp) / 100
print(f"Dobânda acumulată este: {dobanda:.2f}")
