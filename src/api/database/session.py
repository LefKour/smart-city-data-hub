from src.database.database import database


def get_db():
    yield from database.get_postgres_session()

def get_mongo_db():
    return database.get_mongo_db()