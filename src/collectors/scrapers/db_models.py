from sqlalchemy import Column, String, Integer, Text, DateTime, ARRAY
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from .models import ScrapedItem

Base = declarative_base()

class Property(Base):

    __tablename__ =  "properties"

    id = Column(String(32), primary_key=True, index=True)

    url = Column(String(500), unique=True, nullable=False) 
    title = Column(String(500), nullable=False)
    address = Column(String(500))
    price = Column(Integer)
    description = Column(String(2000))
    bedrooms = Column(Integer)
    bathrooms = Column(Integer)
    receptions = Column(Integer)
    epc_rating = Column(String(5))
    image_url = Column(String(100))
    tags = Column(ARRAY(String), default=[])

    @classmethod
    def from_scraped_item(cls, item: ScrapedItem):
        return cls(
            id = item.id,
            url = item.url,
            title = item.title,
            address = item.address,
            price = item.price,
            description = item.description,
            bedrooms = item.bedrooms,
            bathrooms = item.bathrooms,
            receptions = item.receptions,
            epc_rationg = item.epc_rating,
            image_url = item.image_url,
            tags = item.tags
        )

