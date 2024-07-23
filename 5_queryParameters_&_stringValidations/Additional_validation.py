#Nâng cấp phiên bản FastAPI lên ít nhất 0.95.1 trước khi sử dụng Annotated.
#Nhập Annotated từ typing
from typing import Annotated
# Nhập Query từ FastAPI
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
#độ dài q không được vượt quá 50 ký tự
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results