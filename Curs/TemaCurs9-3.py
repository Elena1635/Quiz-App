import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Exercițiul 3: Analiza Datelor de Rating ale Filmelor
def get_positive_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Vă rugăm să introduceți un număr întreg pozitiv.")
        except ValueError:
            print("Vă rugăm să introduceți un număr întreg valid.")

print("Introduceți numărul de utilizatori: ")
num_users = get_positive_int_input("Număr utilizatori: ")
print("Introduceți numărul de filme: ")
num_movies = get_positive_int_input("Număr filme: ")
print("Introduceți numărul de evaluări: ")
num_ratings = get_positive_int_input("Număr evaluări: ")

# Generarea datelor
np.random.seed(0)
user_ids = np.random.randint(1, num_users + 1, num_ratings)
movie_ids = np.random.randint(1, num_movies + 1, num_ratings)
ratings = np.random.randint(1, 6, num_ratings)

data_ratings = pd.DataFrame({
    "ID Utilizator": user_ids,
    "ID Film": movie_ids,
    "Rating": ratings
})

# Procesarea datelor
average_rating = data_ratings.groupby("ID Film")["Rating"].mean()
num_ratings = data_ratings.groupby("ID Film").size()
filtered_movies = average_rating[(num_ratings > 50) & (average_rating < 3.5)]
top_5_movies = average_rating.nlargest(5)

# Vizualizare
plt.figure(figsize=(10, 6))
plt.hist(data_ratings["Rating"], bins=np.arange(0.5, 6, 0.5), edgecolor="black")
plt.xlabel("Rating")
plt.ylabel("Număr Evaluări")
plt.title("Distribuția Ratingurilor")
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(top_5_movies.index, top_5_movies.values)
plt.xlabel("ID Film")
plt.ylabel("Rating Mediu")
plt.title("Top 5 Filme cu Cel Mai Mare Rating Mediu")
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(num_ratings, average_rating)
plt.xlabel("Număr Evaluări")
plt.ylabel("Rating Mediu")
plt.title("Număr Evaluări vs. Rating Mediu")
plt.show()
