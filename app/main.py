from fastapi import FastAPI
from pydantic import BaseModel

from typing import List
from .sql_app import schemas
from .sql_app import database

app = FastAPI(
    title="Aviation API",
    description="This is a very fancy project, with auto docs for the API and everything",
    version="1.0.0",
    openapi_url="/api/v1/openapi.json"
)

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
def update_item(item_id: int, item: schemas.Item):
    return {"item_name": item.name, "item_id": item_id}

@app.put("/user/list")
def update_item(item_id: int, item: schemas.Item):
    return {"item_name": item.name, "item_id": item_id}
