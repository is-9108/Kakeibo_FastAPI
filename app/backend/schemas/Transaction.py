from pydantic import BaseModel

class TransactionBase(BaseModel):
    category_id: int
    amount: int
    memo: str


class CreateTransaction(TransactionBase):
    pass

class UpdateTransaction(BaseModel):
    amount: int | None = None
    memo: str | None = None

class GetTransaction(TransactionBase):
    id: int

    class Config:
        from_attributes = True