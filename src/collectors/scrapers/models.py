from dataclasses import dataclass, field
from typing import List


@dataclass
class ScrapedItem:    
    id: str = ""
    url: str = ""
    title: str = ""
    address: str = ""
    price: int = 0
    description: str = ""
    bedrooms: int = 0
    bathrooms: int = 0
    receptions: int = 0
    epc_rating: str = ""
    image_url: str = ""
    tags: List[str] = field(default_factory=list)

    def __str__(self):
        return (
            f"Scraped Item = ({self.title}, price = £{self.price})"
        )
    
    def to_dict(self):
        return {
            "id": self.id,
            "url": self.url,
            "title": self.title
            # TODO: Complete conversion
        }