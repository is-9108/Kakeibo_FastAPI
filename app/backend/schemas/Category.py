from pydantic import BaseModel

class CategoryBase(BaseModel):
    name: str
    is_income: bool


class CategoryRead(CategoryBase):
    id: int

    class Config:
        from_attributes = True