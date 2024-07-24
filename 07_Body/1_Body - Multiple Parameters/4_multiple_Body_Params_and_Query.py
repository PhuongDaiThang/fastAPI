# Theo mặc định, các giá trị số ít được hiểu là tham số query,
# bạn không cần phải thêm query một cách rõ ràng mà chỉ cần thực hiện:
q: Union[str, None] = None
#hoặc
q: str | None = None #Bản 3.10+
#Ví dụ:
from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None


@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: Item,
    user: User,
    importance: Annotated[int, Body(gt=0)],
    q: str | None = None,
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    if q:
        results.update({"q": q})
    return results