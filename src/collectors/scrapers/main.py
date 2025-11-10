import time
import json
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from scraper import PropertyScraper
from config import LONDON_AREAS
import json

url = 'https://www.zoopla.co.uk'

if __name__ == "__main__":
    items = []
    scraper = PropertyScraper()

    for area in LONDON_AREAS:
        items.extend(scraper.scrape_area(area))

    json.dump(items, open('data.json', 'w'))

    # with sync_playwright() as pw:
    #
    #     browser = pw.chromium.launch(headless=False)
    #
    #     page = browser.new_page()
    #
    #     page.goto(url)
    #
    #     # Accept the T&Cs
    #     cookie_button = page.locator("#accept")
    #     cookie_button.click()
    #
    #     search_input = page.locator("._1xvvvlo0.fjlmpi8")
    #     search_input.fill("Holborn, London")
    #
    #     # Press Enter
    #     page.keyboard.press("Enter")
    #
    #     time.sleep(2)
    #
    #
    #     # Get Listings
    #
    #     listing_urls = []
    #
    #     listing_cards = page.locator("._19tyedx0").all()
    #
    #     for index, card in enumerate(listing_cards, 1):
    #         link_element = card.locator("a").first
    #         href = link_element.get_attribute("href")
    #
    #         if href.startswith("/"):
    #             full_url = f"{url}{href}"
    #         else:
    #             full_url = href
    #
    #         listing_urls.append(full_url)
    #
    #     print(listing_urls)
    #     time.sleep(30)
    #
    #     # Extract Data From Page
    #
    #     listing_data = []
    #
    #     for listing_url in listing_urls:
    #         page.go_to(listing_url)
    #
    #         # Extracting Data
    #
    #         listing_item = {
    #             "url": listing_url,
    #             "title": None,
    #             "address": None,
    #             "price": None,
    #             "description": None,
    #             "bedrooms": None,
    #             "bathrooms": None,
    #             "receptions": None,
    #             "epc_rating": None,
    #             "image_url": None,
    #             "tags": []
    #         }
    #
    #         # Extract Title
    #         try:
    #             title_element = page.locator("h1.fjlmpi8._1kxlhi28").first
    #             listing_item["title"] = title_element.inner_text().strip()
    #         except:
    #             listing_item["title"] = ""
    #
    #         # Extract Address
    #         try:
    #             address_element = page.locator("address._1olqsf98")
    #             listing_item['address'] = address_element.inner_text().strip()
    #         except:
    #             listing_item["address"] = ""
    #
    #         # Extract Price
    #         try:
    #             price_element = page.locator("p.fjlmpi3.r4q9to1").first
    #             price_text = price_element.inner_text.strip()
    #             price_text = price_text.replace("£", "").replace(",","")
    #             price = int(price_text)
    #
    #             listing_item["price"] = price
    #         except:
    #             listing_item["price"] = 0
    #
    #
    #         listing_data.append(listing_item)
    #
    #         time.sleep(1)

