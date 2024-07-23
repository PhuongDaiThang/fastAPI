# Trước Pydantic version 2 và trước FastAPI 0.100.0,
# tham số này được gọi là biểu thức chính quy thay vì pattern nhưng hiện tại không được dùng nữa.


from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(
    q: Annotated[
        str | None, Query(min_length=3, max_length=50, regex="^fixedquery$")
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Lưu ý: Nó không được dùng nữa và cần được cập nhật để sử dụng tham số mới: pattern.