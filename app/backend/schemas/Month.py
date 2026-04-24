from pydantic import BaseModel

class MonthBase(BaseModel):
    kyuryo: int
    sonotaShunyu: int
    shokuhi: int
    gaishoku: int
    hitiyohin: int
    koutsuhi: int
    yatin: int
    sabusuku: int
    kounetsuhi: int
    fuku: int
    shoseki: int
    sonota: int

class CreateMonth(MonthBase):
    pass

class GetMonth(MonthBase):
    id: int
    
    class Config:
        from_attributes = True