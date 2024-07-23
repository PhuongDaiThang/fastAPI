# Nếu bạn muốn nó mong đợi một JSON có một item chính và bên trong nó là nội dung model,
# giống như khi bạn khai báo các tham số body bổ sung, bạn có thể sử dụng nhúng tham số Body đặc biệt:
item: Item = Body(embed=True)
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


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results

#Trong trường hợp này FastAPI sẽ có bpdy như:
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    }
}
#thay vì:
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2
}