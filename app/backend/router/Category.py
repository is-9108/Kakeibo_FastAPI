from fastapi import APIRouter

router = APIRouter(prefix="/Category", tags=["Category"])

@router.get("/")
def get_category():
    return None