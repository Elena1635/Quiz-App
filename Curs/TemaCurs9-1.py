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

def get_valid_interval(prompt_min, prompt_max):
    while True:
        min_value = get_float_input(prompt_min)
        max_value = get_float_input(prompt_max)
        if min_value < max_value:
            return min_value, max_value
        else:
            print("Valoarea minimă trebuie să fie mai mică decât valoarea maximă. Încercați din nou.")

# Exercițiul 1: Analiza și Vizualizarea Datelor Meteo
# Introducere date
print("Introduceți intervalul temperaturii (min și max) în °C: ")
min_temp, max_temp = get_valid_interval("Temperatura minimă: ", "Temperatura maximă: ")
print("Introduceți intervalul umidității (min și max) în %: ")
min_humidity, max_humidity = get_valid_interval("Umiditate minimă: ", "Umiditate maximă: ")
print("Introduceți intervalul vitezei vântului (min și max) în km/h: ")
min_wind, max_wind = get_valid_interval("Viteza minimă: ", "Viteza maximă: ")

# Generarea datelor
np.random.seed(0)
dates = pd.date_range(start="2024-01-01", periods=365)
temperature = np.random.uniform(min_temp, max_temp, 365)
humidity = np.random.uniform(min_humidity, max_humidity, 365)
wind_speed = np.random.uniform(min_wind, max_wind, 365)

data_meteo = pd.DataFrame({
    "Data": dates,
    "Temperatura": temperature,
    "Umiditate": humidity,
    "Viteza Vântului": wind_speed
})

# Procesarea datelor
data_meteo["Temperatura Resimțita"] = data_meteo["Temperatura"] - 0.7 * (data_meteo["Umiditate"] / 100)
max_temp_day = data_meteo.loc[data_meteo["Temperatura Resimțita"].idxmax()]
min_temp_day = data_meteo.loc[data_meteo["Temperatura Resimțita"].idxmin()]

# Vizualizare
plt.figure(figsize=(10, 6))
plt.plot(data_meteo["Data"], data_meteo["Temperatura"], label="Temperatura")
plt.plot(data_meteo["Data"], data_meteo["Temperatura Resimțita"], label="Temperatura Resimțita")
plt.xlabel("Data")
plt.ylabel("Temperatura (°C)")
plt.title("Temperatura și Temperatura Resimțită pe parcursul anului")
plt.legend()
plt.show()

# Calcularea temperaturii medii lunare
data_meteo["Luna"] = data_meteo["Data"].dt.month
mean_temp_monthly = data_meteo.groupby("Luna")["Temperatura"].mean()

plt.figure(figsize=(10, 6))
plt.bar(mean_temp_monthly.index, mean_temp_monthly.values)
plt.xlabel("Luna")
plt.ylabel("Temperatura Medie (°C)")
plt.title("Temperatura Medie Lunară")
plt.xticks(mean_temp_monthly.index)
plt.show()
