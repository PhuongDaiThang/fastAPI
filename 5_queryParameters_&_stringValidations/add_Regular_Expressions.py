from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()
#biểu thức chính quy cụ thể này sẽ kiểm tra xem giá trị tham số đã nhận:
# ^: bắt đầu bằng các ký tự sau, không có ký tự nào trước đó.
#
# fixedquery: có giá trị cố định chính xác.
#
# $: kết thúc ở đó, không còn ký tự nào sau truy vấn cố định.

@app.get("/items/")
async def read_items(
    q: Annotated[
        str | None, Query(min_length=3, max_length=50, pattern="^fixedquery$")
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results