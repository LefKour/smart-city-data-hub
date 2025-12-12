from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from pymongo import MongoClient

from .config import Config

Base = declarative_base()

class Database:

    def __init__(self):
        self.postgres_engine = create_engine(
            Config.get_sql_url(),
            echo = True,
            pool_pre_pring = True,
            pool_size = 5,
            max_overflow = 10,
        )

        self.session =sessionmaker(
            autocommit = False,
            autoflush = False,
            bind = self.postgres_engine
        )

        self.mongo_client = MongoClient(Config.get_mongodb_url())
        self.mongo_db = self.mongo_client(Config.MONGODB_NAME)

    
    def get_postgres_session(self):
        db = self.session
        try:
            yield db
        finally:
            db.close()

    def get_mongo_db(self):
        return self.mongo_db
    
    def create_tables(self):
        Base.metadata.create_all(self.postgres_engine)

    def close(self):
        self.postgres_engine.dispose()
        self.mongo_client.close()

database = Database()    
