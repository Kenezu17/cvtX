from fastapi import APIRouter

router = APIRouter(prefix="/convert", tags=["convert"])

@router.get("/")
def read_convert():
    return {"message": "Convert route is alive"}
