import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

num_days = 60

daily_sales = []

for day in range(num_days):

    num_products = np.random.randint(5, 20)

    prices = np.random.normal(loc=40, scale=8, size=num_products)
    prices = np.clip(prices, 10, None)

    quantities = np.random.randint(1, 11, size=num_products)

    promo_mask = np.random.rand(num_products) < 0.3
    discounted_prices = prices.copy()
    discounted_prices[promo_mask] *= 0.8

    sales_per_product = discounted_prices * quantities

    total_sales = np.sum(sales_per_product)

    total_profit = total_sales * 0.3

    daily_sales.append(
        [day + 1, num_products, total_sales, total_profit, np.mean(discounted_prices), np.mean(quantities),
         promo_mask.sum()])

df = pd.DataFrame(daily_sales,
                  columns=["Day", "Num_Products", "Total_Sales", "Total_Profit", "Avg_Price", "Avg_Quantity",
                           "Num_Promotions"])

stats = {
    "Average Price": df["Avg_Price"].mean(),
    "Max Price": df["Avg_Price"].max(),
    "Min Price": df["Avg_Price"].min(),
    "Average Quantity": df["Avg_Quantity"].mean(),
    "Max Quantity": df["Avg_Quantity"].max(),
    "Min Quantity": df["Avg_Quantity"].min(),
    "Average Profit": df["Total_Profit"].mean(),
    "Max Profit": df["Total_Profit"].max(),
    "Min Profit": df["Total_Profit"].min(),
    "Total Sales (60 days)": df["Total_Sales"].sum(),
    "Total Profit (60 days)": df["Total_Profit"].sum()
}
plt.figure(figsize=(12, 6))
plt.plot(df["Day"], df["Total_Sales"], label="Total Sales", marker="o")
plt.plot(df["Day"], df["Total_Profit"], label="Total Profit", marker="s")
plt.xlabel("Day")
plt.ylabel("Amount")
plt.title("Evolution of Sales and Profit Over 60 Days")
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(12, 6))
plt.hist(df["Avg_Price"], bins=15, color='blue', alpha=0.7, edgecolor='black')
plt.xlabel("Average Price")
plt.ylabel("Frequency")
plt.title("Distribution of Prices Over 60 Days")
plt.grid()
plt.show()

plt.figure(figsize=(12, 6))
plt.hist(df["Avg_Quantity"], bins=10, color='green', alpha=0.7, edgecolor='black')
plt.xlabel("Average Quantity")
plt.ylabel("Frequency")
plt.title("Distribution of Quantities Sold Over 60 Days")
plt.grid()
plt.show()

plt.figure(figsize=(12, 6))
plt.bar(df["Day"], df["Num_Promotions"], color='red', alpha=0.7)
plt.xlabel("Day")
plt.ylabel("Number of Promotions")
plt.title("Number of Promotions Applied Each Day")
plt.grid()
plt.show()

print(df.head())

for key, value in stats.items():
    print(f"{key}: {value:.2f}")

""""
import numpy as np
import pandas as pd

# Setăm seed pentru reproducibilitate
np.random.seed(42)

# Numărul de zile
num_days = 60

# Inițializăm listele pentru stocarea datelor
daily_sales = []

for day in range(num_days):
    # Generăm numărul de produse vândute în această zi (între 5 și 15)
    num_products = np.random.randint(5, 16)

    # Generăm prețurile produselor folosind o distribuție normală
    prices = np.random.normal(loc=40, scale=8, size=num_products)
    prices = np.clip(prices, 10, None)  # Asigurăm că prețurile nu sunt negative

    # Generăm cantitățile vândute folosind o distribuție uniformă
    quantities = np.random.randint(1, 11, size=num_products)

    # Aplicăm promoții cu o probabilitate de 30%
    promo_mask = np.random.rand(num_products) < 0.3
    discounted_prices = prices.copy()
    discounted_prices[promo_mask] *= 0.8  # Reducere de 20%

    # Calculăm vânzările per produs
    sales_per_product = discounted_prices * quantities

    # Total vânzări pe zi
    total_sales = np.sum(sales_per_product)

    # Calculăm profitul pe zi (30% din totalul vânzărilor)
    total_profit = total_sales * 0.3

    # Salvăm datele
    daily_sales.append(
        [day + 1, num_products, total_sales, total_profit, np.mean(discounted_prices), np.mean(quantities),
         promo_mask.sum()])

# Creăm un DataFrame
df = pd.DataFrame(daily_sales,
                  columns=["Day", "Num_Products", "Total_Sales", "Total_Profit", "Avg_Price", "Avg_Quantity",
                           "Num_Promotions"])

# Statistici generale
stats = {
    "Average Price": df["Avg_Price"].mean(),
    "Max Price": df["Avg_Price"].max(),
    "Min Price": df["Avg_Price"].min(),
    "Average Quantity": df["Avg_Quantity"].mean(),
    "Max Quantity": df["Avg_Quantity"].max(),
    "Min Quantity": df["Avg_Quantity"].min(),
    "Average Profit": df["Total_Profit"].mean(),
    "Max Profit": df["Total_Profit"].max(),
    "Min Profit": df["Total_Profit"].min(),
    "Total Sales (60 days)": df["Total_Sales"].sum(),
    "Total Profit (60 days)": df["Total_Profit"].sum()
}

# Analiza veniturilor și profitului
evolution_data = df[["Day", "Total_Sales", "Total_Profit"]]

# Distribuția prețurilor și cantităților
distribution_data = df[["Avg_Price", "Avg_Quantity"]]

# Impactul promoțiilor
promotions_data = df[["Day", "Num_Promotions"]]

# Afișăm primele 5 zile din dataset
print(df.head())

# Afișăm statisticile generale
for key, value in stats.items():
    print(f"{key}: {value:.2f}")

# Afișăm analiza datelor
print("\nEvoluția veniturilor și profitului:")
print(evolution_data.head())

print("\nDistribuția prețurilor și cantităților:")
print(distribution_data.describe())

print("\nImpactul promoțiilor:")
print(promotions_data.head())

"""