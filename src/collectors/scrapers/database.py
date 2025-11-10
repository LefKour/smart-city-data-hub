from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from .models import Base, ScrapedItem
from .db_models import Property

def create_engine(database_url: str):
    return create_engine(
        database_url=database_url,
        pool_pre_ping = True,
        echo = False
    )

def create_session(db_engine):
    return sessionmaker(
        autocommit = False,
        autoflush = False,
        bind = db_engine
    )

def create_table(db_engine):
    Base.metadata.create_all(bind = db_engine)

def create_property(item: ScrapedItem, session: Session):
    property_obj = Property.from_scraped_item(item)
    session.add(property_obj)
    session.commit()
    session.refresh(property_obj)
    