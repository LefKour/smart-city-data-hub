from sqlalchemy.orm import Session
from src.core.models.property import Property

class PorpertyRepository:

    @staticmethod
    def get_all(
        db: Session,
        skip: int = 0, 
        limit: int = 100
    ):
        return db.query((Property).offset(skip).limit(limit).all())
    
    @staticmethod
    def get_by_id(db: Session, property_id: str):
        return db.query((Property).filter(Property.id == property_id)).first()
    

    @staticmethod
    def get_count(dbL Session):
        return db.query((Property)).count()