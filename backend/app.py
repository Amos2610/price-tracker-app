from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/books', methods=['GET'])
def get_books():
    url = 'https://www.amazon.co.jp/gp/bestsellers/books/ref=zg_bs_nav_books_0'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    books = []
    items = soup.find_all("div", {"class": "zg-item-immersion"})[:9]  # 9冊分取得

    if not items:
        print("No items found. Check the HTML structure.")
        return jsonify(books)

    for item in items:
        title = item.find("div", {"class": "p13n-sc-truncate"})
        price_tag = item.find("span", {"class": "p13n-sc-price"})
        image = item.find("img")

        if title and price_tag and image:
            title = title.get_text(strip=True)
            price = price_tag.get_text(strip=True)
            image = image["src"]
            books.append({"title": title, "price": price, "image": image})
        else:
            print(f"Missing data in item: {item}")

    return jsonify(books)

if __name__ == '__main__':
    app.run(debug=True)
