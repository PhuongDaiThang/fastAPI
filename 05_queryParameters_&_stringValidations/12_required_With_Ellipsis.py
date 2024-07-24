# Có thể đặt default thành giá trị: ...
# Nó được Pydantic và FastAPI sử dụng để khai báo rõ ràng rằng một giá trị là bắt buộc.

# FastAPI biết rằng tham số này là bắt buộc.
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[str, Query(min_length=3)] = ...):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results