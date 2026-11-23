import requests
from bs4 import BeautifulSoup


def scrape_quotes():
    url = "https://quotes.toscrape.com/"

    response = requests.get(url)
    if response.status_code != 200:
        print("Не удалось загрузить страницу")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    quote_blocks = soup.find_all("div", class_="quote")

    print("--- Топ-5 цитат с сайта ---")
    for block in quote_blocks[:5]:
        text = block.find("span", class_="text").text
        author = block.find("small", class_="author").text

        print(f"«{text}» — {author}\n")


if __name__ == "__main__":
    scrape_quotes()