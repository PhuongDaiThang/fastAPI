# Có thể sử dụng các giá trị mặc định khác với None.
#
# Giả sử muốn khai báo tham số query q có độ dài tối thiểu là 3 và có giá trị default là "fixedquery":
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[str, Query(min_length=3)] = "fixedquery"):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

#Việc có một giá trị mặc định thuộc bất kỳ loại nào, kể cả None,
# làm cho tham số trở thành tùy chọn (không bắt buộc).