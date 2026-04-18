from pydantic import BaseModel

#monthテーブル
class month(BaseModel):
    ID: int
    Kyuryo: int
    SonotaShunyu: int
    Shokuhi: int
    Gaishoku: int
    Hitiyohin: int
    Koutsuhi: int
    Yatin: int
    Sabusuku: int
    Kounetsuhi: int
    Fuku: int
    Shoseki: int
    Sonota: int
