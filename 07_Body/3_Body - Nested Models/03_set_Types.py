#Python có một kiểu dữ liệu đặc biệt cho các tập hợp các mục duy nhất, tập hợp.
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

# Với điều này, ngay cả khi bạn nhận được yêu cầu có dữ liệu trùng lặp,
# nó sẽ được chuyển đổi thành một tập hợp các mục duy nhất.
#
# Và bất cứ khi nào bạn xuất dữ liệu đó, ngay cả khi nguồn có bản sao,
# nó sẽ được xuất dưới dạng một tập hợp các mục duy nhất.
#
# Và nó cũng sẽ được chú thích/ghi lại tương ứng.