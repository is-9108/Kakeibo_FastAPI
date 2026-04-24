from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

# transactionテーブル
class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True,index=True)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    amount = Column(Integer,nullable=False)
    memo = Column(String, nullable= True)

    categories = relationship("Category", back_populates="transactions")
