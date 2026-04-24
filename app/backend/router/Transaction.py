from fastapi import APIRouter

router = APIRouter(prefix="/Transaction", tags=["Transaction"])

@router.get("/")
def get_transaction():
    return None

@router.get("/{id}")
def get_transactionbyId(id: int):
    return None

@router.post("/")
def create_transaction():
    return None

@router.put("/{id}")
def update_transaction(id: int):
    return None

@router.delete("/{id}")
def delete_transaction(id: int):
    return None