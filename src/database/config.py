import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).parents[2] / '.env'
load_dotenv(dotenv_path=env_path)


class Config:

    # PostgreSQL Config
    POSTGRES_HOST = os.getenv("PS_DB_HOST", "localhost")
    POSTGRES_PORT = os.getenv("PS_DB_PORT", "5432")
    POSTGRES_USER = os.getenv("PS_DB_USER", "postgres")
    POSTGRES_PASSWORD = os.getenv("PS_DB_PASSWORD", "postgres")
    POSTGRES_DB = os.getenv("PS_DB_NAME", "smart-city-hub")

    # MongoDB Config
    MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
    MONGODB_NAME = os.getenv("MONGODB_NAME", "smart-city-hub")

    @classmethod
    def get_sql_url(cls) -> str:
        return (
            f"postgresql://{cls.POSTGRES_USER}:{cls.POSTGRES_PASSWORD}@{cls.POSTGRES_HOST}:{cls.POSTGRES_PORT}/{cls.POSTGRES_DB}"
        )
    
    @classmethod
    def get_mongodb_url(cls) -> str:
        return cls.MONGODB_URL
