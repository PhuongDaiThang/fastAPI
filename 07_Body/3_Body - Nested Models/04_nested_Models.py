#Xác định một mô hình con
# Ví dụ: chúng ta có thể định nghĩa một model Image:


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Image(BaseModel):
    url: str
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

#Sử dụng mô hình con làm kiểu:Và sau đó chúng ta có thể sử dụng nó làm loại thuộc tính:
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Image(BaseModel):
    url: str
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

#bạn sẽ nhận được:

# Hỗ trợ trình chỉnh sửa (hoàn thành, v.v.), ngay cả đối với các models lồng nhau
# Chuyển đổi dữ liệu
# Xác nhận dữ liệu
# Tài liệu tự động