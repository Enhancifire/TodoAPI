from typing import Optional
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

@app.get("/")
def read_root():
    return "Hello World"

@app.get('/item/{item_id}')
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.put('/item/{item_id}')
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
