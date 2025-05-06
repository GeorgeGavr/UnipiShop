import requests
from bs4 import BeautifulSoup
import json

def scrape_test(keyword=""):
    url = "https://books.toscrape.com/catalogue/page-1.html"
    base_url = "https://books.toscrape.com/catalogue/"
    results = []

    while url:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        for article in soup.select("article.product_pod"):
            title = article.h3.a["title"]
            price = article.select_one("p.price_color").text
            availability = article.select_one("p.availability").text.strip()
            rating = article.p["class"][1]
            link = base_url + article.h3.a["href"]

            results.append({
                "title": title,
                "price": price,
                "availability": availability,
                "rating": rating,
                "link": link
            })

        
        next_btn = soup.select_one("li.next a")
        if next_btn:
            page_num = int(url.split("page-")[1].split(".")[0]) + 1
            url = f"https://books.toscrape.com/catalogue/page-{page_num}.html"
        else:
            url = None

    return results
