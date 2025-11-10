import os

# Browser Settings
HEADLESS = True

BASE_URL = 'https://www.zoopla.co.uk'


SELECTORS = {
    'cookie_input': "#accept",
    'search_input': "._1xvvvlo0.fjlmpi8",
    'listing_card': "._19tyedx0",
    'pagination': "ol.jx0me43 li a",

    # Detail Selectors
    'address': "address._1olqsf98"
}

LONDON_AREAS = [
    "Holborn, London",
    "Shoreditch, London",
    "Camden, London",
    "Islington, London"
]

DB_URL = "postgresql://postgres:postgress@localhost:5432/smart-city-db"