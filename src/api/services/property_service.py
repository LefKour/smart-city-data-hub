from sqlalchemy.orm import Session

from src.api.repositories.property_repository import PorpertyRepository

class PropertyService:
    
    def __init__(self, db: Session):
        self.db = db
        self.repository = PorpertyRepository
    
    def list_properties(self, skip: int = 0, limit: int = 100):
        return self.repository.get_all(self.db, skip=skip, limit=limit)
    
    def get_property(self, property_id: str):
        property_obj = self.repository.get_by_id(self.db, property_id)

        if property_obj is None:
            raise Exception()

        return property_obj
    
    def get_property_statistics(self):
        total_count = self.get_property_count()
        locations = self.get_search_locations()
        states = self.get_states()

        return {
            "total_properties": total_count,
            "unique_locations": len(locations)
        }