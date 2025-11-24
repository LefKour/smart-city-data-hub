from fastapi import APIRouter, Query

router = APIRouter()

@router.get("/")
def list_properties(
        offset:int = Query(0, ge=0, description="Number of records to offset"),
        limit: int = Query(100, ge=1, description="Number of records to return"),
):
    return {"offset": offset, "limit": limit}