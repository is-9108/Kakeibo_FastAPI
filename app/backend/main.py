from fastapi import FastAPI
from database import engine, Base
from router import Category, Month, Transaction

#テーブル作成
Base.metadata.create_all(bind=engine)

app = FastAPI()

#ルーター登録
app.include_router(Category.router)
app.include_router(Month.router)
app.include_router(Transaction.router)

@app.get("/")
def root():
    return {"message": "家計簿API"}
