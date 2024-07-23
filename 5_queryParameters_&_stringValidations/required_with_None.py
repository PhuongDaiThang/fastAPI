# Bạn có thể khai báo rằng một tham số có thể chấp nhận None, nhưng điều đó vẫn là bắt buộc.
# Điều này sẽ buộc khách hàng gửi một giá trị, ngay cả khi giá trị đó là None.
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(min_length=3)] = ...):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

#Hãy nhớ rằng trong hầu hết các trường hợp, khi cần một cái gì đó,
#bạn có thể chỉ cần bỏ qua giá trị mặc định, như vậy thông thường bạn không phải sử dụng ....