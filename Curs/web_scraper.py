"""
import requests
from bs4 import BeautifulSoup
import csv
import matplotlib.pyplot as plt

# 1. Alegerea site-ului de știri (exemplu: BBC News - structura HTML trebuie verificată înainte)
BASE_URL = "https://www.bbc.com/news"

# 2. Funcție pentru extragerea datelor
def extract_data(base_url):
    response = requests.get(base_url)
    print(response.status_code)  # Statusul HTTP
    print(response.text[:500])  # Primele 500 de caractere din răspuns

    if response.status_code != 200:
        print("Failed to retrieve the page")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    articles = []

    # Găsirea articolelor relevante (examinați structura HTML cu Inspect Element)
    for item in soup.find_all('a', class_='gs-c-promo-heading'):
        title = item.text.strip()
        url = item['href']
        if not url.startswith('http'):
            url = "https://www.bbc.com" + url

        summary_tag = item.find_next('p', class_='gs-c-promo-summary')
        summary = summary_tag.text.strip() if summary_tag else "No summary available"

        articles.append({
            'title': title,
            'summary': summary,
            'url': url
        })

    print(f"Am găsit {len(articles)} articole.")
    return articles

# 3. Salvarea datelor într-un fișier CSV
def save_to_csv(articles, filename="news_data.csv"):
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['title', 'summary', 'url'])
            writer.writeheader()
            writer.writerows(articles)
        print(f"Fișierul CSV '{filename}' a fost creat cu succes și conține {len(articles)} articole.")
    except Exception as e:
        print(f"Eroare la salvarea fișierului CSV: {e}")

# 4. Filtrarea articolelor după cuvânt cheie
def filter_articles(articles, keyword):
    return [article for article in articles if keyword.lower() in article['title'].lower()]

# 5. Vizualizarea datelor
def visualize_data(articles):
    categories = {}
    for article in articles:
        # Determinați categoria (în funcție de structura site-ului)
        category = "Uncategorized"  # Actualizați după cum este necesar
        categories[category] = categories.get(category, 0) + 1

    # Crearea graficului cu bare
    plt.bar(categories.keys(), categories.values(), color='skyblue')
    plt.title("Distribuția articolelor pe categorii")
    plt.xlabel("Categorie")
    plt.ylabel("Număr de articole")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Executarea scriptului
def main():
    print("Extragem datele de pe site-ul de știri...")
    articles = extract_data(BASE_URL)

    if not articles:
        print("Nu s-au găsit articole.")
        return

    print(f"Am extras {len(articles)} articole.")
    save_to_csv(articles)

    keyword = input("Introduceți un cuvânt cheie pentru filtrare: ")
    filtered = filter_articles(articles, keyword)

    print(f"Am găsit {len(filtered)} articole potrivite cu cuvântul cheie '{keyword}':")
    for i, article in enumerate(filtered, 1):
        print(f"{i}. {article['title']} - {article['summary']}")

    visualize_data(articles)

if __name__ == "__main__":
    main()
"""
import requests
from bs4 import BeautifulSoup
import csv
import matplotlib.pyplot as plt
from collections import Counter


def get_news():
    url = "https://www.bbc.com/news"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(url, headers=headers)

    print(f"Status code: {response.status_code}")  # Debugging
    if response.status_code != 200:
        print("Eroare la accesarea site-ului!")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    print(soup.prettify()[:1000])  # Debugging

    articles = soup.find_all("article")
    print(f"Articole găsite: {len(articles)}")  # Debugging
    with open("bbc_news.html", "w", encoding="utf-8") as file:
        file.write(soup.prettify())

    print("Fișierul bbc_news.html a fost salvat. Deschide-l și inspectează structura HTML.")

    news_data = []
    for article in articles:
        title_tag = article.find("h3")
        summary_tag = article.find("p")
        link_tag = article.find("a", href=True)

        if title_tag and link_tag:
            title = title_tag.get_text(strip=True)
            summary = summary_tag.get_text(strip=True) if summary_tag else "N/A"
            link = "https://www.bbc.com" + link_tag["href"]

            print(f"Titlu: {title}")  # Debugging
            print(f"Rezumat: {summary}")
            print(f"Link: {link}")
            print("-" * 40)

            news_data.append([title, summary, link])

    return news_data


def save_to_csv(news_data, filename="news.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Titlu", "Rezumat", "URL"])
        writer.writerows(news_data)
    print(f"Datele au fost salvate în {filename}")


def filter_news(keyword, filename="news.csv"):
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Sărim peste antet
        filtered = [row for row in reader if keyword.lower() in row[0].lower() or keyword.lower() in row[1].lower()]

    print("Articole potrivite:")
    for i, row in enumerate(filtered, start=1):
        print(f"{i}. {row[0]} - {row[1]}")


def visualize_news(filename="news.csv"):
    categories = []

    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Sărim peste antet
        for row in reader:
            if "tehnologie" in row[0].lower():
                categories.append("Tehnologie")
            elif "economie" in row[0].lower():
                categories.append("Economie")
            else:
                categories.append("Altele")

    counter = Counter(categories)
    plt.bar(counter.keys(), counter.values(), color=['blue', 'green', 'red'])
    plt.xlabel("Categorie")
    plt.ylabel("Număr de articole")
    plt.title("Distribuția articolelor pe categorii")
    plt.show()


if __name__ == "__main__":
    news = get_news()
    if news:
        save_to_csv(news)
        keyword = input("Introduceți un cuvânt cheie pentru filtrare: ")
        filter_news(keyword)
        visualize_news()
