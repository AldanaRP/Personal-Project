from fastapi import FastAPI
from app.database.connection import engine
from app.database.base import Base
from app.models import user

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "API running"}



items = []

@app.get("/")
def root():
    return {"Hello": "World"} 

@app.post("/items")
def create_item(item: str):
    items.append(item)
    return items

@app.get("/item/{item_id}")
def get_item(item_id: int):
    if item_id < len(item):
        return item
    else:
        raise HTTPException(status_code=404, detail=f"Item {utem_id} not found")