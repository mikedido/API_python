from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Test API", openapi_url="/api/v1/openapi.json")

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

@app.get("/", tags=["login"])
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}", tags=["login"])
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/users/{user_id}", tags=["user"])
def read_items(user_id: int, q: str = None):
    return {"user_id": user_id, "q": q}

@app.put("/items/{item_id}", tags=["user"])
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.put("/user/list")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
