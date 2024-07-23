# Có thể kết hợp các khai báo Path, Query và yêu cầu một cách tự do và FastAPI sẽ biết phải làm gì.
#
# Và bạn cũng có thể khai báo các tham số nội dung là tùy chọn, bằng cách đặt default thành None:

from typing import Annotated

from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: str | None = None,
    item: Item | None = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results

# Lưu ý rằng, trong trường hợp này, item sẽ được lấy ra khỏi Body là tùy chọn. Vì nó có giá trị default None.