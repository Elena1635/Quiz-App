import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Vă rugăm să introduceți un număr valid.")

# Introducere date
print("Introduceți prețul inițial al acțiunii: ")
initial_price = get_float_input("Preț inițial: ")
print("Introduceți abaterea standard a modificării procentuale zilnice (în %): ")
std_dev = get_float_input("Abatere standard: ")

# Generarea datelor
np.random.seed(0)
dates_stock = pd.date_range(start="2024-01-01", periods=730)
percentage_change = np.random.normal(0, std_dev, 730) / 100
price = initial_price * (1 + percentage_change).cumprod()

data_stock = pd.DataFrame({
    "Data": dates_stock,
    "Schimbare Zilnică (%)": percentage_change * 100,
    "Preț de Închidere": price
})

# Procesarea datelor
data_stock["Media Mobilă 30"] = data_stock["Preț de Închidere"].rolling(window=30).mean()
data_stock["Media Mobilă 100"] = data_stock["Preț de Închidere"].rolling(window=100).mean()
over_100 = data_stock[data_stock["Preț de Închidere"] > data_stock["Media Mobilă 100"]]

# Vizualizare
plt.figure(figsize=(10, 6))
plt.plot(data_stock["Data"], data_stock["Preț de Închidere"], label="Preț de Închidere")
plt.plot(data_stock["Data"], data_stock["Media Mobilă 30"], label="Media Mobilă 30 zile")
plt.plot(data_stock["Data"], data_stock["Media Mobilă 100"], label="Media Mobilă 100 zile")
plt.xlabel("Data")
plt.ylabel("Preț (")
plt.title("Prețul Acțiunilor și Mediile Mobile")
plt.legend()
plt.show()