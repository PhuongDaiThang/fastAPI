#send Data: POST, PUT, DELETE, PATCH
#GET: truong hop phuc tạp (co the khong ho tro voi proxies in the middle)


# import BaseModel from pydantic:
from fastapi import FastAPI
from pydantic import BaseModel

#Khai bao mo hinh du lieu duoi dang class:
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item