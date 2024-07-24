#FastAPI sẽ nhận ra và lấy dữ liệu đúng nơi:

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result
#Được nhận biết như sau:
# Nếu tham số cũng được khai báo trong đường dẫn, nó sẽ được sử dụng làm tham số đường dẫn.
#
# Nếu tham số thuộc loại số ít (như int, float, str, bool, v.v.) thì nó sẽ được hiểu là tham số truy vấn.
#
# Nếu tham số được khai báo là thuộc loại mô hình Pydantic, nó sẽ được hiểu là nội dung yêu cầu.