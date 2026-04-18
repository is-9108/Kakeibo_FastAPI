from pydantic import BaseModel

#カテゴリテーブル
class category(BaseModel):
    ID: int
    Name: str
    IsIncome: bool

#リクエスト
class request(BaseModel):
    ID: int

#レスポンス
class response(BaseModel):
    ID: int
    Name: str
    IsIncome: bool