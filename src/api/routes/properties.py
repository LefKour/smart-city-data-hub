from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session

from src.api.services.property_service import PropertyService
from src.api.database.session import get_db


router = APIRouter()


def get_property_service(db: Session = Depends(get_db)):
    return PropertyService(db)

# Routes
@router.get("/")
def list_properties(
        offset:int = Query(0, ge=0, description="Number of records to offset"),
        limit: int = Query(100, ge=1, description="Number of records to return"),
        service: PropertyService = Depends(get_property_service)
):
   return service.list_properties(skip=offset, limit=limit)

@router.get("/{property_id}")
def get_propert(
    property_id: str,
    service: PropertyService = Depends(get_property_service)
    ):
    return service.get_property(property_id)

@router.get("/stats/overview")
def get_property_statistics(
    service: PropertyService = Depends(get_property_service)
):
    return service.get_property_statistics()