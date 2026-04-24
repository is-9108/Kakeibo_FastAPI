from fastapi import APIRouter

router = APIRouter(prefix="/Month",tags=["Month"])

@router.get("/")
def get_month():
    return None

@router.post("/")
def create_month():
    return None