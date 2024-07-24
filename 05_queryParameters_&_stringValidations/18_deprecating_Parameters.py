# Bây giờ giả sử bạn không thích thông số này nữa.
#
# Bạn phải để nó ở đó một lúc vì có khách hàng đang sử dụng nó,
# nhưng bạn muốn tài liệu hiển thị rõ ràng rằng nó không được dùng nữa.
# 
# Sau đó chuyển tham số deprecated=True tới Query:
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(
    q: Annotated[
        str | None,
        Query(
            alias="item-query",
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            max_length=50,
            pattern="^fixedquery$",
            deprecated=True,
        ),
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results