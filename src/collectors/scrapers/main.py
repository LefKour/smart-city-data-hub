import json
from scraper import PropertyScraper
from config import LONDON_AREAS, DB_URL
import json
from database import (create_engine, create_property, create_session, create_table)


if __name__ == "__main__":
    engine = create_engine(DB_URL)
    session = create_session(engine)

    create_table(engine)

    items = []
    scraper = PropertyScraper()

    for area in LONDON_AREAS:
        items.extend(scraper.scrape_area(area))

    # Load to database
    for item in items:
        create_property(item, session)