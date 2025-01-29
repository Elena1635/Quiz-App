import requests
import urllib3

# Dezactivăm avertismentele SSL (dacă vrei să le dezactivezi complet)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_weather(city):
    """Obține informații despre vreme pentru un oraș specificat."""
    try:
        # Verificăm dacă city nu este doar un număr sau prea scurt
        if city.isdigit() or len(city) < 3:
            return "Orașul introdus nu este valid. Vă rugăm să introduceți un nume valid de oraș."

        url = f"https://wttr.in/{city}?format=%C+%t+%w"
        response = requests.get(url, timeout=10, verify=True)  # Activează verificarea certificatului SSL
        response.raise_for_status()  # Ridică excepție pentru coduri de eroare HTTP

        # Verificăm dacă răspunsul conține date valide
        if "404 Not Found" in response.text:
            return f"Nu am găsit informații pentru orașul '{city}'."

        return response.text
    except requests.exceptions.RequestException as e:
        return f"Eroare la conectarea la API: {e}"

def display_weather(data):
    """Afișează informațiile meteo într-un format ușor de citit."""
    try:
        conditions, temperature, wind = data.split()
        print(f"\nInformații meteo:\n")
        print(f"Condiții meteo: {conditions}")
        print(f"Temperatura curentă: {temperature}")
        print(f"Vânt: {wind}")
    except ValueError:
        print("Nu s-au putut extrage toate informațiile meteo din răspunsul API-ului.")

def main():
    print("Bun venit la scriptul meteo!")
    city = input("Introduceți numele orașului: ").strip()

    # Verificăm dacă orașul introdus este valid
    if not city.isalpha() or len(city) < 3:
        print("Orașul introdus nu este valid. Vă rugăm să introduceți un nume de oraș valid, mai lung de 2 caractere.")
        return

    print(f"\nObținerea informațiilor meteo pentru orașul '{city}'...")
    weather_data = get_weather(city)

    if weather_data.startswith("Eroare") or weather_data.startswith("Orașul introdus nu este valid"):
        print(weather_data)
    else:
        display_weather(weather_data)

if __name__ == "__main__":
    main()
