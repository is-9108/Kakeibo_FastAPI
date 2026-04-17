from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_transaction():
    return {"Transaction"}

@app.get("/category")
def get_category():
    return {"Category"}

@app.post("/save")
def save_transaction():
    return None

@app.post("/month")
def saveMonth():
    return None

@app.put("/change")
def change_transaction():
    return {"transaction"}

@app.delete("/delete")
def delete_transaction():
    return None