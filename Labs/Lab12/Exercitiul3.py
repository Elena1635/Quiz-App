import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

def get_crypto_prices():
    """Obține prețurile actuale ale Bitcoin și Ethereum în USD folosind API-ul CoinGecko."""
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return [
            ["Bitcoin", data["bitcoin"]["usd"]],
            ["Ethereum", data["ethereum"]["usd"]],
        ]
    except requests.exceptions.RequestException as e:
        print(f"Eroare la obținerea prețurilor criptomonedelor: {e}")
        return None

def get_latest_news():
    """Extrage cele mai recente 5 știri despre criptomonede de pe CoinDesk."""
    url = "https://www.coindesk.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Verifică structura site-ului pentru a găsi corect titlurile știrilor
        articles = soup.find_all('div', class_='card-title', limit=5)
        news = []
        for article in articles:
            title = article.get_text(strip=True)
            link = article.find('a')['href']
            if not link.startswith("http"):
                link = f"https://www.coindesk.com{link}"
            news.append((title, link))
        return news
    except requests.exceptions.RequestException as e:
        print(f"Eroare la obținerea știrilor: {e}")
        return None


def display_crypto_prices(prices):
    """Afișează prețurile criptomonedelor într-un format tabelar."""
    if prices:
        headers = ["Criptomonedă", "Preț (USD)"]
        print(tabulate(prices, headers=headers, tablefmt="grid"))
    else:
        print("Nu s-au putut obține prețurile criptomonedelor.")

def display_news(news):
    """Afișează știrile într-un format ușor de citit."""
    if news:
        print("\nCele mai recente știri despre criptomonede:")
        for i, (title, link) in enumerate(news, start=1):
            print(f"{i}. {title}")
            print(f"   Link: {link}")
    else:
        print("Nu s-au putut obține știrile despre criptomonede.")

def main():
    print("Obținerea informațiilor despre criptomonede și știri...")

    # Obține prețurile criptomonedelor
    prices = get_crypto_prices()
    print("\nPrețurile criptomonedelor:")
    display_crypto_prices(prices)

    # Obține știrile despre criptomonede
    news = get_latest_news()
    display_news(news)

if __name__ == "__main__":
    main()