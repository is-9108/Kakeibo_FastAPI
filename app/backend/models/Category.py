from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from database import Base

#カテゴリテーブル
class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    is_income = Column(Boolean, nullable=False)

    transactions = relationship("Transaction", back_populates="categories")

