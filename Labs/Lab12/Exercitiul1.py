import requests
from tabulate import tabulate

def get_users():
    """Interoghează API-ul și returnează lista de utilizatori."""
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/users")
        if response.status_code != 200:
            print(f"Eroare: API-ul a returnat codul de stare {response.status_code}.")
            return None
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Eroare la conectarea cu API-ul: {e}")
        return None

def display_users(users):
    """Afișează informațiile utilizatorilor într-un format tabelar."""
    table = []
    headers = ["ID", "Nume", "Username", "Email", "Oraș", "Companie", "Telefon", "Website"]

    for user in users:
        table.append([
            user.get("id"),
            user.get("name"),
            user.get("username"),
            user.get("email"),
            user.get("address", {}).get("city"),
            user.get("company", {}).get("name"),
            user.get("phone"),
            user.get("website"),
        ])

    print(tabulate(table, headers=headers, tablefmt="grid"))

def filter_users_by_city(users, city):
    """Filtrează utilizatorii după orașul specificat."""
    filtered_users = [user for user in users if user.get("address", {}).get("city") == city]
    return filtered_users

def main():
    print("Obținerea utilizatorilor de la API...")
    users = get_users()

    if users is None:
        return

    print("\nToți utilizatorii:")
    display_users(users)

    city = input("\nIntroduceți orașul pentru a filtra utilizatorii: ").strip()
    print(f"\nUtilizatori din orașul '{city}':")
    filtered_users = filter_users_by_city(users, city)

    if filtered_users:
        display_users(filtered_users)
    else:
        print(f"Nu există utilizatori din orașul '{city}'.")

if __name__ == "__main__":
    main()
