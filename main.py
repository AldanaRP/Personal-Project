from fastapi import FastAPI

app = FastAPI()

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
    item=items[idem_id]
    return item