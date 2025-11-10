import time
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from config import HEADLESS, BASE_URL, SELECTORS
from typing import List
from .models import ScrapedItem


class PropertyScraper:

    def __init__(self, headless: bool = HEADLESS):
        self.headless = headless
        self.browser = None

    def _create_page(self):
        page = self.browser.new_page(
            viewport = {
                "width": 1920,
                "height": 1080
            }
        )

        page.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            });
        """)

        return page

    def _accept_cookies(self, page):
        try:
            page.wait_for_selector(SELECTORS['cookie_input'], timeout=3000)
            page.click(SELECTORS['cookie_input'])
            time.sleep(2)
        except:
            pass

    def _search_location(self, page, location: str):
        page.goto(BASE_URL, wait_until="domcontentloaded")

        self._accept_cookies(page)

        page.wait_for_selector(SELECTORS['search_input'], timeout=3000)
        page.fill(SELECTORS['search_input'], location)

        page.keyboard.press("Enter")

    def _collect_listing_urls(self, page) -> List[str]:
        current_page = 1
        while True:
            page_urls = []

            listings = page.locator(SELECTORS['listing_card']).all()

            for listing in listings:
                link = listing.locator("a").first
                if link.count() > 0:
                    href = link.attr("href")
                    if href:
                        page_urls.append(f"{BASE_URL}{href}" if href.startwith("/") else href)


            try:
                pagination = page.locator(SELECTORS['pagination'])
                pagination_links = pagination.all()

                next_page_url = None
                for link in pagination_links:
                    href = link.attr("href")
                    text = link.text_content()

                    if href and (f"pn={current_page + 1}" in href or "next" in text.lower()):
                        next_page_url = f"{BASE_URL}{href}" if href.startwith("/") else href
                        break

                if next_page_url:
                    page.goto(next_page_url, wait_until="domcontentloaded")
                    time.sleep(2)
                    current_page += 1
                else:
                    break
            except:
                break

        return page_urls

    def _scrape_detail_page(self, page, soup: BeautifulSoup, location: str):
        scraped_item = ScrapedItem()

        # TODO: Extract the rest of the properties

        address_element = soup.select_one(SELECTORS['address'])
        if address_element:
            scraped_item.address = address_element.get_text(strip=True)

        return scraped_item

    def _scrape_listings(self, page, listing_urls: List[str], location: str):
        scraped_items = []

        for index, listing_url in enumerate(listing_urls):
            page.goto(listing_url, wait_until="domcontentloaded")
            time.sleep(2)

            detail_html = page.inner_html("body")
            detail_soup = BeautifulSoup(detail_html, "html.parser")

            scraped_item = self._scrape_detail_page(page, detail_soup, location)
            scraped_items.append(scraped_item)

        return scraped_items

    def scrape_area(self, location: str):

        with sync_playwright() as pw:
            self.browser = pw.chromium.launch(headless=self.headless)

            page = self._create_page()

            # Search for the location
            self._search_location(location)

            # Collect the listings
            urls = self._collect_listing_urls(page)

            # Scrape the listings
            scraped_items = self._scrape_listings(page, listing_urls=urls, location=location)

            return scraped_items