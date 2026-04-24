from sqlalchemy import Column, Integer
from database import Base

#monthテーブル
class month(Base):
    __tablename__ = "month"
    id = Column(Integer,primary_key=True,index=True)
    kyuryo = Column(Integer,nullable=False)
    sonotaShunyu = Column(Integer,nullable=False)
    shokuhi = Column(Integer,nullable=False)
    gaishoku = Column(Integer,nullable=False)
    hitiyohin = Column(Integer,nullable=False)
    koutsuhi = Column(Integer,nullable=False)
    yatin = Column(Integer,nullable=False)
    sabusuku = Column(Integer,nullable=False)
    kounetsuhi = Column(Integer,nullable=False)
    fuku = Column(Integer,nullable=False)
    shoseki = Column(Integer,nullable=False)
    sonota = Column(Integer,nullable=False)