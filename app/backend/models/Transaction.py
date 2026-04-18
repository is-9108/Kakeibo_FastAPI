from fastapi import FastAPI
from pydantic import BaseModel

# transactionテーブル
class transaction(BaseModel):
    ID: int
    CategoryID: int
    Amount: int
    Memo: str

# リクエストモデル
class request(BaseModel):
    CategoryID: int
    Amount: int
    Memo: str

#レスポンス
class response(BaseModel):
    ID: int
    CategoryID: int
    Amount: int
    Memo: int
    