#Bạn có thể khai báo các tham số đường dẫn và nội dung yêu cầu cùng một lúc.

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}
#FastAPI sẽ nhận ra rằng các tham số hàm khớp với tham số đường dẫn phải được lấy từ đường dẫn và
# các tham số hàm được khai báo là mô hình Pydantic phải được lấy từ nội dung yêu cầu.
