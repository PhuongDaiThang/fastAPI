# Ngoài các kiểu số ít thông thường như str, int, float, v.v.,
# bạn có thể sử dụng các kiểu số ít phức tạp hơn kế thừa từ str.
#
# Để xem tất cả các tùy chọn bạn có,
# hãy xem Pydantic's exotic types.
#
# Ví dụ: như trong model Image, chúng ta có field url,
# chúng ta có thể khai báo nó là một thể hiện của HttpUrl của Pydantic thay vì str:

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    image: Image | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
# Chuỗi sẽ được kiểm tra xem có phải là URL hợp lệ và được ghi lại trong Lược đồ JSON/OpenAPI như vậy không.